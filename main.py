import os
from pathlib import Path

OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"

ENTRY_LINE = "My calendar put a 'quick sync' over lunch, then offered to move my sandwich to 3:15."


def entry_directory():
    override = os.environ.get(OUTPUT_ENV)
    return Path(override if override else DEFAULT_OUTPUT_DIR)


def checked_line(text):
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip() or any(ch in text for ch in "\n\r"):
        raise ValueError("entry must be one non-blank line")
    return text


def write_entry():
    target_dir = entry_directory()
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / ENTRY_FILENAME
    destination.write_text(checked_line(ENTRY_LINE) + "\n", encoding="utf-8")
    return destination


if __name__ == "__main__":
    write_entry()
