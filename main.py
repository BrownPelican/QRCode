import cv2
from pyzbar import pyzbar

from kivymd.app import MDApp

class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Barcode-QR-Code-Reader"
        self.theme_cls.primary_palette = "Blue"

    def startCamera(self):
        cap = cv2.VideoCapture(0)

        code_read = True
        while code_read:
            _, frame = cap.read()

            decoded_objects = pyzbar.decode(frame)
            for obj in decoded_objects:
                self.root.ids['code_label'].text = obj.data.decode("utf-8")
                code_read = False

    def quit(self):
        MainApp().stop()

if __name__ == '__main__':
    MainApp().run()
