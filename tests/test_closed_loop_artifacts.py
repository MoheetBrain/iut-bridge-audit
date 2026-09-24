"""Provenance and graph consistency tests, not mathematical IUT tests."""
import copy
import csv
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_closed_loop import outputs, validate

class ClosedLoopIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = ROOT / 'research/04_closed_loop'
        cls.db = json.loads((cls.base / 'STAGE35_DATABASE.json').read_text())
        with (ROOT / 'research/01_source_lock/SOURCE_MANIFEST.csv').open() as f:
            cls.sources = {r['source_id'] for r in csv.DictReader(f)}

    def test_evidence_and_generated_views(self):
        self.assertEqual(validate(self.db, self.sources), [])
        for name, text in outputs(self.db).items():
            with self.subTest(name=name):
                self.assertEqual((self.base / name).read_text(), text)

    def test_unknown_source_rejected(self):
        db = copy.deepcopy(self.db)
        db['tables']['CROSSWALK'][0]['source_ids'] = 'INVENTED'
        self.assertTrue(any('unknown source' in e for e in validate(db, self.sources)))

    def test_unsupported_epistemic_promotion_rejected(self):
        db = copy.deepcopy(self.db)
        db['tables']['CLOSED_LOOP_LEDGER'][0]['evidence_type'] = 'PROVED_BY_AUDIT'
        self.assertTrue(any('evidence type' in e for e in validate(db, self.sources)))

    def test_graph_cannot_diverge_from_evidence(self):
        db = copy.deepcopy(self.db)
        db['graph']['edges'][0]['edge_type'] = 'literal equality'
        self.assertTrue(any('mismatch' in e for e in validate(db, self.sources)))

    def test_missing_locator_rejected(self):
        db = copy.deepcopy(self.db)
        db['tables']['Q_PILOT_TRANSPORT'][0]['source_locator'] = ''
        self.assertTrue(any('missing locator' in e for e in validate(db, self.sources)))

    def test_dangling_closed_loop_endpoint_rejected(self):
        db = copy.deepcopy(self.db)
        db['graph']['edges'][0]['target'] = 'INVENTED'
        self.assertTrue(any('dangling' in e for e in validate(db, self.sources)))

if __name__ == '__main__':
    unittest.main()
