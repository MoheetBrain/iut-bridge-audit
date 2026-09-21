#!/usr/bin/env python3
"""Reproducible lexical/import audit, explicitly not Lean kernel verification."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / 'sources/lana_agents_iut'
OUT = ROOT / 'research/02_eta_reconstruction'
COMMIT = '2d8f000457da6447fa4df4bfec7365c1a49b6384'


def code_only(text):
    """Mask strings and nested comments while preserving offsets and line numbers."""
    result = list(text)
    i, depth, quoted = 0, 0, False
    while i < len(text):
        pair = text[i:i+2]
        if depth:
            if pair == '/-':
                result[i:i+2] = '  '; depth += 1; i += 2; continue
            if pair == '-/':
                result[i:i+2] = '  '; depth -= 1; i += 2; continue
            if text[i] != '\n': result[i] = ' '
        elif quoted:
            if text[i] == '\\' and i + 1 < len(text):
                result[i:i+2] = '  '; i += 2; continue
            if text[i] == '"': quoted = False
            if text[i] != '\n': result[i] = ' '
        elif pair == '/-':
            result[i:i+2] = '  '; depth = 1; i += 2; continue
        elif pair == '--':
            end = text.find('\n', i)
            if end < 0: end = len(text)
            result[i:end] = ' ' * (end-i); i = end; continue
        elif text[i] == '"':
            result[i] = ' '; quoted = True
        i += 1
    return ''.join(result)


def write_csv(path, rows, fields):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def audit():
    modules, texts, masked, imports = {}, {}, {}, {}
    inventory, holes, declarations = [], [], []
    for path in sorted(CODE.rglob('*')):
        if not path.is_file(): continue
        rel = str(path.relative_to(CODE))
        inventory.append({'source_id':'LCODE', 'path':rel, 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        if path.suffix != '.lean': continue
        module = '.'.join(path.relative_to(CODE).with_suffix('').parts)
        modules[module] = path
        texts[module] = path.read_text()
        masked[module] = code_only(texts[module])
        imports[module] = re.findall(r'^\s*(?:public\s+|private\s+)?import\s+([\w.]+)', masked[module], re.M)
        for hit in re.finditer(r'\b(sorry|admit|sorryAx|axiom)\b', masked[module]):
            line = masked[module].count('\n',0,hit.start()) + 1
            holes.append({'source_id':'LCODE','path':rel,'line':line,'token':hit.group(), 'commit':COMMIT})

    roots = ['Iut.Cor312.Statement','Iut.Implication.Corollary23',
             'Iut.Concrete.Main','Iut.Concrete.Existence','Iut.Anabelian.Existence',
             'Iut.Tripod.Main']
    closure, external, queue = set(), set(), list(roots)
    while queue:
        module = queue.pop()
        if module in closure: continue
        if module not in modules: external.add(module); continue
        closure.add(module); queue.extend(imports[module])
    decl_pattern = re.compile(r'^\s*(?:(?:noncomputable|private|protected|unsafe|partial|scoped)\s+)*(def|abbrev|theorem|lemma|structure|class|axiom|opaque|instance)\s+([^\s({:\[]+)', re.M)
    interfaces = []
    for module in sorted(closure):
        text, clean = texts[module], masked[module]
        matches = list(decl_pattern.finditer(clean))
        for i, match in enumerate(matches):
            start = match.start(1)
            end = matches[i+1].start(1) if i+1 < len(matches) else len(text)
            first = text.count('\n',0,start)+1
            last = text.count('\n',0,end)+1
            decl = {'source_id':'LCODE','module':module,'path':str(modules[module].relative_to(CODE)),
                    'declaration':match.group(2),'kind':match.group(1),'start_line':first,
                    'end_line_exclusive':last,'commit':COMMIT,
                    'inventory_method':'LEXICAL_DECLARATION_SPAN_NOT_ELABORATED'}
            declarations.append(decl)
            if match.group(1) in ('structure','class'):
                interfaces.append(dict(decl, source_text=text[start:end].rstrip(),
                    boundary_status='REVIEW_TYPE_FIELDS; structure is not automatically an unproved theorem'))
    result = {'source_id':'LCODE','commit':COMMIT,'branch':'main','audit_kind':'LEXICAL_AND_LOCAL_IMPORT_CLOSURE',
              'kernel_replayed':False,'lean_toolchain':(CODE/'lean-toolchain').read_text().strip(),
              'all_lean_files_scanned':len(modules),'tokens':holes,'axiom_keyword_count':sum(x['token']=='axiom' for x in holes),
              'sorry_admit_count':sum(x['token'] in ('sorry','admit','sorryAx') for x in holes),
              'roots':roots,'local_import_closure':sorted(closure),'external_import_boundary':sorted(external),
              'tokens_in_local_closure':[h for h in holes if '.'.join(Path(h['path']).with_suffix('').parts) in closure],
              'external_dependency_pins':json.loads((CODE/'lake-manifest.json').read_text()),
              'claim_limit':'No source-level placeholders in the local closure is not a #print axioms result; imported dependency axioms and kernel success remain UNKNOWN.'}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'LANA_STATIC_AUDIT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    (OUT/'LANA_INTERFACE_INVENTORY.json').write_text(json.dumps(interfaces,indent=2,ensure_ascii=False)+'\n')
    write_csv(OUT/'LANA_DECLARATION_INVENTORY.csv',declarations,list(declarations[0]))
    write_csv(ROOT/'sources/metadata/LANA_FILE_MANIFEST.csv',inventory,['source_id','path','sha256'])
    print(json.dumps({k:result[k] for k in ['all_lean_files_scanned','axiom_keyword_count','sorry_admit_count','tokens_in_local_closure','kernel_replayed']},indent=2))
    print('Local import modules:',len(closure),'declarations:',len(declarations),'record interfaces:',len(interfaces))
    return result


if __name__ == '__main__':
    audit()
