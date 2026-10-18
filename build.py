#!/usr/bin/env python3
"""Build RP01 preprint and Chinese explanation; no upload/network calls.

Python 3.10+, Markdown 3.x, and a TeX installation are required for all targets.
The verification entry point uses only the Python standard library.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output' / 'pdf'

def protect_math(source):
    found = []
    pattern = r'\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]|(?<!\\)\$([^$\n]+?)(?<!\\)\$|\\\(([\s\S]*?)\\\)'
    def sub(m):
        display = m.group(1) is not None or m.group(2) is not None
        value = next(g for g in m.groups() if g is not None).strip()
        value = re.sub(r'\n\s*\n', '\n', value)
        key = f'RPXMATH{len(found):05d}TOKEN'
        found.append((key, value, display))
        return '\n\n' + key + '\n\n' if display else key
    return re.sub(pattern, sub, source), found

def text_tex(value):
    repl = {'\\':r'\textbackslash{}', '&':r'\&', '%':r'\%', '$':r'\$',
            '#':r'\#', '_':r'\_', '{':r'\{', '}':r'\}', '~':r'\textasciitilde{}',
            '^':r'\textasciicircum{}'}
    return ''.join(repl.get(c,c) for c in value)

def html_to_tex(content):
    tree = ET.fromstring('<root>' + content + '</root>')
    def inner(node):
        return text_tex(node.text or '') + ''.join(visit(c) + text_tex(c.tail or '') for c in node)
    def visit(node):
        tag = node.tag
        if tag in ('h1','h2','h3','h4'):
            cmd = {'h1':'chapter','h2':'section','h3':'subsection','h4':'subsubsection'}[tag]
            title=re.sub(r'^\d+(?:\.\d+)*\s+', '', inner(node))
            title=re.sub(r'^第[一二三四五六七八九十]+章[\s　]*', '', title)
            if tag=='h1' and title=='阅读路线与术语索引':
                return '\n\\chapter*{'+title+'}\\addcontentsline{toc}{chapter}{'+title+'}\n'
            keep='\\Needspace{7\\baselineskip}\n' if tag in ('h2','h3') else ''
            return '\n'+keep+'\\' + cmd + '{' + title + '}\n'
        if tag == 'p':
            if (node.text or '').strip()=='RPXMAINSTARTTOKEN':
                return '\n\\tableofcontents\n\\mainmatter\n'
            content=inner(node)
            keep='\\Needspace{5\\baselineskip}\n' if 0<len(content.strip())<45 and 'RPXMATH' not in content else ''
            return '\n' + keep + content + '\n\n'
        if tag == 'strong': return r'\textbf{' + inner(node) + '}'
        if tag == 'em': return r'\emph{' + inner(node) + '}'
        if tag == 'code': return r'\texttt{' + inner(node) + '}'
        if tag == 'a':
            url=node.get('href','')
            if url.startswith('#'):
                m=re.fullmatch(r'#ch-(\d+)(?:-sec-(\d+))?',url)
                if m:
                    dest=('chapter.'+str(int(m[1]))) if m[2] is None else ('section.'+str(int(m[1]))+'.'+str(int(m[2])))
                    return r'\hyperlink{'+dest+'}{'+inner(node)+'}'
                return inner(node)
            return r'\href{' + url.replace('%',r'\%').replace('#',r'\#') + '}{' + inner(node) + '}'
        if tag in ('ul','ol'):
            env='itemize' if tag=='ul' else 'enumerate'
            return '\n\\begin{' + env + '}\n' + inner(node) + '\n\\end{' + env + '}\n'
        if tag=='li': return '\n\\item ' + inner(node)
        if tag=='blockquote': return '\n\\begin{quote}\n'+inner(node)+'\n\\end{quote}\n'
        if tag=='hr': return '\n\\medskip\\hrule\\medskip\n'
        if tag=='br': return '\\\\\n'
        if tag=='table':
            rows=list(node.iter('tr'))
            count=max(len(list(r)) for r in rows)
            width=(.96-.025*(count-1))/count
            spec='@{}' + ('p{'+f'{width:.4f}'+r'\linewidth}' + '@{\\hspace{.025\\linewidth}}')*(count-1) + 'p{'+f'{width:.4f}'+r'\linewidth}@{}'
            result='\n\\begin{longtable}{'+spec+'}\n\\toprule\n'
            for i,row in enumerate(rows):
                result+=' & '.join(inner(c).strip() for c in row)+' \\\\\n'
                if i==0: result+='\\midrule\n\\endhead\n'
            return result+'\\bottomrule\n\\end{longtable}\n'
        if tag=='pre': return '\n\\begin{quote}\\ttfamily\\small\n'+inner(node)+'\n\\end{quote}\n'
        return inner(node)
    return inner(tree)

def explain_sources():
    import markdown
    chapters=sorted((ROOT/'explainer'/'chapters').glob('*.md'))
    if len(chapters)!=8: raise RuntimeError(f'Expected eight chapters; found {len(chapters)}')
    chapter_text='\n\n'.join(p.read_text() for p in chapters)
    front=(ROOT/'explainer'/'FRONTMATTER.md').read_text()
    merged=front+'\n\nRPXMAINSTARTTOKEN\n\n'+chapter_text
    (ROOT/'explainer'/'RP01_EXPLAINED_ZH.md').write_text(front+'\n\n'+chapter_text, encoding='utf-8')
    protected,maps=protect_math(merged)
    body=markdown.markdown(protected, extensions=['tables','fenced_code','sane_lists'])
    latex=html_to_tex(body)
    # Give PDF bookmarks plain text for mathematical section titles.
    def heading_math(match):
        text=match.group(0)
        for key,value,display in maps:
            if key in text:
                plain=re.sub(r'\\([A-Za-z]+)',r'\1',value)
                plain=re.sub(r'[{}_^]','',plain)
                text=text.replace(key,r'\texorpdfstring{\('+value+r'\)}{'+text_tex(plain)+'}')
        return text
    latex=re.sub(r'\\(?:chapter|section|subsection|subsubsection)\{[^\n]*\}',heading_math,latex)
    for key,value,display in maps:
        latex=latex.replace(key, ('\\[\n'+value+'\n\\]') if display else ('\\('+value+'\\)'))
    preamble=r'''\documentclass[UTF8,fontset=fandol,zihao=-4,openany,oneside]{ctexbook}
\usepackage[a4paper,margin=25mm,headheight=15pt]{geometry}
\usepackage{amsmath,amssymb,mathtools,booktabs,longtable,array,enumitem,needspace}
\usepackage{microtype}
\usepackage[unicode,colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!55!black]{hyperref}
\usepackage{xcolor,bookmark,fancyhdr}
\allowdisplaybreaks[2]
\setlength{\emergencystretch}{3em}
\setlist{itemsep=.35em,topsep=.4em}
\renewcommand{\arraystretch}{1.3}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small RP01：完整中文解析}
\fancyhead[R]{\small v0.1.0 · 2026-10-17}
\fancyfoot[C]{\thepage}
\hypersetup{pdftitle={RP01完整中文论文解析},pdfauthor={Qi Liu},pdfsubject={Companion to preprint v0.1.0}}
\title{RP01 完整中文论文解析\\\large 从群计数到偶数半维数等号群分类}
\author{Qi Liu\\\small AI辅助整理的中文阅读材料}
\date{对应预印本 v0.1.0\\2026年10月17日}
\begin{document}
\frontmatter\maketitle
\chapter*{版本与使用说明}\addcontentsline{toc}{chapter}{版本与使用说明}
本解析对应英文论文 \emph{Extremal Klein Four Counts in Semi-Extraspecial 2-Groups}，
预印本 v0.1.0（2026-10-17），文件为 \texttt{RP01\_preprint.pdf}。
对应英文稿为19页；定义、命题与公式编号沿用该版本。
解析的章号仅用于教学导航；原稿定位以文中“原稿”编号为准。
这里的解释、背景与展开计算不构成新的研究定理；有标识的教学补充亦不作为原创贡献。
数学探索、证明发展、计算检查、文献核对与文本生成有生成式AI参与，
包括OpenAI Codex/ChatGPT及记录中的Muse Spark 1.3。
材料交付不表示作者已经阅读或人工核验全部论证，也不是外部同行评审。
阅读本解析不需要答题、打卡或等待另一次对话。
引用键与英文稿一致，书目信息集中列在最后一章。
原创解析文字采用\href{https://creativecommons.org/licenses/by/4.0/}{CC BY 4.0}；构建与阅读代码MIT，MathJax另保留Apache-2.0。
英文论文：\href{https://doi.org/10.5281/zenodo.23450418}{doi:10.5281/zenodo.23450418}；配套资料：\href{https://doi.org/10.5281/zenodo.23450447}{doi:10.5281/zenodo.23450447}。
'''
    tex=preamble+latex+'\n\\end{document}\n'
    texpath=ROOT/'explainer'/'tex'/'main.tex'
    texpath.parent.mkdir(exist_ok=True)
    texpath.write_text(tex,encoding='utf-8')
    # HTML contains its mathematical renderer. No CDN is used at read time.
    for key,value,display in maps:
        delimiter=('\\[', '\\]') if display else ('\\(', '\\)')
        wrap='div' if display else 'span'
        # MathJax's tag parser is already in text mode; nested \\text is redundant.
        render_value=re.sub(r'\\tag\{\\text\{([^{}]*)\}\}',r'\\tag{\1}',value)
        rendered='<'+wrap+' class="math-source" data-tex="'+html.escape(value,quote=True)+'">'+html.escape(delimiter[0]+render_value+delimiter[1])+'</'+wrap+'>'
        if display: body=body.replace('<p>'+key+'</p>',rendered)
        body=body.replace(key,rendered)
    body=body.replace('<p>RPXMAINSTARTTOKEN</p>','')
    toc=[]; chapter=0; section=0
    def anchor(m):
        nonlocal chapter,section
        tag,title=m.group(1),m.group(2)
        if tag=='h1' and title=='阅读路线与术语索引': ident='reading-map'
        elif tag=='h1': chapter+=1;section=0; ident=f'ch-{chapter:02d}'
        else: section+=1;ident=f'ch-{chapter:02d}-sec-{section:02d}'
        plain=re.sub('<[^>]+>','',title)
        toc.append((tag,ident,plain))
        return f'<{tag} id="{ident}">{title}<a class="permalink" href="#{ident}" aria-label="本节链接"> §</a></{tag}>'
    body=re.sub(r'<(h[123])>(.*?)</\1>',anchor,body,flags=re.S)
    nav=''.join('<a class="toc-'+tag+'" href="#'+ident+'">'+label+'</a>' for tag,ident,label in toc)
    style=(ROOT/'explainer'/'assets'/'reader.css').read_text()
    search=(ROOT/'explainer'/'assets'/'reader.js').read_text()
    mathjax=(ROOT/'explainer'/'assets'/'tex-svg-full.js').read_text()
    licence=(ROOT/'explainer'/'assets'/'MATHJAX-LICENSE.txt').read_text()
    original_notice = '<!-- Original RP01 explanation prose: CC BY 4.0; https://creativecommons.org/licenses/by/4.0/\nOriginal reader layout/search code: MIT; complete notice follows.\n' + (ROOT/'LICENSES'/'MIT.txt').read_text() + '\n-->\n'
    header=original_notice+'<!-- MathJax 3.2.2; Apache-2.0; full licence follows.\n'+licence+'\n-->\n'+'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>RP01完整中文论文解析 · v0.1.0</title><style>'''+style+'''</style>
<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']],packages:{'[+]':['ams','newcommand','textmacros']},maxBuffer:40000},svg:{fontCache:'local'},options:{enableMenu:false}};</script>
<script>'''+mathjax.replace('</script','<\\/script')+'''</script></head><body><header><strong>RP01完整中文解析</strong><span>v0.1.0 · 2026-10-17</span><button id="tocToggle" aria-controls="toc">目录</button><label>页内搜索 <input id="search" type="search" placeholder="输入词语或公式的TeX名称"></label><button id="searchPrev">上一处</button><button id="searchNext">下一处</button><output id="searchCount"></output></header><nav id="toc" aria-label="章节目录">'''+nav+'''</nav><main><div class="version-note"><p>对应论文：<a href="https://doi.org/10.5281/zenodo.23450418">预印本v0.1.0（论文DOI）</a>；<a href="https://doi.org/10.5281/zenodo.23450447">配套资料DOI</a>。本解析的教学章号与英文命题编号分别保留；请按各节“原稿”定位交叉阅读。数学公式渲染资源已嵌入，无需联网；只在点击外部文献链接时联网。可用浏览器搜索或上方搜索框。AI参与数学及文本生成；不表示作者已经完成全部人工核验。</p></div>'''
    page=header+body+'<footer>RP01 v0.1.0；正文CC BY 4.0，原创阅读脚本MIT，MathJax Apache-2.0；预印本不等于同行评审。</footer></main><script>'+search+'</script></body></html>'
    (ROOT/'explainer'/'RP01_EXPLAINED_ZH.html').write_text(page,encoding='utf-8')
    print(json.dumps({'chapters':len(chapters),'math_expressions':len(maps),'markdown_chars':len(merged),'headings':len(toc)},ensure_ascii=False))

def compile_tex(source, name, engine):
    outdir=ROOT/'tmp'/'pdfs'/name
    outdir.mkdir(parents=True,exist_ok=True); OUT.mkdir(parents=True,exist_ok=True)
    binary=shutil.which(engine)
    if not binary:
        p=Path('/Library/TeX/texbin')/engine
        if p.exists(): binary=str(p)
    if not binary: raise RuntimeError(f'{engine} not found: install a normal TeX distribution before building PDFs')
    for run in range(3):
        proc=subprocess.run([binary,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(outdir),source.name],cwd=source.parent,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (outdir/f'pass-{run+1}.log').write_text(proc.stdout)
        if proc.returncode: raise RuntimeError(f'TeX failed: see {outdir}/pass-{run+1}.log')
    shutil.copy2(outdir/(source.stem+'.pdf'),OUT/(name+'.pdf'))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target',choices=['paper','explainer','html','all'])
    args=parser.parse_args()
    if args.target in ('html','explainer','all'): explain_sources()
    if args.target in ('paper','all'): compile_tex(ROOT/'paper'/'main.tex','RP01_preprint','pdflatex')
    if args.target in ('explainer','all'): compile_tex(ROOT/'explainer'/'tex'/'main.tex','RP01_EXPLAINED_ZH','xelatex')

if __name__=='__main__': main()
