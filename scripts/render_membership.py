#!/usr/bin/env python3
"""Validate and render Stage 3.75 evidence. Does not certify mathematical truth."""
import argparse,csv,io,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'research/05_membership_provenance'
KINDS={'DEFINITION','THEOREM_APPLICATION','FUNCTORIALITY','ISOMORPHISM','INCLUSION','SURJECTION','QUOTIENT','NORMALIZATION','ORDER','APPROXIMATION','EXPLANATORY_RESTATEMENT','CLAIMED_IMPLICATION','UNKNOWN'}
LEAVES={'DEFINITION','PREVIOUSLY PROVED THEOREM','PREVIOUSLY PROVED PROPOSITION','PREVIOUSLY PROVED COROLLARY','EXPLICIT CONSTRUCTION','EXPLANATORY RESTATEMENT','TARGET-EQUIVALENT CLAIM','UNRESOLVED DEPENDENCY'}
FIELDS=['edge_id','from_claim','to_claim','source','locator','edge_kind','assumptions','independent_of_target?','status','notes']
STATUSES={'SOURCE_PROVED','SOURCE_ASSERTED','PARTIAL','UNRESOLVED','UNKNOWN','VERIFIED_ELEMENTARY'}
CROSSWALK={'PROVED','SOURCE_CLAIM','PARTIAL','STRONGER_THAN','WEAKER_THAN','DIFFERENTLY_TYPED','UNKNOWN'}

def csv_text(rows):
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows);return s.getvalue()

def acyclic(nodes,edges):
 adjacency={n:[] for n in nodes};degree={n:0 for n in nodes}
 for e in edges:
  if e['from_claim'] not in adjacency or e['to_claim'] not in adjacency:return False
  adjacency[e['from_claim']].append(e['to_claim']);degree[e['to_claim']]+=1
 ready=[n for n in degree if degree[n]==0];seen=0
 while ready:
  a=ready.pop();seen+=1
  for b in adjacency[a]:
   degree[b]-=1
   if degree[b]==0:ready.append(b)
 return seen==len(nodes)

def validate(db,sources):
 errors=[];nodes={n['id']:n for n in db['nodes']};edges=db['edges'];ids=set();incoming=set()
 if len(nodes)!=len(db['nodes']):errors.append('duplicate node')
 for x in edges:
  i=x.get('edge_id','?')
  if set(x)!=set(FIELDS):errors.append(i+': edge schema')
  if i in ids:errors.append(i+': duplicate ID')
  ids.add(i)
  if not x.get('locator','').strip() and x.get('status')!='UNKNOWN':errors.append(i+': missing locator')
  if x.get('edge_kind') not in KINDS:errors.append(i+': edge kind')
  if x.get('status') not in STATUSES:errors.append(i+': status')
  if x.get('independent_of_target?') not in {'YES','NO','UNKNOWN'}:errors.append(i+': independence')
  if not set(x.get('source','').split(';'))<=sources:errors.append(i+': unknown source')
  if x.get('from_claim') not in nodes or x.get('to_claim') not in nodes:errors.append(i+': dangling node')
  incoming.add(x.get('to_claim'))
  if x.get('edge_kind')=='EXPLANATORY_RESTATEMENT' and x.get('status') in {'SOURCE_PROVED','VERIFIED_ELEMENTARY'}:errors.append(i+': explanatory edge promoted to proof')
  if x.get('edge_kind')=='UNKNOWN' and x.get('status') not in {'UNKNOWN','UNRESOLVED'}:errors.append(i+': unknown edge promoted')
 for i,n in nodes.items():
  if not n['source'] in sources or not n['locator'].strip():errors.append(i+': node provenance')
  if n['leaf_category'] and n['leaf_category'] not in LEAVES:errors.append(i+': invalid leaf')
  if i not in incoming and not n['leaf_category']:errors.append(i+': unclassified terminal leaf')
 proof=[e for e in edges if e['edge_kind']!='EXPLANATORY_RESTATEMENT']
 if not acyclic(nodes,proof):errors.append('proof dependency cycle')
 keys={'TH311','CQ3','CQ4','FITW','ENGLF','XI_E','XI_F','COR312'}
 pairs=[(r['from_claim'],r['to_claim']) for r in db['tables']['CLAIM_RELATION_MATRIX']]
 if len(pairs)!=56 or set(pairs)!={(a,b) for a in keys for b in keys if a!=b}:errors.append('incomplete pair matrix')
 for r in db['tables']['DIRECTIONAL_CROSSWALK']:
  if r['status'] not in CROSSWALK:errors.append('crosswalk status')
 # This snapshot must not silently turn open dependencies into a complete proof.
 if any(e['status'] in {'UNRESOLVED','PARTIAL','UNKNOWN'} for e in edges) and db['classification']=='VERIFIED_SOURCE_CHAIN':errors.append('open dependencies with verified-chain status')
 return errors

