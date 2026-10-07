"""Step 2: MIDI transcription.

Converts a separated stem (bass/guitar/piano/other) into a MIDI file using
Basic Pitch. Must be run with the Python 3.9 venv (venv39) — Basic Pitch's
dependencies don't build on Python 3.12.

Usage:
    venv39/Scripts/python.exe scripts/transcribe.py separated/htdemucs_6s/<song>/bass.wav [-o midi_output]
"""
import argparse
import os
import subprocess
import sys


def transcribe(input_path: str, output_dir: str = "midi_output") -> None:
    os.makedirs(output_dir, exist_ok=True)
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    basic_pitch_exe = os.path.join(os.path.dirname(sys.executable), "basic-pitch.exe")
    subprocess.run([basic_pitch_exe, output_dir, input_path], check=True, env=env)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("-o", "--output-dir", default="midi_output")
    args = parser.parse_args()
    transcribe(args.input_path, args.output_dir)
