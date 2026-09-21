#!/usr/bin/env python3
"""Validate schemas, foreign keys, statuses, citations and generated-view freshness.

The small schema validator implements exactly the keywords used by this project's
schemas (type, required, additionalProperties, enum, minItems). It is not a
replacement for a general JSON Schema implementation or mathematical checking.
"""
import csv
import io
import json
import re
from pathlib import Path
from render_ledgers import TABLES, render, CLAIM_STATUS, INVARIANT_STATUS, EVIDENCE
from build_dependency_graph import build, outputs
ROOT=Path(__file__).resolve().parents[1]
IDS={'claims':'claim_id','objects':'object_id','maps':'map_id','steps':'step_id','choices':'choice_id','indeterminacies':'indeterminacy_id','orbits':'transformation_id','invariants':'invariant_id','questions':'question_id'}
LOCATORS={'claims':'location','objects':'construction_source','orbits':'source'}

def parts(value):return [p.strip() for p in value.split(';') if p.strip()]

def schema_errors(rows,schema,label):
    errors=[]
    if not isinstance(rows,list):return [label+': expected array']
    if len(rows)<schema.get('minItems',0):errors.append(label+': empty array')
    item=schema['items'];props=item['properties']
    for i,row in enumerate(rows):
        at=f'{label}[{i}]'
        if not isinstance(row,dict):errors.append(at+': expected object');continue
        for name in item['required']:
            if name not in row:errors.append(at+': missing '+name)
        for name,val in row.items():
            if name not in props:
                if not item.get('additionalProperties',True):errors.append(at+': unexpected '+name)
                continue
            if not isinstance(val,str):errors.append(at+': expected string '+name)
            if 'enum' in props[name] and val not in props[name]['enum']:errors.append(at+': invalid '+name)
    return errors

def graph_errors(graph):
    errors=[];ids=[n['id'] for n in graph['nodes']];known=set(ids)
    if len(ids)!=len(known):errors.append('graph: duplicate node')
    adj={i:[] for i in known};degree={i:0 for i in known}
    for e in graph['edges']:
        a,b=e['source'],e['target']
        if a not in known or b not in known:errors.append('graph: dangling endpoint');continue
        adj[a].append(b);degree[b]+=1
    todo=[n for n in known if degree[n]==0];seen=0
    while todo:
        n=todo.pop();seen+=1
        for v in adj[n]:
            degree[v]-=1
            if degree[v]==0:todo.append(v)
    if seen!=len(known):errors.append('graph: cycle')
    return errors

def validate(db,source_ids,root=ROOT):
    errors=[];known={}
    for table,idfield in IDS.items():
        rows=db.get(table,[])
        schema=json.loads((root/'schemas'/f'{TABLES[table][1]}.schema.json').read_text())
        errors+=schema_errors(rows,schema,table)
        values=[r.get(idfield,'') for r in rows]
        if '' in values or len(values)!=len(set(values)):errors.append(table+': missing/duplicate ID')
        known[table]=set(values)
    def check_refs(row,field,target,required=True):
        value=row.get(field,'');values=parts(value) if isinstance(value,str) else []
        if required and not values:errors.append(f'{row}: missing reference {field}')
        for value in values:
            if value not in target:errors.append(f'{field}: unknown reference {value}')
    for table,rows in ((k,db[k]) for k in IDS):
        for row in rows:
            check_refs(row,'source_id' if table=='claims' else 'source_ids',source_ids)
            loc=row.get(LOCATORS.get(table,'source_location'),'')
            if not loc.strip():errors.append(table+': missing source locator')
            if row.get('evidence_type') not in EVIDENCE:errors.append(table+': missing/invalid evidence type')
            if table!='claims':check_refs(row,'claim_ids',known['claims'])
            # All object references, including prose notes, must resolve.
            for value in row.values():
                if isinstance(value,str):
                    for oid in re.findall(r'\bO_[A-Z][A-Z_0-9]*\b',value):
                        if oid not in known['objects']:errors.append('unknown object '+oid)
    for r in db['claims']:
        if r.get('status') not in CLAIM_STATUS:errors.append('claim: missing epistemic status')
    for r in db['invariants']:
        if r.get('status') not in INVARIANT_STATUS:errors.append('invariant: missing evidence status')
        for f in ['evidence','scope','limitations']:
            if not r.get(f,'').strip():errors.append('invariant: missing '+f)
    for r in db['maps']:
        for f in ['domain','codomain']:check_refs(r,f,known['objects'])
        for cid in re.findall(r'\bCH\d+\b',r.get('dependence_on_choice','')):
            if cid not in known['choices']:errors.append('map: unknown choice '+cid)
    for r in db['choices']:
        check_refs(r,'stage',known['steps']);check_refs(r,'object_acted_on',known['objects'])
        check_refs(r,'interaction_with_other_choices',known['choices'],False)
    for r in db['steps']:
        for field,table in [('input_objects','objects'),('output_objects','objects'),('choices_introduced','choices'),('dependencies','steps'),('open_question','questions'),('map_ids','maps')]:check_refs(r,field,known[table],field!='dependencies')
    if sorted(r.get('step_number') for r in db['steps'])!=[str(i) for i in range(1,10)]:errors.append('algorithm: exactly nine ordered source steps required')
    for r in db['indeterminacies']:check_refs(r,'object_acted_upon',known['objects'])
    for r in db['orbits']:
        check_refs(r,'origin',known['choices']);check_refs(r,'acts_on',known['objects']);check_refs(r,'invariant_properties',known['invariants'])
    if not errors:errors+=graph_errors(build(db))
    return errors

def main():
    db=json.loads((ROOT/'research/RESEARCH_DATABASE.json').read_text())
    rows=list(csv.DictReader(io.StringIO((ROOT/'research/01_source_lock/SOURCE_MANIFEST.csv').read_text())))
    errors=validate(db,{r['source_id'] for r in rows})
    if not errors:
        for name,text in {**render(db),**outputs(db)}.items():
            f=ROOT/name
            if not f.exists() or f.read_text()!=text:errors.append('generated file stale: '+name)
    if errors:raise SystemExit('\n'.join(errors))
    print('PASS: schemas, evidence labels, source locators, foreign keys, nine steps, DAG and generated views')
if __name__=='__main__':main()
