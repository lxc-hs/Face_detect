from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QFont,QIcon
from Ui_main import Ui_Form
from PictureDetect import PictureDetect_window
from CameraDetect import CameraDetect_window
from VideoDetect import VideoDetect_window
from FaceCapture import FaceCapture_wimdow
from qt_material import apply_stylesheet
import icon_rc

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bind()

    def bind(self):
        self.pbtPicture.clicked.connect(self.PictureDetect_slot)
        self.pbtCamera.clicked.connect(self.CameraDetect_slot)
        self.pbtVideo.clicked.connect(self.VideoDetect_slot)
        self.pbtcapture.clicked.connect(self.FaceCapture_slot)
        #self.label_2.setFont(QFont("Microsoft YaHei UI", 16))
        self.setWindowIcon(QIcon(':/images/C:/Users/萝卜土豆/Pictures/Saved Pictures/nw.jpg'))
    
    #图片识别
    def PictureDetect_slot(self):
        self.close()
        self.picwindow = PictureDetect_window(self)
        self.picwindow.show()
        
    #摄像头识别
    def CameraDetect_slot(self):
        self.close()
        self.camwindow = CameraDetect_window(self)
        self.camwindow.show()

    #视频识别
    def VideoDetect_slot(self):
        self.close()
        self.vidwindow = VideoDetect_window(self)
        self.vidwindow.show()
    
    #面部捕获
    def FaceCapture_slot(self):
        self.close()
        self.facwinsow = FaceCapture_wimdow(self)
        self.facwinsow.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    extra = {
    # Button font
    'font_size': '30px',
}
    apply_stylesheet(app,theme='dark_lightgreen.xml',extra=extra)
    #apply_stylesheet(app,theme='dark_lightgreen.xml')
    window.show()
    app.exec()