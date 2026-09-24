#!/usr/bin/env python3
"""Rebuild the optional lexical index from existing tmp/*.pages.json caches.

Caches are extracted inspection aids, not source authority. Compare generated
normalized hashes to the recorded scope before accepting a changed extraction.
"""
import csv,json,hashlib,re,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
B=ROOT/'research/05_membership_provenance'
anchors={r['object_id']:r for r in json.loads((B/'STAGE375_DATABASE.json').read_text())['tables']['ENGULF_OBJECTS']}
spec=[('IUT3','IUT_III',[(126,130,'O01'),(131,145,'O02'),(153,163,'O03'),(182,184,'O04'),(188,189,'O05'),(190,191,'O06')]),('ELS','Essential_Logical_Structure',[(44,44,'O16'),(139,144,'O07'),(145,147,'O18'),(148,150,'O08'),(151,154,'O09'),(155,155,'O10'),(156,158,'O19'),(159,160,'O11'),(161,164,'O12')]),('FORM','Formalization_2026_04',[(1,5,'O13'),(6,9,'O17'),(10,11,'O13')]),('LANA','LANA_report_202607',[(43,43,'O14'),(44,45,'O20'),(46,49,'O14')]),('ALIEN','Alien_Copies',[(143,146,'O15')])]
terms={'engulf':r'engulf(?:s|ing|ed)?','contain':r'contain(?:s|ed|ing|ment)?','special case':r'specialcase','simultaneously':r'simultaneously','intrinsically associated':r'intrinsicallyassociated','without invalidating':r'withoutinvalidating','projection of Theta-intertwining onto q-intertwining':r'projection'}
rows=[];pagehash=[]
for sid,f,ranges in spec:
 pages=json.load(open(ROOT/'tmp'/(f+'.pages.json')))
 for a,b,anchor in ranges:
  for n in range(a,b+1):
   page=re.sub(r'(?<=\w)[-‐]\n(?=\w)', '', pages[n-1]);norm=re.sub(r'\s+','',unicodedata.normalize('NFKC',page)).replace('\u00ad','').casefold();h=hashlib.sha256(norm.encode()).hexdigest();pagehash.append(dict(source=sid,page=n,normalized_text_sha256=h))
   for term,pat in terms.items():
    for m in re.finditer(pat,norm):
     # All projection uses retained as broad candidate matches, not literal phrase claims.
     r=dict(occurrence_id=f'OCC{len(rows)+1:04}',source=sid,locator=f'PDF p.{n}, normalized character {m.start()+1}',term=term,matched_form=m.group(),anchor_id=anchor,normalized_page_sha256=h,match_scope='Projection candidate; inspect source context' if term.startswith('projection') else 'Lexical stem/phrase; anchor gives passage-level semantics')
     r.update({k:v for k,v in anchors[anchor].items() if k not in {'source','locator','object_id'}});rows.append(r)
with (B/'OCCURRENCE_INDEX.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0],lineterminator='\n');w.writeheader();w.writerows(rows)
(B/'OCCURRENCE_SCOPE.json').write_text(json.dumps(dict(normalization='Dehyphenate word-breaking line ends; Unicode NFKC, remove whitespace and soft hyphens, casefold; one-based character offsets; stem matches include container candidates',source_ranges=spec,pages=pagehash),ensure_ascii=False,indent=2)+'\n')
print('Indexed',len(rows),'occurrences on',len(pagehash),'pages; semantic anchors are passage-level, not separate theorem claims')
