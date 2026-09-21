#!/usr/bin/env python3
"""Offline byte verification of source pins, metadata and the audited code snapshot."""
import csv
import io
import hashlib
import json
import tarfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST='research/01_source_lock/SOURCE_MANIFEST.csv'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def verify(root=ROOT):
    errors=[]
    rows=list(csv.DictReader(io.StringIO((root/MANIFEST).read_text())))
    ids=set()
    for row in rows:
        sid=row['source_id']
        if sid in ids:errors.append(f'duplicate source {sid}')
        ids.add(sid)
        file=(root/row['local_path']).resolve()
        if not file.is_relative_to(root.resolve()):errors.append(f'{sid}: path escapes repository');continue
        if not file.is_file():errors.append(f'{sid}: missing source');continue
        if digest(file)!=row['sha256']:errors.append(f'{sid}: SHA256 mismatch')
        if file.suffix=='.pdf' and not file.read_bytes().startswith(b'%PDF-'):errors.append(f'{sid}: invalid PDF signature')
        try:meta=json.loads((root/'sources/metadata'/f'{sid}.json').read_text())
        except (OSError,ValueError) as exc:errors.append(f'{sid}: metadata {exc}');continue
        for key,value in row.items():
            if meta.get(key)!=value:errors.append(f'{sid}: metadata mismatch {key}')
        for key in ['authors','publication_status','retrieval_date','bytes','read_scope']:
            if not meta.get(key):errors.append(f'{sid}: missing metadata {key}')
        if meta.get('bytes')!=file.stat().st_size:errors.append(f'{sid}: length mismatch')
    code_manifest=root/'sources/metadata/LANA_FILE_MANIFEST.csv'
    code_rows=list(csv.DictReader(io.StringIO(code_manifest.read_text())))
    code_root=root/'sources/lana_agents_iut'
    expected={r['path']:r['sha256'] for r in code_rows}
    actual={p.relative_to(code_root).as_posix():digest(p) for p in code_root.rglob('*') if p.is_file() and '.git' not in p.relative_to(code_root).parts}
    if actual!=expected:errors.append('LCODE: snapshot differs from complete file manifest')
    with tarfile.open(root/'sources/primary/lana_iut_2d8f000.tar.gz') as tf:
        archive={}
        for member in tf.getmembers():
            if not member.isfile():continue
            rel=Path(member.name).parts[1:]
            if not rel or '..' in rel:errors.append('LCODE: unsafe archive path');continue
            archive['/'.join(rel)]=hashlib.sha256(tf.extractfile(member).read()).hexdigest()
        if archive!=expected:errors.append('LCODE: archive and audited snapshot differ')
    return errors,len(rows),len(code_rows)

if __name__=='__main__':
    errors,n,c=verify()
    if errors:raise SystemExit('\n'.join(errors))
    print(f'PASS: {n} source pins and metadata records; {c} LANA files match pinned archive')