def graph(db,subset=None):
 ns=db['nodes'];es=db['edges']
 if subset is not None:ns=[n for n in ns if n['id'] in subset];es=[e for e in es if e['from_claim'] in subset and e['to_claim'] in subset]
 return {'semantics':'Support -> claim; incoming support may be joint. Statuses are authoritative. Exposition is not an independent proof dependency.','nodes':ns,'edges':[e for e in es if e['edge_kind']!='EXPLANATORY_RESTATEMENT'],'explanatory_edges':[e for e in es if e['edge_kind']=='EXPLANATORY_RESTATEMENT']}

def outputs(db):
 out={name+'.csv':csv_text(rows) for name,rows in db['tables'].items()}
 out['PROOF_EDGE_LEDGER.csv']=csv_text(db['edges'])
 out['ENGULF_PROVENANCE.csv']=csv_text(db['nodes'])
 frontier={'ENGLF','ENG_PRE'}
 while True:
  extended=frontier|{e['from_claim'] for e in db['edges'] if e['to_claim'] in frontier}
  if extended==frontier:break
  frontier=extended
 out['SOURCE_DEPENDENCY_DAG.json']=json.dumps(graph(db),ensure_ascii=False,indent=2)+'\n'
 out['ENGULF_DEPENDENCY_DAG.json']=json.dumps(graph(db,frontier),ensure_ascii=False,indent=2)+'\n'
 atomic={'NATIVE_Q','Q_GENERATOR','TH311','HULL','UPPER','DET','CQ3','CQ4','CL','ENG_PRE','U_NATIVE','P39','RSS','RSS_LOG','OB9','SQ5','PILOT_RECON','INFIMA','XI_D','XI_E','XI_F','U_DESCENT','ORDER','COR312','IPL','SHE_APT'}
 out['XI_E_XI_F_EDGES.csv']=csv_text([e for e in db['edges'] if e['from_claim'] in atomic and e['to_claim'] in atomic and e['edge_kind']!='EXPLANATORY_RESTATEMENT'])
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
 db=json.loads((BASE/'STAGE375_DATABASE.json').read_text())
 with (ROOT/'research/01_source_lock/SOURCE_MANIFEST.csv').open() as f:sources={r['source_id'] for r in csv.DictReader(f)}
 errors=validate(db,sources)
 anchors={r['object_id'] for r in db['tables']['ENGULF_OBJECTS']}
 with (BASE/'OCCURRENCE_INDEX.csv').open() as f:
  occ=list(csv.DictReader(f))
  for r in occ:
   if r['anchor_id'] not in anchors or not r['locator']:errors.append('occurrence anchor/locator')
   if r['source'] not in sources:errors.append('occurrence source')
 for name,body in outputs(db).items():
  p=BASE/name
  if args.check:
   if not p.exists() or p.read_text()!=body:errors.append('stale view: '+name)
  elif not errors:p.write_text(body)
 if errors:raise SystemExit('\n'.join(errors))
 print(f'PASS: {len(db["nodes"])} nodes, {len(db["edges"])} edges, {len(occ)} lexical occurrences, 56 ordered pairs; locators, source IDs, leaf classes, DAG and generated views')
if __name__=='__main__':main()
