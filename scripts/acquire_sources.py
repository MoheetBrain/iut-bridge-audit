#!/usr/bin/env python3
"""Download the bounded Stage 1–3 corpus; record requests, times and byte hashes.

Acquisition is separate from mathematical verification. Existing recovered files
are not overwritten. Git archives are pinned to commits, not mutable branches.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / 'sources/metadata'


def acquire():
    META.mkdir(parents=True, exist_ok=True)
    requests = []
    old = json.loads((ROOT / 'sources/retrieval.json').read_text())
    old += json.loads((ROOT / 'sources/dependency_retrieval.json').read_text())
    for entry in old:
        url = entry['url']
        if entry['file'] == 'LANA_report_202607.pdf':
            url = url.replace('/pdf/', '/b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676/')
        if entry['file'] == 'LANA_report_202607.tex':
            url = url.replace('/main/', '/293bdd89463473ae13d40834d70fb4b7ba81da1f/')
        requests.append({'url': url, 'path': 'sources/primary/' + entry['file'],
                         'recovered_sha256': entry['sha256']})
    requests += [
        {'url': 'https://arxiv.org/pdf/2004.13228v2',
         'path': 'sources/secondary/Dupuy_Hilado_Initial_Theta_Data_v2.pdf'},
        {'url': 'https://raw.githubusercontent.com/katobungen/LANA_report_202607/293bdd89463473ae13d40834d70fb4b7ba81da1f/LANA.bib',
         'path': 'sources/primary/LANA.bib'},
        {'url': 'https://codeload.github.com/lana-agents/iut/tar.gz/2d8f000457da6447fa4df4bfec7365c1a49b6384',
         'path': 'sources/primary/lana_iut_2d8f000.tar.gz'},
    ]

    def fetch(entry):
        record = dict(entry, retrieved_at_utc=datetime.now(timezone.utc).isoformat())
        try:
            req = urllib.request.Request(entry['url'], headers={'User-Agent': 'IUT-Bridge-Audit/1.0 (source preservation)'})
            try:
                with urllib.request.urlopen(req, timeout=45) as response:
                    data = response.read()
                    record.update(final_url=response.url, http_status=response.status,
                                  content_type=response.headers.get('Content-Type'))
                record['method'] = 'urllib'
            except Exception as exc:
                record['initial_urllib_error'] = str(exc)
                # Independent HTTPS client for the observed SS TLS incompatibility.
                # A temporary download must pass all checks before becoming a source.
                with tempfile.TemporaryDirectory() as tmp:
                    downloaded = Path(tmp) / 'source'
                    command = ['curl', '--fail', '--location', '--max-time', '45',
                               '--silent', '--show-error', '--output', str(downloaded), entry['url']]
                    subprocess.run(command, check=True, capture_output=True)
                    data = downloaded.read_bytes()
                    record['fallback_command'] = command
                    record['method'] = 'curl'
            if entry['path'].endswith('.pdf') and not data.startswith(b'%PDF-'):
                raise ValueError('Response is not a PDF')
            target = ROOT / entry['path']
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != data:
                raise ValueError('Refusing to overwrite an existing different source')
            target.write_bytes(data)
            record.update(bytes=len(data), sha256=sha256(data).hexdigest(), result='ACQUIRED')
            if 'recovered_sha256' in entry:
                record['matches_recovered_version'] = record['sha256'] == entry['recovered_sha256']
        except Exception as exc:
            record.update(result='FAILED', error=str(exc))
        return record

    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, requests))
    log = META / 'ACQUISITION_LOG.json'
    if log.exists():
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        log = META / ('ACQUISITION_LOG_' + timestamp + '.json')
    log.write_text(json.dumps(records, indent=2) + '\n')
    for row in records:
        print(row['result'], row['path'], row.get('sha256', row.get('error')))
    return records


if __name__ == '__main__':
    records = acquire()
    raise SystemExit(0 if all(r['result'] == 'ACQUIRED' for r in records) else 1)
