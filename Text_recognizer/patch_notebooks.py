import json
import os

# 1. Patch pytesseract_testing.ipynb
pytesseract_nb = "pytesseract_testing.ipynb"
if os.path.exists(pytesseract_nb):
    print(f"Patching {pytesseract_nb}...")
    with open(pytesseract_nb, "r", encoding="utf-8") as f:
        nb_data = json.load(f)
    
    for cell in nb_data.get("cells", []):
        if cell.get("cell_type") == "code":
            source = cell.get("source", [])
            # Search for the lines setting tesseract_cmd
            for i, line in enumerate(source):
                if 'tessrect_model_file_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"' in line or 'tessrect_model_file_path = ' in line:
                    # Replace with cross-platform logic
                    source[i] = "import platform\n"
                    # Add subsequent lines
                    source.insert(i+1, "if platform.system() == 'Windows':\n")
                    source.insert(i+2, "    tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'\n")
                    source.insert(i+3, "else:\n")
                    source.insert(i+4, "    tess.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'\n")
                    # Remove the old setting command line (which originally followed)
                    for j in range(i+5, len(source)):
                        if 'tess.pytesseract.tesseract_cmd = ' in source[j]:
                            source.pop(j)
                            break
                    break
    
    with open(pytesseract_nb, "w", encoding="utf-8") as f:
        json.dump(nb_data, f, indent=1)
    print("PyTesseract notebook patched successfully!")

# 2. Patch ocr_testing.ipynb
ocr_nb = "ocr_testing.ipynb"
if os.path.exists(ocr_nb):
    print(f"Patching {ocr_nb}...")
    with open(ocr_nb, "r", encoding="utf-8") as f:
        nb_data = json.load(f)
    
    # We want to add the SSL bypass context to the import cell
    for cell in nb_data.get("cells", []):
        if cell.get("cell_type") == "code":
            source = cell.get("source", [])
            # Find the import cell
            if any("import easyocr" in line for line in source):
                # Add SSL context bypass at the very beginning of this cell
                source.insert(0, "import ssl\n")
                source.insert(1, "ssl._create_default_https_context = ssl._create_unverified_context\n")
                break
                
    with open(ocr_nb, "w", encoding="utf-8") as f:
        json.dump(nb_data, f, indent=1)
    print("EasyOCR notebook patched successfully!")
