import cv2
from pyzbar.pyzbar import decode
import webbrowser
import threading
import time

class Qr:
    def __init__(self, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.flag = False
    def f1(self):
        time.sleep(2)
        while not self.flag:
            ret, fm = self.cap.read()
            if not ret:
                break
            decoded_objects = decode(fm)
            for obj in decoded_objects:
                data = obj.data.decode("utf-8")
                if not self.flag:
                    print(f"Code detected: {data}")
                    webbrowser.open(data)
                    self.flag = True
            cv2.imshow('QR Code Scanner', fm)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
def func(video_source=0):
    qrp = Qr(video_source)
    td = threading.Thread(target=qrp.f1)
    td.start()
    td.join()

if __name__ == "__main__":
    func()