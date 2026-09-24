#!/usr/bin/env python3
"""Render Stage 3.5 source ledgers; JSON is canonical, CSV is a review view."""
import argparse
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'research/04_closed_loop'
EVIDENCE = {'SOURCE FACT', 'SOURCE CLAIM', 'RECONSTRUCTION', 'INFERENCE', 'OPEN QUESTION'}
EDGE_TYPES = {'literal equality', 'canonical isomorphism', 'noncanonical isomorphism',
              'poly-isomorphism', 'full poly-isomorphism', 'inclusion', 'surjection',
              'functorial reconstruction', 'formal quotient', 'log-link relation', 'other'}
CROSSWALK = {'PROVED_BY_SOURCE', 'SOURCE_CLAIM', 'RECONSTRUCTED', 'PARTIAL', 'NOT_EQUIVALENT', 'UNKNOWN'}

def outputs(db):
    out = {}
    for name, rows in db['tables'].items():
        stream = io.StringIO(newline='')
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
        out[name + '.csv'] = stream.getvalue()
    out['CLOSED_LOOP_GRAPH.json'] = json.dumps(db['graph'], ensure_ascii=False, indent=2) + '\n'
    return out

def validate(db, source_ids):
    errors = []
    all_ids = set()
    for name, rows in db['tables'].items():
        if not rows:
            errors.append(name + ': empty table')
            continue
        fields = set(rows[0])
        for r in rows:
            if set(r) != fields or any(not isinstance(v, str) or not v.strip() for v in r.values()):
                errors.append(name + ': inconsistent/empty/nonstring field')
            if r['id'] in all_ids:
                errors.append('duplicate ID: ' + r['id'])
            all_ids.add(r['id'])
            if r.get('evidence_type') not in EVIDENCE:
                errors.append(r['id'] + ': invalid evidence type')
            if not set(r.get('source_ids', '').split(';')) <= source_ids:
                errors.append(r['id'] + ': unknown source')
            if not r.get('source_locator'):
                errors.append(r['id'] + ': missing locator')
            if name == 'CROSSWALK' and r['status'] not in CROSSWALK:
                errors.append(r['id'] + ': invalid crosswalk status')
            if name == 'CLOSED_LOOP_LEDGER' and r['edge_type'] not in EDGE_TYPES:
                errors.append(r['id'] + ': invalid edge type')
    graph = db['graph']
    nodes = {n['id'] for n in graph['nodes']}
    if len(nodes) != len(graph['nodes']):
        errors.append('duplicate graph node')
    edges = {r['id']: r for r in db['tables']['CLOSED_LOOP_LEDGER']}
    for e in graph['edges']:
        if e['source'] not in nodes or e['target'] not in nodes:
            errors.append('dangling graph edge')
        if e['ledger_id'] not in edges:
            errors.append('edge missing evidence record')
        elif any(e[k] != edges[e['ledger_id']][k] for k in ['source', 'target', 'edge_type']):
            errors.append('graph/ledger mismatch')
    if {e['ledger_id'] for e in graph['edges']} != set(edges):
        errors.append('graph does not cover edge ledger')
    # Cycles are intentional here: unlike the earlier dependency DAG, this graph
    # records an asserted return relation, not an execution dependency.
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    db = json.loads((BASE / 'STAGE35_DATABASE.json').read_text())
    with (ROOT / 'research/01_source_lock/SOURCE_MANIFEST.csv').open() as f:
        sources = {r['source_id'] for r in csv.DictReader(f)}
    errors = validate(db, sources)
    for name, content in outputs(db).items():
        path = BASE / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                errors.append('stale view: ' + name)
        elif not errors:
            path.write_text(content)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f"PASS: {sum(map(len, db['tables'].values()))} Stage 3.5 rows; source IDs, epistemic labels, schemas, graph references and view freshness")

if __name__ == '__main__':
    main()
