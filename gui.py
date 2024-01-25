import cv2
from pyzbar.pyzbar import decode
import webbrowser
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk

class QRCodeScanner:
    def __init__(self, video_source=0):
        self.root = tk.Tk()
        self.root.title("QR Code Scanner")

        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(self.root, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack()

        self.btn_start = tk.Button(self.root, text="Start", width=10, command=self.start_capture)
        self.btn_start.pack(padx=10, pady=10)

        self.btn_stop = tk.Button(self.root, text="Stop", width=10, command=self.stop_capture)
        self.btn_stop.pack(padx=10, pady=10)
        self.btn_stop["state"] = "disabled"

        self.is_capturing = False
        self.qr_code_thread = None

    def start_capture(self):
        self.is_capturing = True
        self.btn_start["state"] = "disabled"
        self.btn_stop["state"] = "normal"
        self.qr_code_thread = Thread(target=self.capture_qr_codes)
        self.qr_code_thread.start()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.update()

    def stop_capture(self):
        self.is_capturing = False
        self.btn_start["state"] = "normal"
        self.btn_stop["state"] = "disabled"
        self.vid.release()

    def capture_qr_codes(self):
        while self.is_capturing:
            ret, frame = self.vid.read()
            if ret:
                decoded_objects = decode(frame)
                for obj in decoded_objects:
                    data = obj.data.decode("utf-8")
                    print(f"QR Code detected: {data}")
                    self.open_link(data)
                self.display_frame(frame)

    def open_link(self, link):
        webbrowser.open(link)

    def display_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.root.update_idletasks()

    def update(self):
        if self.is_capturing:
            ret, frame = self.vid.read()
            if ret:
                self.display_frame(frame)
        self.root.after(10, self.update)

    def on_closing(self):
        if self.is_capturing:
            self.stop_capture()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    qr_code_scanner = QRCodeScanner()
    qr_code_scanner.run()
