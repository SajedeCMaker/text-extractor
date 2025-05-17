# OCR Text Extractor with GUI (Tkinter + EasyOCR)

This Python project uses **EasyOCR** to extract text from an image and provides a simple **graphical interface using Tkinter**.

## Features

- Upload an image using a graphical file dialog
- Display detected texts visually on the image
- Show the extracted texts in a scrollable textbox
- Ask the user whether to save the results to a `.txt` file
- Full support for Persian/Arabic texts using `arabic_reshaper` and `bidi`


## How to Run

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the app**:
    ```bash
    python main.py
    ```

## Dependencies

- easyocr
- opencv-python
- pillow
- tkinter (usually included with Python)
- arabic-reshaper
- python-bidi

You can install all of them with:

```bash
pip install easyocr opencv-python pillow arabic-reshaper python-bidi
