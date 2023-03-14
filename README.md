# python-ocr

### Tool for extracting texts from PDF

Tool made with the objective of extracting texts from PDF files, using [pytesseract]("https://pypi.org/project/pytesseract/") and [pdf2image]("https://pypi.org/project/pdf2image/")

## Get Started

Make sure you have Python and Pip installed on your machine.

1. Clone the repository

        git clone https://github.com/WeversonL/python-ocr.git
        cd python-ocr.git

2. Download dependencies with pip

        pip install -r requirements.txt

3. Run the python file passing a PDF as an argument

        python ./main.py 'test-file.pdf'

4. In the current directory, you will have the file 'ocr-parsed.txt' as output. 

        cat ocr-parsed.txt

⚠️ Still in development

## License

`python-ocr` is released under the [GNU General Public License, Version 2](LICENSE)
    
        Copyright (C) 2022 Weverson Lemos

        This program is free software; you can redistribute it and/or
        modify it under the terms of the GNU General Public License
        as published by the Free Software Foundation; either version 2
        of the License, or (at your option) any later version
