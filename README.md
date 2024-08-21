# Inspired by [Visual Cryptography](http://www.datagenetics.com/blog/november32013/index.html)

## Visual Cryptography with Python

This project demonstrates encoding and decoding text using visual cryptography techniques. It utilizes the `Pillow` library for image processing and `pytesseract` for optical character recognition.

``pip install pillow``

``pip install pytesseract``

## Usage:
### Encoding
To encode a string into text and generate two shares, run:

``python encode.py``

This will encode the text and save it as two separate images (shares) that can be combined to reveal the original text.

### Decoding
To decode the text from the shares, run:

``python decode.py``

This will process the shares and extract the encoded text.

## Files:
`encode.py`: Script for encoding a string into visual cryptographic shares.
`decode.py`: Script for decoding text from visual cryptographic shares.