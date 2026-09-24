import copy,csv,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('membership',ROOT/'scripts/render_membership.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class MembershipAudit(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.db=json.loads((m.BASE/'STAGE375_DATABASE.json').read_text())
  with (ROOT/'research/01_source_lock/SOURCE_MANIFEST.csv').open() as f:cls.sources={r['source_id'] for r in csv.DictReader(f)}
 def test_snapshot_valid_and_views_fresh(self):
  self.assertEqual(m.validate(self.db,self.sources),[])
  for name,body in m.outputs(self.db).items():self.assertEqual((m.BASE/name).read_text(),body,name)
 def test_missing_locator_rejected_except_unknown(self):
  d=copy.deepcopy(self.db);d['edges'][0]['locator']=' '
  self.assertTrue(any('missing locator' in x for x in m.validate(d,self.sources)))
  d['edges'][0]['status']='UNKNOWN'
  self.assertFalse(any('missing locator' in x for x in m.validate(d,self.sources)))
 def test_explanation_cannot_be_promoted(self):
  d=copy.deepcopy(self.db);next(e for e in d['edges'] if e['edge_kind']=='EXPLANATORY_RESTATEMENT')['status']='SOURCE_PROVED'
  self.assertTrue(any('explanatory edge promoted' in x for x in m.validate(d,self.sources)))
 def test_missing_leaf_class_rejected(self):
  d=copy.deepcopy(self.db);next(n for n in d['nodes'] if n['id']=='U_NATIVE')['leaf_category']=''
  self.assertTrue(any('unclassified terminal leaf' in x for x in m.validate(d,self.sources)))
 def test_proof_cycle_rejected(self):
  d=copy.deepcopy(self.db);e=copy.deepcopy(d['edges'][0]);e.update(edge_id='TEST',from_claim='TH311',to_claim='INITIAL');d['edges'].append(e)
  self.assertTrue(any('proof dependency cycle' in x for x in m.validate(d,self.sources)))
 def test_incomplete_pair_matrix_rejected(self):
  d=copy.deepcopy(self.db);d['tables']['CLAIM_RELATION_MATRIX'].pop()
  self.assertTrue(any('pair matrix' in x for x in m.validate(d,self.sources)))
 def test_open_chain_cannot_be_marked_verified(self):
  d=copy.deepcopy(self.db);d['classification']='VERIFIED_SOURCE_CHAIN'
  self.assertTrue(any('open dependencies' in x for x in m.validate(d,self.sources)))
 def test_dangling_source_and_node_rejected(self):
  d=copy.deepcopy(self.db);d['edges'][0].update(source='NOT_PINNED',to_claim='NOT_A_NODE')
  errors=m.validate(d,self.sources)
  self.assertTrue(any('unknown source' in x for x in errors));self.assertTrue(any('dangling node' in x for x in errors))
if __name__=='__main__':unittest.main()
