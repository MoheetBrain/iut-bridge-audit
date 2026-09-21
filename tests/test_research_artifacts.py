"""Tests of research-data integrity, not mathematical proofs of IUT."""
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import tarfile
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_ledgers import validate, graph_errors
from render_ledgers import render
from build_dependency_graph import build, outputs
from verify_sources import verify
from audit_lana import code_only

class LedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db=json.loads((ROOT/'research/RESEARCH_DATABASE.json').read_text())
        cls.sources={r['source_id'] for r in csv.DictReader(io.StringIO((ROOT/'research/01_source_lock/SOURCE_MANIFEST.csv').read_text()))}
    def broken(self,fn,fragment):
        db=copy.deepcopy(self.db);fn(db)
        errors=validate(db,self.sources)
        self.assertTrue(any(fragment in e for e in errors),errors)
    def test_valid_database(self):self.assertEqual(validate(self.db,self.sources),[])
    def test_missing_source(self):self.broken(lambda d:d['objects'][0].update(source_ids=''),'missing reference')
    def test_unknown_source(self):self.broken(lambda d:d['claims'][0].update(source_id='GHOST'),'unknown reference GHOST')
    def test_missing_locator(self):self.broken(lambda d:d['choices'][0].update(source_location=''),'missing source locator')
    def test_unknown_object(self):self.broken(lambda d:d['choices'][0].update(object_acted_on='O_NONEXISTENT'),'unknown object')
    def test_dangling_map_endpoint(self):self.broken(lambda d:d['maps'][0].update(codomain='dangling'),'unknown reference dangling')
    def test_nonexistent_step(self):self.broken(lambda d:d['choices'][0].update(stage='S99'),'unknown reference S99')
    def test_missing_invariant_status(self):self.broken(lambda d:d['invariants'][0].pop('status'),'missing evidence status')
    def test_missing_claim_status(self):self.broken(lambda d:d['claims'][0].pop('status'),'missing epistemic status')
    def test_invalid_evidence(self):self.broken(lambda d:d['maps'][0].update(evidence_type='PROVED_BY_AI'),'invalid evidence type')
    def test_unknown_invariant(self):self.broken(lambda d:d['orbits'][0].update(invariant_properties='J999'),'unknown reference J999')
    def test_duplicate_id(self):self.broken(lambda d:d['claims'].append(copy.deepcopy(d['claims'][0])),'duplicate ID')
    def test_graph_cycle(self):
        g=build(self.db);g['edges'].append(dict(source='S09',target='S01',relation='bad',status='UNRESOLVED'))
        self.assertIn('graph: cycle',graph_errors(g))
    def test_graph_dangling_endpoint(self):
        g=build(self.db);g['edges'][0]['source']='MISSING'
        self.assertIn('graph: dangling endpoint',graph_errors(g))
    def test_generated_views_current(self):
        for path,text in {**render(self.db),**outputs(self.db)}.items():
            with self.subTest(path=path):self.assertEqual((ROOT/path).read_text(),text)
    def test_comment_string_masking(self):
        source='-- sorry\n/- axiom /- admit -/ sorry -/\ndef x := "sorry \\\" axiom"\ntheorem y : True := by\n  sorry\n'
        masked=code_only(source)
        hits=list(re.finditer(r'\b(sorry|admit|axiom)\b',masked))
        self.assertEqual([x.group() for x in hits],['sorry'])
        self.assertEqual(masked.count('\n'),source.count('\n'))
        self.assertEqual(len(masked),len(source))

class SourceTests(unittest.TestCase):
    def fixture(self,root):
        for p in ['research/01_source_lock','sources/metadata','sources/primary','sources/lana_agents_iut']:(root/p).mkdir(parents=True,exist_ok=True)
        paper=root/'sources/primary/paper.pdf';paper.write_bytes(b'%PDF-test fixture, not a mathematical source')
        row=dict(source_id='TEST',title='Fixture',authors='Fixture',local_path='sources/primary/paper.pdf',sha256=hashlib.sha256(paper.read_bytes()).hexdigest())
        with (root/'research/01_source_lock/SOURCE_MANIFEST.csv').open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(row));w.writeheader();w.writerow(row)
        meta=dict(row,publication_status='fixture',retrieval_date='2026-09-21',bytes=paper.stat().st_size,read_scope='unit fixture')
        (root/'sources/metadata/TEST.json').write_text(json.dumps(meta))
        code=b'def x := 1\n';(root/'sources/lana_agents_iut/Test.lean').write_bytes(code)
        with (root/'sources/metadata/LANA_FILE_MANIFEST.csv').open('w') as f:
            w=csv.DictWriter(f,fieldnames=['path','sha256']);w.writeheader();w.writerow(dict(path='Test.lean',sha256=hashlib.sha256(code).hexdigest()))
        with tarfile.open(root/'sources/primary/lana_iut_2d8f000.tar.gz','w:gz') as tf:
            member=tarfile.TarInfo('snapshot/Test.lean');member.size=len(code);tf.addfile(member,io.BytesIO(code))
        return paper
    def test_valid_source_fixture(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);self.fixture(root);self.assertEqual(verify(root),([],1,1))
    def test_source_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);paper=self.fixture(root);paper.write_bytes(b'%PDF-changed')
            self.assertIn('TEST: SHA256 mismatch',verify(root)[0])
    def test_snapshot_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);self.fixture(root);(root/'sources/lana_agents_iut/Test.lean').write_text('changed')
            self.assertIn('LCODE: snapshot differs from complete file manifest',verify(root)[0])

if __name__=='__main__':unittest.main()
