import os
from pathlib import Path

ENTRY_TEXT = "My map app reroutes me around traffic it caused by telling 40,000 drivers to take my street."
OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"


def validate_text(text):
    if not isinstance(text, str):
        raise TypeError("entry text must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry text must not be whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    return text


def write_entry(output_dir=None):
    text = validate_text(ENTRY_TEXT)
    directory = output_dir if output_dir is not None else os.environ.get(OUTPUT_ENV, DEFAULT_OUTPUT_DIR)
    target = Path(directory)
    target.mkdir(parents=True, exist_ok=True)
    path = target / "entry.txt"
    path.write_bytes((text + "\n").encode("utf-8"))
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
