"""Step 1: source separation.

Splits an input song into 6 stems (vocals, drums, bass, guitar, piano, other)
using Demucs' htdemucs_6s model.

Usage:
    venv/Scripts/python.exe scripts/separate.py path/to/song.mp3 [-o output_dir]
"""
import argparse
import subprocess
import sys


def separate(input_path: str, output_dir: str = "separated") -> None:
    subprocess.run(
        [sys.executable, "-m", "demucs", "-n", "htdemucs_6s", input_path, "-o", output_dir],
        check=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("-o", "--output-dir", default="separated")
    args = parser.parse_args()
    separate(args.input_path, args.output_dir)
