# QR Code Scanner

This Python script captures live video from your camera, detects QR codes, and opens the corresponding links. The script utilizes OpenCV for video capture and Pyzbar for QR code decoding.

## Requirements

Ensure you have the required dependencies installed. You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt 
```

## Usage
Run the script in main pipeline :
 ```bash
 python cli.py
 ```

To integrate the function as a whole use the class Qr and the subsequent function `func()`
to do so.


The script will open your camera feed and display it using opencv.

Point your camera towards a QR code, and the script will detect and open the associated link.

Press 'q' to exit the script forcefully.
Gracefull exit has been coded if qr code is detected.

## GUI ADDON
Simple gui add-on for with tkinter.
use q for graceful exit
