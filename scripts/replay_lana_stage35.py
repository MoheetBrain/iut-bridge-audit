#!/usr/bin/env python3
"""Bounded, exact-toolchain replay in a disposable copy; never edit pinned sources."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/04_closed_loop'
SOURCE = ROOT / 'sources/lana_agents_iut'
WORK = Path(tempfile.mkdtemp(prefix='iut-stage35-lean-'))
shutil.copytree(SOURCE, WORK, dirs_exist_ok=True)
ELAN = str(Path.home() / '.elan/bin/elan')
TOOLCHAIN = SOURCE.joinpath('lean-toolchain').read_text().strip()
record = {'workdir': str(WORK), 'toolchain': TOOLCHAIN,
          'started_at_utc': datetime.now(timezone.utc).isoformat(),
          'snapshot_commit': '2d8f000457da6447fa4df4bfec7365c1a49b6384',
          'commands': [], 'kernel_replay': 'UNKNOWN', 'axiom_closure': 'UNKNOWN'}

def save():
    (OUT / 'LEAN_BUILD_REPLAY.json').write_text(json.dumps(record, indent=2) + '\n')

def run(args, timeout):
    command = [ELAN, 'run', TOOLCHAIN] + args
    entry = {'command': command, 'timeout_seconds': timeout}
    proc = subprocess.Popen(command, cwd=WORK, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
        entry.update(exit_code=proc.returncode, stdout=stdout, stderr=stderr)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            stdout, stderr = proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            stdout, stderr = proc.communicate()
        entry.update(exit_code=proc.returncode, timed_out=True, stdout=stdout, stderr=stderr)
    record['commands'].append(entry)
    save()
    print(json.dumps({'command': command, 'exit_code': entry['exit_code'],
                      'timed_out': entry.get('timed_out', False)}), flush=True)
    return entry['exit_code'] == 0 and not entry.get('timed_out')

save()
run(['lean', '--version'], 30)
built = run(['lake', 'build', 'Iut.Implication.Corollary23', 'Iut.Tripod.Main'], 480)
record['manifest_unchanged'] = (WORK / 'lake-manifest.json').read_bytes() == (SOURCE / 'lake-manifest.json').read_bytes()
record['dependency_revisions'] = []
for package in json.loads((SOURCE / 'lake-manifest.json').read_text())['packages']:
    path = WORK / '.lake/packages' / package['name'].strip('«»')
    result = subprocess.run(['git', '-C', str(path), 'rev-parse', 'HEAD'], capture_output=True, text=True)
    record['dependency_revisions'].append({'name': package['name'], 'expected': package['rev'],
        'actual': result.stdout.strip() if result.returncode == 0 else 'UNAVAILABLE',
        'error': result.stderr.strip() if result.returncode else ''})
exact = record['manifest_unchanged'] and all(p['actual'] == p['expected'] for p in record['dependency_revisions'])
record['all_dependency_revisions_match'] = exact
if built and exact:
    record['kernel_replay'] = 'BUILD_PASSED'
    text = ('import Iut.Implication.Corollary23\nimport Iut.Tripod.Main\n'
            '#print axioms Iut.statementII_of_cor312\n'
            '#print axioms Iut.cor312Variant_implies_abc\n'
            '#print axioms Iut.cor312Variant_implies_abc\'\n'
            '#print axioms Iut.Tripod.abc_of_variant\n')
    (WORK / 'Stage35Axioms.lean').write_text(text)
    (OUT / 'LEAN_AXIOM_COMMANDS.lean.txt').write_text(text)
    if run(['lake', 'env', 'lean', 'Stage35Axioms.lean'], 120):
        record['axiom_closure'] = 'PRINTED_SEE_COMMAND_OUTPUT'
record['finished_at_utc'] = datetime.now(timezone.utc).isoformat()
record['pinned_source_hashes_unchanged'] = all(
    hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256((WORK / p.relative_to(SOURCE)).read_bytes()).digest()
    for p in SOURCE.rglob('*') if p.is_file())
save()
