import cv2
from pyzbar import pyzbar

from kivymd.app import MDApp
from android.permissions import request_permissions, Permission

request_permissions([
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE
        ])

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
