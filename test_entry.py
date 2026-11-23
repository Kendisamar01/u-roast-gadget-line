import ast
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from candidates import CANDIDATES, SELECTED_INDEX
from main import DEFAULT_OUTPUT_DIR, ENTRY_TEXT, OUTPUT_ENV, validate_text

REPO_DIR = Path(__file__).resolve().parent
MAIN_FILE = REPO_DIR / "main.py"
FORBIDDEN = ("fuck", "shit", "bitch", "crap", "damn")


class EntryTests(unittest.TestCase):
    def test_output_contract_constants(self):
        self.assertEqual(OUTPUT_ENV, "MAKEFUN_OUTPUT_DIR")
        self.assertEqual(DEFAULT_OUTPUT_DIR, "/output")

    def test_selected_line_matches_top_candidate(self):
        selected = CANDIDATES[SELECTED_INDEX]
        self.assertEqual(ENTRY_TEXT, selected.text)
        self.assertEqual(selected.total, max(c.total for c in CANDIDATES))
        self.assertEqual(sum(c.total == selected.total for c in CANDIDATES), 1)

    def test_candidates_cover_brief(self):
        self.assertGreaterEqual(len(CANDIDATES), 6)
        for candidate in CANDIDATES:
            with self.subTest(text=candidate.text):
                text = validate_text(candidate.text)
                self.assertLessEqual(len(text), 200)
                self.assertTrue(text.strip())
                self.assertIn(candidate.target.lower(), text.lower())
                self.assertFalse(any(word in text.lower() for word in FORBIDDEN))
                self.assertEqual(len(candidate.scores), 5)
                self.assertTrue(all(1 <= score <= 5 for score in candidate.scores))
                self.assertTrue(candidate.note.strip())

    def test_main_uses_stdlib_only(self):
        tree = ast.parse(MAIN_FILE.read_text(encoding="utf-8"))
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                imports.add(node.module.split(".", 1)[0])
        self.assertTrue(imports)
        self.assertTrue(imports.issubset(sys.stdlib_module_names), imports - sys.stdlib_module_names)

    def test_program_writes_exactly_one_utf8_line(self):
        for run in range(2):
            with self.subTest(run=run), tempfile.TemporaryDirectory() as output_dir:
                env = os.environ.copy()
                env[OUTPUT_ENV] = output_dir
                result = subprocess.run(
                    [sys.executable, "-P", "-s", str(MAIN_FILE)],
                    cwd=REPO_DIR,
                    env=env,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                raw = (Path(output_dir) / "entry.txt").read_bytes()
                text = raw.decode("utf-8")
                self.assertEqual(text, ENTRY_TEXT + "\n")
                self.assertEqual(raw.count(b"\n"), 1)
                self.assertNotIn("\r", text)
                self.assertEqual(len(raw.decode("utf-8").rstrip("\n")), len(ENTRY_TEXT))
                self.assertLessEqual(len(ENTRY_TEXT), 200)


if __name__ == "__main__":
    unittest.main()
