# Repository Guidelines

## Project Structure & Module Organization

This repository contains an academic CV and supporting materials.

- `main.tex`: primary LaTeX CV source.
- `refactored_main.tex`: alternate/refactored CV source.
- `CV_Duong*.pdf`, `CN_Duong_v7.pdf`: generated CV/cover-note outputs. Keep only useful final versions.
- `qualifications/`: degree and transcript PDFs; `qualifications/ocr/` stores extracted OCR text.
- `*.md`: research notes, PhD topic analysis, prompts, and planning documents.
- `pdf_to_image.py`: utility for converting a PDF to a JPG preview.
- `%OUTDIR%/`, `*.aux`, `*.log`, `*.fls`, `*.fdb_latexmk`, `*.synctex.gz`: LaTeX build artifacts.

No application source tree or test suite exists. Treat this as a document repository.

## Build, Test, and Development Commands

- `pdflatex main.tex`: build the main CV PDF from LaTeX.
- `pdflatex refactored_main.tex`: build the alternate CV PDF.
- `python -m pip install -r requirements.txt`: install Python utilities used by `pdf_to_image.py`.
- `python pdf_to_image.py CV_Duong_v6.pdf main.jpg`: convert one PDF to a JPG preview.

For clean LaTeX rebuilds, remove stale artifacts before compiling:

```sh
rm -f *.aux *.log *.out *.fls *.fdb_latexmk *.synctex.gz
pdflatex main.tex
```

## Coding Style & Naming Conventions

Use existing LaTeX style in `main.tex`: custom `\resume...` commands, compact spacing, and section blocks. Keep source readable by CV section. Prefer ASCII unless names or cited titles require Unicode.

Name versioned PDFs with clear suffixes, for example `CV_Duong_v7.pdf`. Avoid committing temporary files, duplicate failed exports, or build artifacts unless needed for review.

Python code should stay minimal, use 4-space indentation, and follow standard library naming conventions.

## Testing Guidelines

No automated tests are configured. Validate changes by compiling the edited `.tex` file and opening the generated PDF. Check layout, hyperlinks, line wrapping, section order, and publication references. For `pdf_to_image.py`, run it against a known PDF and confirm the JPG is created.

## Commit & Pull Request Guidelines

Git history currently uses simple upload/delete messages such as `Add files via upload` and `Delete main.tex`. Prefer more specific imperative messages going forward, for example `Update publication list` or `Add transcript OCR text`.

Pull requests should describe the document changed, include before/after PDF screenshots or exported PDFs for visual edits, and note any generated files intentionally included. Link related application, PhD topic, or review context when relevant.

## Security & Configuration Tips

Qualification PDFs contain personal academic records. Do not add new private documents unless they are intended for this repository. Review PDFs and OCR text for personal data before sharing externally.
