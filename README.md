# Extremal Klein Four Counts in Semi-Extraspecial 2-Groups

**Qi Liu · research preprint and reproducibility companion · v0.1.0**

Manuscript version dated **17 October 2026**. This repository contains the English research preprint, a complete Chinese reading companion, and exact finite verification code. It is a preprint, not a peer-reviewed journal publication.

- [Versioned GitHub release](https://github.com/oNanachii/rp01-extremal-klein-four/releases/tag/v0.1.0) · [source repository](https://github.com/oNanachii/rp01-extremal-klein-four).
- Paper DOI: [10.5281/zenodo.23450418](https://doi.org/10.5281/zenodo.23450418).
- Companion/software DOI: [10.5281/zenodo.23450447](https://doi.org/10.5281/zenodo.23450447).

## Read and download

[English PDF](https://github.com/oNanachii/rp01-extremal-klein-four/releases/download/v0.1.0/RP01_preprint.pdf) · [中文PDF](https://github.com/oNanachii/rp01-extremal-klein-four/releases/download/v0.1.0/RP01_EXPLAINED_ZH.pdf) · [offline HTML](https://github.com/oNanachii/rp01-extremal-klein-four/releases/download/v0.1.0/RP01_EXPLAINED_ZH.html) · [complete reproduction package](https://github.com/oNanachii/rp01-extremal-klein-four/releases/download/v0.1.0/RP01_reproducibility_v0.1.0.zip) · [arXiv source bundle](https://github.com/oNanachii/rp01-extremal-klein-four/releases/download/v0.1.0/RP01_arxiv_source_v0.1.0.tar.gz)

- [English preprint](output/pdf/RP01_preprint.pdf), [editable LaTeX](paper/main.tex), [bibliography](paper/references.bib).
- [完整中文解析PDF](output/pdf/RP01_EXPLAINED_ZH.pdf), [离线HTML](explainer/RP01_EXPLAINED_ZH.html), [可编辑Markdown](explainer/RP01_EXPLAINED_ZH.md); durable chapter sources: [`explainer/chapters/`](explainer/chapters/).
- [Reading and question-answering entry](READING_START.md); [mathematical numbering map](NUMBERING.md).
- [Verification coverage and limitations](repro/README.md); [release notes](RELEASE_NOTES.md).

The HTML includes MathJax 3.2.2 and SVG mathematics data. Its mathematics, contents navigation and search work without a CDN; following external bibliography links needs a network connection. On Mac, open PDF in Preview or HTML in Safari/Chrome. On iPad, use Books/Files for PDF or a browser that executes JavaScript for HTML; a quick-preview viewer may not execute the mathematical renderer. No font source files or TeX installation are bundled.

## Mathematical scope

The groups satisfy `Z(G)=G'=Phi(G)=C2^2`, `dim_F2(G/Z(G))=2n`, and the semi-extraspecial condition. The count `s` includes the identity; `v4` counts actual Klein four subgroups, not conjugacy classes. On the maximum-`s` branch, the paper gives sharp bounds and exact equality conditions. For **even n >= 4**, all lower-equality groups form one strict square-map/group-isomorphism type. This does not classify every odd branch, every intermediate count, or the embeddings of the eight-dimensional core.

Quadratic-map theory, alternating pencils, scalar Walsh duality and Maiorana–McFarland formulas, Arf criteria and hyperbolic normalization are established tools. Fixed-polar refinement selection and compensation exclusion are short applications of those tools. The paper's concrete extremal statement and complete even-parameter classification are the subject; no new general duality theory or absolute priority certification is claimed.

## Exact finite checks

Python 3.10+ and its standard library suffice:

```sh
python3 repro/code/run_checks.py light
python3 repro/code/run_checks.py full
```

`full` adds the bounded census of 65,536 refinements of one fixed eight-dimensional polar. Neither command enumerates all groups of a given order or proves the general-dimensional theorem. Do not use `python -O`: assertions are part of the checks. Outputs include source hashes, timings and timestamps; the latter two need not agree between runs. The shipped full result records its actual earlier execution; see its timestamp and the reproduction guide.

## Build

Read the supplied PDFs/HTML without installing anything. To rebuild, install Python 3.10+, the exact Python requirement below, and a normal TeX distribution providing pdfLaTeX, XeLaTeX, ctex/Fandol, amsmath, natbib, hyperref, cleveref, bookmark and the packages listed in the sources. Tested with TeX Live 2024.

```sh
python3 -m pip install -r requirements-build.txt
python3 build.py paper
python3 build.py explainer
# or: python3 build.py all
python3 assemble_release.py
```

`build.py html` regenerates editable merged explanation sources and the standalone HTML. Edit the eight chapter Markdown files for lasting changes; generated TeX is overwritten on rebuild. The English source is independent; its bibliography is inline for portable compilation, with a matching `.bib` file. The assembler uses an explicit whitelist, generates a nonrecursive SHA-256 manifest and archives, and excludes temporary build files and private history.

## Citation and identifiers

For mathematical results, cite the English preprint; for use of the software, also cite the matching companion version. [CITATION.cff](CITATION.cff) keeps the companion at the root and the paper in `preferred-citation`. The paper and companion have separate archival records; real identifiers are recorded there and in [platform metadata](platform_metadata.json).

> Qi Liu (2026). *Extremal Klein Four Counts in Semi-Extraspecial 2-Groups*. Research preprint, version 0.1.0. https://doi.org/10.5281/zenodo.23450418

> Qi Liu (2026). *RP01 companion: exact finite checks and Chinese explanation for Extremal Klein Four Counts in Semi-Extraspecial 2-Groups*. Version 0.1.0. https://doi.org/10.5281/zenodo.23450447

## Licences and AI use

The original paper and Chinese explanation, including original textual sources, are **CC BY 4.0**. Original verification/build/reader code and original finite-check data are **MIT**. Embedded MathJax retains **Apache-2.0**. See the precise component boundary and complete legal texts in [LICENSE_SCOPE.md](LICENSE_SCOPE.md). Public access is not public-domain dedication.

Generative AI tools, including OpenAI Codex/ChatGPT and the system recorded as Muse Spark 1.3, contributed to mathematical exploration and proof development, computational checks, literature review, and manuscript drafting. Historical deployment versions are not all confirmed. Automated checks are not external human peer review and do not certify the author's completed personal verification.
