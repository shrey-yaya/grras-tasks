# 🔍 Text Recognizer (OCR Comparison Tool)

A python-based OCR (Optical Character Recognition) utility that demonstrates and compares two popular open-source OCR engines: **PyTesseract** (based on Google's Tesseract-OCR) and **EasyOCR** (deep learning-based OCR supporting Hindi, English, and 80+ other languages).

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Prerequisites & Installation](#-prerequisites--installation)
  - [1. Install System OCR Engine (Tesseract)](#1-install-system-ocr-engine-tesseract)
  - [2. Install Python Dependencies](#2-install-python-dependencies)
- [How to Run the Script](#-how-to-run-the-script)
- [Using Jupyter Notebooks](#-using-jupyter-notebooks)
  - [Notebook Patching Utility](#notebook-patching-utility)

---

## 🎯 Overview
This project serves as a learning playground and a utility to extract text from images:
1. **PyTesseract**: A Python wrapper for Google's Tesseract-OCR. Highly efficient for standard documents and clean text. It operates based on traditional layout analysis and character recognition.
2. **EasyOCR**: A deep learning-based OCR package built using PyTorch. Highly robust with noisy backgrounds, hand-written text, rotated text, and multi-lingual documents (configured here to support both English `en` and Hindi `hi` recognition).

---

## 🏗️ Project Structure
```text
.
├── run_ocr.py                  # Main execution script running both OCR engines
├── patch_notebooks.py          # Helper script to fix paths & SSL context inside Jupyter Notebooks
├── pytesseract_testing.ipynb   # Jupyter Notebook dedicated to testing PyTesseract
├── ocr_testing.ipynb           # Jupyter Notebook dedicated to testing EasyOCR
├── requirements.txt            # Python library dependencies
├── img1.jpeg                   # Sample test image 1
├── img2.jpeg                   # Sample test image 2
├── img3.jpeg                   # Sample test image 3
└── tesseract_downloaded/       # Local folder containing downloaded models (if applicable)
```

---

## 🚀 Prerequisites & Installation

### 1. Install System OCR Engine (Tesseract)
`pytesseract` requires the binary Tesseract-OCR engine to be installed on your operating system.

* **macOS** (using Homebrew):
  ```bash
  brew install tesseract
  ```
  *Note: The script looks for the binary at `/opt/homebrew/bin/tesseract` by default.*

* **Windows**:
  1. Download the installer from the official GitHub/ub-mannheim repository (e.g., [tesseract-ocr-w64-setup](https://github.com/UB-Mannheim/tesseract/wiki)).
  2. Install it in the default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`.
  *Note: The script dynamically switches to this path when running on Windows.*

* **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt-get update
  sudo apt-get install tesseract-ocr -y
  ```

### 2. Install Python Dependencies
Set up your virtual environment and install the required library packages:
```bash
# Create and activate environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

---

## 💻 How to Run the Script
Execute the main script to process the sample images (`img1.jpeg`, `img2.jpeg`, `img3.jpeg`) with both PyTesseract and EasyOCR:
```bash
python run_ocr.py
```
This will print out:
- Text extracted by PyTesseract.
- Text extracted by EasyOCR (using the English and Hindi language models).

---

## 📓 Using Jupyter Notebooks
There are two notebooks for interactive testing:
1. `pytesseract_testing.ipynb`: Step-by-step Tesseract evaluation.
2. `ocr_testing.ipynb`: Step-by-step EasyOCR evaluation.

### Notebook Patching Utility
If you are running the notebooks in a clean environment and encounter certificate errors (common when downloading EasyOCR's PyTorch weights over SSL) or need to set up correct system paths, run the pre-configured patching script:
```bash
python patch_notebooks.py
```
This script modifies the `.ipynb` files to:
- Inject a cross-platform detection context for the `tesseract.exe` location.
- Inject SSL context bypass code (`ssl._create_unverified_context`) to resolve network weight downloading issues.