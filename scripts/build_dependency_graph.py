#!/usr/bin/env python3
"""Generate a specification/dependency DAG, not a proof of the IUT bridge."""
import argparse
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def build(db):
    nodes=[]; edges=[]
    def node(i,label,kind,source_ids,location,status):
        nodes.append(dict(id=i,label=label,kind=kind,source_ids=source_ids,source_location=location,status=status))
    def edge(a,b,relation,status='RECONSTRUCTION'):
        edges.append(dict(source=a,target=b,relation=relation,status=status))
    for r in db['questions']:
        node(r['question_id'],r['title'],'UNRESOLVED_OBLIGATION',r['source_ids'],r['source_location'],'UNRESOLVED')
    for r in db['steps']:
        node(r['step_id'],f"Step {r['step_number']}: {r['operation']}",'ALGORITHM_STEP',r['source_ids'],r['source_location'],'SOURCE_CLAIM_ONLY')
        for dep in filter(None,r['dependencies'].split(';')):edge(dep,r['step_id'],'construction prerequisite')
        for q in filter(None,r['open_question'].split(';')):edge(q,r['step_id'],'unresolved typing or fidelity obligation','UNRESOLVED')
    node('TARGET','Existence of suitable S with eta_q = eta_anab_S','TARGET','LANA','§9.2 equation (9-1), PDF p.46','UNRESOLVED')
    edge('S09','TARGET','map construction needed before stating existence target','UNRESOLVED')
    node('IUT311','Theorem 3.11 with source structures and indeterminacies','SOURCE_THEOREM','IUT3','pp.153–158','SOURCE_CLAIM_ONLY')
    node('BRIDGE','Source-faithful bridge and LANA/Lean correspondence','UNRESOLVED_BRIDGE','IUT3;LANA;LCODE','IUT3 xi-d–f pp.183–184; LANA §9.2; Iut/Cor312/Statement.lean:43–52','UNRESOLVED')
    node('VARIANT','Iut.Corollary312Variant X := X.qPilot.lhs ≤ X.rhsData.rhs','PROP_DEFINITION','LCODE','Iut/Cor312/Statement.lean:89–91 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    node('H312','h312: forall X, P X -> Corollary312Variant X','EXPLICIT_HYPOTHESIS','LCODE','Iut/Implication/Corollary23.lean:119–125 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    node('PACKAGES','ProofPackage; Corollary22Inputs; ThetaDataExistence; prime bounds','EXPLICIT_HYPOTHESES','LCODE','Iut/Implication/Corollary23.lean:119–125 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    node('C22','Corollary22Inputs.c2: conditional numerical bound','SOURCE_CODE_THEOREM','LCODE','Iut/Implication/Corollary22.lean:384 onward @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    node('STMTII','statementII_of_cor312','SOURCE_CODE_THEOREM','LCODE','Iut/Implication/Corollary23.lean:56–112 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    node('ABC','Conditional theorem cor312Variant_implies_abc','SOURCE_CODE_THEOREM','LCODE','Iut/Implication/Corollary23.lean:119–125 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    edge('IUT311','BRIDGE','correspondence/derivation not reconstructed','UNRESOLVED')
    edge('TARGET','BRIDGE','LANA asserted relevance; no formal equivalence certified','UNRESOLVED')
    edge('U09','BRIDGE','native-q and formal-quotient obligation','UNRESOLVED')
    edge('BRIDGE','VARIANT','missing source-faithfulness derivation; NOT a proved implication','UNRESOLVED')
    edge('VARIANT','H312','proposition occurring in hypothesis, NOT a proof')
    edge('H312','C22','explicit bridge hypothesis required')
    edge('PACKAGES','C22','additional explicit packages required')
    edge('C22','STMTII','conditional source-code use')
    edge('STMTII','ABC','statementII_implies_statementI with ProofPackage')
    edge('PACKAGES','ABC','additional explicit hypotheses')
    edge('U10','ABC','kernel and imported-axiom certification outstanding','UNRESOLVED')
    node('TRIPOD_INPUTS','Pi1; Tp; residual cyclic bound hcyc; concrete h312','EXPLICIT_HYPOTHESES','LCODE','Iut/Tripod/Main.lean:78–79,125–143 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    node('TRIPOD','Iut.Tripod.abc_of_variant: tripodTheory.StatementII','SOURCE_CODE_THEOREM','LCODE','Iut/Tripod/Main.lean:125–143 @ 2d8f000457da6447fa4df4bfec7365c1a49b6384','VERIFIED_PRIMARY')
    edge('STMTII','TRIPOD','conditional source-code use with constructed concrete inputs')
    edge('TRIPOD_INPUTS','TRIPOD','explicit remaining hypotheses')
    edge('U10','TRIPOD','kernel and imported-axiom certification outstanding','UNRESOLVED')
    return {'schema_version':1,'kind':'SPECIFICATION_DEPENDENCY_DAG_NOT_PROOF_GRAPH','nodes':nodes,'edges':edges}


def markdown(g):
    lines=['# Dependency DAG','', '**RECONSTRUCTION:** Edges distinguish construction dependencies, explicit code hypotheses and unresolved correspondences. No path proves TARGET ★. Acyclicity describes this audit workflow; it is not a claim that the actual log-theta lattice is acyclic. Full lexical import/declaration data are in the LANA audit inventories.','', '```mermaid','flowchart TD']
    for n in g['nodes']:
        label=n['id']+': '+n['label']
        label=label.replace('"',"'").replace('≤','&le;')
        lines.append(f'  {n["id"]}["{label}"]')
    for e in g['edges']:
        arrow='-.->' if e['status']=='UNRESOLVED' else '-->'
        lines.append(f'  {e["source"]} {arrow} {e["target"]}')
    lines+=['```','','## Edge semantics','']
    for e in g['edges']:lines.append(f'- {e["source"]} → {e["target"]}: {e["relation"]} [{e["status"]}].')
    lines+=['','## Node provenance','']
    for n in g['nodes']:lines.append(f'- {n["id"]}: {n["source_ids"]}, {n["source_location"]} [{n["status"]}].')
    return '\n'.join(lines)+'\n'


def outputs(db):
    graph=build(db)
    return {'research/02_eta_reconstruction/DEPENDENCY_DAG.json':json.dumps(graph,ensure_ascii=False,indent=2)+'\n','research/02_eta_reconstruction/DEPENDENCY_DAG.md':markdown(graph)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args()
    for path,content in outputs(json.loads((ROOT/'research/RESEARCH_DATABASE.json').read_text())).items():
        f=ROOT/path
        if args.check:
            if not f.exists() or f.read_text()!=content:raise SystemExit('STALE: '+path)
        else:f.write_text(content)
    print('Dependency graph '+('checked' if args.check else 'generated'))
if __name__=='__main__':main()
