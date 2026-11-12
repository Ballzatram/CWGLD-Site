"""Public route, metadata, local-resource and JavaScript regression checks."""
import importlib.util
import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("site_check", ROOT / ".engineering/tools/site_check.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
class SiteContractTests(unittest.TestCase):
    def test_public_routes_resources_and_scripts(self):
        pages = json.loads((ROOT / ".engineering/site-contract.json").read_text())["pages"]
        self.assertTrue(pages)
        self.assertEqual(module.inspect(ROOT, pages), [])
if __name__ == "__main__":
    unittest.main()
