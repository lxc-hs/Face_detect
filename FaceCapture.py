from PySide6.QtWidgets import QApplication,QWidget,QMessageBox
from Ui_FaceCapture import Ui_Form
from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QPixmap,QImage,QIcon
import threading
import cv2 as cv
import os
import unicodedata
import icon_rc

class FaceCapture_wimdow(QWidget,Ui_Form):
    SendValueToMainwindow = Signal()

    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.Camera_isOpened = False
        self.cap = None
        self.frame = None
        self.num = 1
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pbtBack.clicked.connect(self.SendValueToMainwindow.emit)
        self.SendValueToMainwindow.connect(self.BackToMainWindow)
        self.pbtSelect.clicked.connect(self.Camera_Open)
        self.pbtRun.setEnabled(False)
        self.pbtRun.clicked.connect(self.pbtRun_slot)
        self.pbtClose.clicked.connect(self.stopcamera)
        self.setWindowIcon(QIcon(':/images/C:/Users/萝卜土豆/Pictures/Saved Pictures/nw.jpg'))


    #返回按钮逻辑
    def BackToMainWindow(self):
        if self.Camera_isOpened:
            QMessageBox.warning(self,'警告','摄像头未释放，请先关闭摄像头！')
            return
        self.close()
        self.parent.show()

    def Camera_Open(self):
        if self.Camera_isOpened:
            QMessageBox.information(self,'警告','不要重复打开摄像头！')
            return
        self.cap = cv.VideoCapture(0) #如果填0，就调用默认的摄像头，如果数字改变就是调用你外接的摄像头或者其他摄像头
        #打开摄像头后运行按钮才能启动
        if self.cap == None:
            QMessageBox.warning(self,'警告','摄像头打开失败！')
        QMessageBox.information(self,'提示','摄像头已成功打开！')
        self.Camera_isOpened = True
        self.pbtRun.setEnabled(True)
        camera_thread = threading.Thread(target=self.Camera_Runing)
        camera_thread.start()

    #截取按钮槽函数
    def pbtRun_slot(self):
        
        text = self.ledname.text()

        #检测名字是否为空
        if not text.strip():
            QMessageBox.warning(self,'警告','名字不能为空或者空格！')
            return
        # 检查字符串是否只包含字母
        for char in text:
            if not char.isalpha() or unicodedata.name(char).startswith('CJK UNIFIED'):
                QMessageBox.warning(self,'警告','名字只能包含英文字母且不能包含中文！')
                return

        # 检查字符串的长度是否大于10
        if len(text) > 10:
            QMessageBox.warning(self,'警告','名字的长度不能大于10！')
            return
        
        current_path = os.path.dirname(__file__)
        path = os.path.join(current_path,'face_pictures')
        path_name = os.path.join(path,text)
        path_name2 =os.path.join(path_name,text)

        #如果没有face_pictures文件夹就创建face_pictures文件夹
        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.exists(path_name):
            os.makedirs(path_name)
        
        if cv.imwrite(path_name2+str(self.num)+'.jpg', self.frame):#会将path_name的最后一个文件名字变成图片名
            self.labshow.setText(text+str(self.num)+'.jpg'+'保存成功！')
        self.num += 1
    
    #摄像头多线程运行
    def Camera_Runing(self):
        
        while self.Camera_isOpened:
            #read()返回两个值，第一个判断视频是否播放完，True为在播放，Fasle为已播放完
            #第二个值为截取的当前帧，就是一张图片，利用Face_detect_demo()进行处理
            flag,self.frame = self.cap.read()
            self.showcamera(self.frame)
        
            

    #将摄像头画面显示到label中
    def showcamera(self,frame):
        if frame is None:
            return
        h, w, c = frame.shape
        bytes_per_line = 3 * w
        q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_BGR888)#注意是BGR

        pixmap = QPixmap.fromImage(q_image).scaled(self.label.size(), aspectMode=Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

    #停止摄像头并释放
    def stopcamera(self):
        if self.Camera_isOpened == False:
            return
        self.Camera_isOpened = False
        self.cap.release()
        QMessageBox.information(self,'提示','摄像头已关闭')
    

if __name__ == '__main__':
    app = QApplication([])
    window = FaceCapture_wimdow()
    window.show()
    app.exec()