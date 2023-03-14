#!/usr/bin/env python

import sys
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
 
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
 
files_path = sys.argv[1]

pdf_file = Path(files_path)
output_path = pdf_file.parent.absolute()
text_file = output_path / Path("ocr-parsed.txt")

image_file_list = []
 
def main():

    with TemporaryDirectory() as tempdir:

        pdf_pages = convert_from_path(pdf_file, 500)
        
        for page_enumeration, page in enumerate(pdf_pages, start=1):

            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
 
            page.save(filename, "JPEG")
            image_file_list.append(filename)
  
        with open(text_file, "w") as output_file:

            for image_file in image_file_list:

                text = str(((pytesseract.image_to_string(Image.open(image_file)))))
 
                text = text.replace("-\n", "")
 
                output_file.write(text)
 
if __name__ == "__main__":
    main()
