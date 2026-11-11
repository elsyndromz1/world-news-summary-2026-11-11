# World News — Wednesday, 11 November 2026

An original, source-attributed English digest of consequential world events that happened or were first reported on 11 November 2026. The program reads `summary.txt` and writes its exact UTF-8 bytes to `/output/entry.txt`.

## Run locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The entry uses only Python’s standard library, makes no network or model calls, and produces deterministic output.
