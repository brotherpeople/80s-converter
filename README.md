# 80s Converter

Pop song -> instrument-separated -> rearranged in 80s style.

## Pipeline

1. **Separation** (`scripts/separate.py`) — splits the input song into 6 stems
   (vocals, drums, bass, guitar, piano, other) using Demucs (`htdemucs_6s`).
   Runs on Python 3.12 (`venv`).
2. **Transcription** (`scripts/transcribe.py`) — converts a melodic/harmonic
   stem (bass/guitar/piano/other) into MIDI using Basic Pitch.
   Requires Python 3.9 (`venv39`) — Basic Pitch's dependencies don't build on
   Python 3.12.
3. **80s rearrangement** (not started) — rule-based transformation of the
   transcribed MIDI into 80s-style instrumentation (synth bass, gated-reverb
   drums, FM/DX7-style pads, minimal-instrument mode).
4. **Re-synthesis & mix** (not started) — render the rearranged MIDI with
   80s-style synth/drum machine sounds and mix with the original vocal stem.
5. **GUI** (not started) — simple interface on top of the pipeline, to be
   tackled after the core pipeline works end-to-end.

## Setup

```
py -3.12 -m venv venv
venv/Scripts/python.exe -m pip install -r requirements-separation.txt

py -3.9 -m venv venv39
venv39/Scripts/python.exe -m pip install -r requirements-transcription.txt
```

## Notes

- Test audio files and generated outputs (`separated/`, `midi_output/`,
  `*.mp3`, `*.wav`, `*.mid`) are intentionally untracked — see `.gitignore`.
