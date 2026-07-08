import os
import platform
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from PIL import Image
import pytesseract as tess
import easyocr

# Configure Tesseract path for macOS/Linux/Windows
if platform.system() == "Windows":
    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    tess.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

images = ["img1.jpeg", "img2.jpeg", "img3.jpeg"]

print("=" * 60)
print("1. RUNNING PYTESSERACT OCR")
print("=" * 60)
for img_name in images:
    if os.path.exists(img_name):
        try:
            img = Image.open(img_name)
            text = tess.image_to_string(img).strip()
            print(f"[{img_name}] PyTesseract Extracted Text:")
            print("-" * 40)
            print(text if text else "(No text found)")
            print("-" * 40)
        except Exception as e:
            print(f"Error processing {img_name} with PyTesseract: {e}")
    else:
        print(f"Image {img_name} not found.")

print("\n" + "=" * 60)
print("2. RUNNING EASYOCR")
print("=" * 60)
try:
    # Initialize reader for Hindi and English
    reader = easyocr.Reader(['hi', 'en'], gpu=False)
    for img_name in images:
        if os.path.exists(img_name):
            try:
                result = reader.readtext(img_name, detail=0)
                extracted_text = " ".join(result).strip()
                print(f"[{img_name}] EasyOCR Extracted Text:")
                print("-" * 40)
                print(extracted_text if extracted_text else "(No text found)")
                print("-" * 40)
            except Exception as e:
                print(f"Error processing {img_name} with EasyOCR: {e}")
        else:
            print(f"Image {img_name} not found.")
except Exception as e:
    print(f"Error initializing EasyOCR: {e}")
