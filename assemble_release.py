#!/usr/bin/env python3
"""Build explicit-whitelist RP01 archives and a SHA-256 manifest; never uploads.

Copyright (c) 2026 Qi Liu. Original code licensed under MIT.
Archives do not include themselves, private history, temporary files or credentials.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import io
import json
import shutil
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parent
VERSION = '0.1.0'
NAME = 'RP01_reproducibility_v' + VERSION
CHAPTERS = ['01_foundations.md', '02_group_counting.md', '03_walsh_bounds.md', '04_attainment.md',
            '05_core.md', '06_decomposition.md', '07_scope_examples.md', '08_literature_appendices.md']
FILES = ['README.md', 'CITATION.cff', 'RELEASE_NOTES.md', 'READING_START.md', 'NUMBERING.md',
         'LICENSE_SCOPE.md', 'LICENSES/CC-BY-4.0.txt', 'LICENSES/MIT.txt', '.gitignore',
         'platform_metadata.json', 'build.py', 'requirements-build.txt', 'assemble_release.py',
         'paper/main.tex', 'paper/references.bib',
         'explainer/FRONTMATTER.md', 'explainer/RP01_EXPLAINED_ZH.md',
         'explainer/RP01_EXPLAINED_ZH.html', 'explainer/tex/main.tex',
         'explainer/assets/reader.css', 'explainer/assets/reader.js',
         'explainer/assets/tex-svg-full.js', 'explainer/assets/MATHJAX-LICENSE.txt',
         'explainer/assets/THIRD_PARTY_NOTICES.md',
         'output/pdf/RP01_preprint.pdf', 'output/pdf/RP01_EXPLAINED_ZH.pdf',
         'output/RP01_arxiv_source_v0.1.0.tar.gz', 'repro/README.md',
         'repro/code/run_checks.py', 'repro/code/full_core.py',
         'repro/code/cmp_mm.py', 'repro/code/mpg_instances.py',
         'repro/results/checks_light.json', 'repro/results/checks_full.json']
FILES += ['explainer/chapters/' + x for x in CHAPTERS]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def paper_archives():
    """Two-source arXiv bundle plus separately licensed complete paper-source zip."""
    target = ROOT / 'output' / ('RP01_arxiv_source_v' + VERSION + '.tar.gz')
    target.parent.mkdir(exist_ok=True)
    with target.open('wb') as stream:
        with gzip.GzipFile(fileobj=stream, mode='wb', mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode='w') as archive:
                for name in ('main.tex', 'references.bib'):
                    data = (ROOT / 'paper' / name).read_bytes()
                    info = tarfile.TarInfo(name)
                    info.size = len(data)
                    info.mode = 0o644
                    info.uid = info.gid = 0
                    info.uname = info.gname = ''
                    info.mtime = 1792195200  # Manuscript version date, not a publication claim.
                    archive.addfile(info, io.BytesIO(data))
    paper = ROOT / 'output' / ('RP01_paper_source_v' + VERSION + '.zip')
    with zipfile.ZipFile(paper, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in ('paper/main.tex', 'paper/references.bib', 'LICENSES/CC-BY-4.0.txt'):
            put_zip(archive, name, (ROOT / name).read_bytes())
    return target, paper


def put_zip(archive, name, data):
    item = zipfile.ZipInfo(name, date_time=(2026, 10, 17, 0, 0, 0))
    item.compress_type = zipfile.ZIP_DEFLATED
    item.external_attr = 0o644 << 16
    archive.writestr(item, data)


def validate_sources():
    for name in FILES:
        source = ROOT / name
        if source.is_symlink() or not source.is_file():
            raise RuntimeError('Invalid or missing whitelist member: ' + name)
    if len(FILES) != len(set(FILES)):
        raise RuntimeError('Duplicate whitelist member')
    cc = (ROOT / 'LICENSES/CC-BY-4.0.txt').read_text()
    for mark in ('Section 1 -- Definitions.', 'Section 8 -- Interpretation.', 'Creative Commons may be contacted'):
        if mark not in cc:
            raise RuntimeError('CC legal text is incomplete')
    if 'Copyright (c) 2026 Qi Liu' not in (ROOT / 'LICENSES/MIT.txt').read_text():
        raise RuntimeError('Missing original-code copyright notice')
    for name in FILES:
        if Path(name).suffix in ('.md', '.tex', '.cff', '.json', '.py'):
            content = (ROOT / name).read_text()
            if ('/' + 'Users/') in content or ('/' + 'private/var/') in content:
                raise RuntimeError('Local personal path in public file: ' + name)
    for mode in ('light', 'full'):
        record = json.loads((ROOT / 'repro/results' / ('checks_' + mode + '.json')).read_text())
        # Existing full census remains the evidence of its actual recorded execution.
        # Metadata/licence edits do not justify claiming a new full-census run.
        if record.get('status') != 'passed':
            raise RuntimeError('Recorded checks did not pass: ' + mode)
        for name, digest in record.get('source_sha256', {}).items():
            if sha(ROOT / 'repro' / 'code' / name) != digest:
                raise RuntimeError('Check-code hash no longer matches recorded execution: ' + name)


def assemble(stage_only=False):
    paper_archives()
    validate_sources()
    names = list(FILES)
    if (ROOT / 'output/validation.json').is_file():
        names.append('output/validation.json')
    manifest = {name: sha(ROOT / name) for name in names}
    (ROOT / 'MANIFEST_SHA256.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
    if stage_only:
        stage = ROOT / 'release' / NAME
        if stage.exists():
            shutil.rmtree(stage)  # This exact path is generated staging, not research history.
        for name in names + ['MANIFEST_SHA256.json']:
            dest = stage / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dest)
        print(json.dumps({'status': 'staged', 'directory': str(stage), 'files': len(names) + 1}))
        return
    target = ROOT / 'output' / (NAME + '.zip')
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(names + ['MANIFEST_SHA256.json']):
            put_zip(archive, NAME + '/' + name, (ROOT / name).read_bytes())
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(names) + 1
        for name, digest in manifest.items():
            assert hashlib.sha256(archive.read(NAME + '/' + name)).hexdigest() == digest
    print(json.dumps({'status': 'assembled', 'archive': str(target), 'sha256': sha(target),
                      'files': len(names) + 1, 'bytes': target.stat().st_size}))


def check_manifest():
    manifest = json.loads((ROOT / 'MANIFEST_SHA256.json').read_text())
    assert 'MANIFEST_SHA256.json' not in manifest
    for name, digest in manifest.items():
        if sha(ROOT / name) != digest:
            raise RuntimeError('Frozen file changed: ' + name)
    print(json.dumps({'status': 'manifest_verified', 'files': len(manifest)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage-only', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        check_manifest()
    else:
        assemble(args.stage_only)
