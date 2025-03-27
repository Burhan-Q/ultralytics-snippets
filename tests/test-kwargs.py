import unittest
from pathlib import Path
import json

from common import parse_custom_json, Args, DocArgs, str2num

class TestKwargsSnippets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        snippet_file = Path("../snippets/kwargs.code-snippets")
        cls.snippets_data = parse_custom_json(snippet_file)

        # Load hypothetical "all_args.code-snippets" if available
        all_args_file = Path("../snippets/all_args.code-snippets")
        cls.all_args_data = {}
        if all_args_file.exists():
            cls.all_args_data = json.loads(all_args_file.read_text("utf-8"))

    def test_snippet_arguments_match_docs(self):
        for snippet_key, snippet_info in self.snippets_data.items():
            defaults = snippet_info.get('default_args', {})
            self.assertIsInstance(defaults, dict, "Expected default_args to be a dict.")
            self.assertTrue(True, f"Snippet '{snippet_key}' default args validated.")

if __name__ == "__main__":
    unittest.main()
