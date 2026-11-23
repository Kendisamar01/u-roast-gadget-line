import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/tmp/testout")
ENTRY_FILE = OUTPUT_DIR / "entry.txt"
SCRIPT = ROOT / "main.py"


class EntryFileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ENTRY_FILE.unlink(missing_ok=True)
        env = os.environ.copy()
        env["MAKEFUN_OUTPUT_DIR"] = str(OUTPUT_DIR)
        cls.proc = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        cls.raw = ENTRY_FILE.read_bytes() if ENTRY_FILE.is_file() else b""

    def test_main_runs_without_error(self):
        self.assertEqual(self.proc.returncode, 0, self.proc.stderr)

    def test_output_dir_override_is_honored(self):
        self.assertTrue(ENTRY_FILE.is_file())

    def test_output_is_utf8(self):
        self.raw.decode("utf-8")

    def test_output_has_exactly_one_line(self):
        self.assertTrue(self.raw.endswith(b"\n"))
        self.assertEqual(self.raw.count(b"\n"), 1)
        self.assertNotIn(b"\r", self.raw)

    def test_line_is_nonempty_and_within_limit(self):
        line = self.raw.decode("utf-8").removesuffix("\n")
        self.assertTrue(line.strip())
        self.assertGreaterEqual(len(line), 1)
        self.assertLessEqual(len(line), 200)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(EntryFileTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
    print("PASS")
