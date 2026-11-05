#!/usr/bin/env bash
set -euo pipefail
cd /workspace/drzewo-genealogiczne
# Keep tracked source and dependency files unchanged.
python3 -c 'import fitz, pdfplumber, pypdf, pandas, openpyxl, xlrd; from PIL import Image'
command -v tesseract
mkdir -p /workspace/genealogy-tools/tessdata
for lang in pol deu rus lat; do
  curl --fail --silent --show-error --location --retry 2 "https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/65727574dfcd264acbb0c3e07860e4e9e9b22185/$lang.traineddata" -o "/workspace/genealogy-tools/tessdata/$lang.traineddata.tmp"
  mv "/workspace/genealogy-tools/tessdata/$lang.traineddata.tmp" "/workspace/genealogy-tools/tessdata/$lang.traineddata"
done
tesseract --tessdata-dir /workspace/genealogy-tools/tessdata --list-langs
