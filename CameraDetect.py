from PySide6.QtWidgets import QApplication,QWidget,QMessageBox
from Ui_CameraDetect import Ui_Form
from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QPixmap,QImage,QIcon
import os
import sys
import threading
import cv2 as cv
import icon_rc

class CameraDetect_window(QWidget,Ui_Form):
    SendValueToMainwindow = Signal()

    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.Camera_isOpened = False
        self.cap = None
        
        # 获取可执行文件所在的路径
        if getattr(sys, 'frozen', False):
            current_path = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            current_path = os.path.dirname(os.path.abspath(__file__))
        self.model_path_face = os.path.join(current_path,"models", "haarcascade_frontalface_alt2.xml")
        self.model_path_eye = os.path.join(current_path,"models", "haarcascade_eye.xml")
        self.model_path_lefteye = os.path.join(current_path,"models", "haarcascade_lefteye_2splits.xml")
        self.model_path_fullbody = os.path.join(current_path,"models", "haarcascade_fullbody.xml")
        
        #默认选择此模型
        self.face_detecter = self.model_path_face
        self.targget = '人脸'
        #检测次数
        self.times = 1 
        #默认目标大小
        self.min = 100
        self.max = 400
        self.slider_value = 1.1
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pbtBack.clicked.connect(self.SendValueToMainwindow.emit)
        self.SendValueToMainwindow.connect(self.BackToMainWindow)
        self.pbtSelect.clicked.connect(self.Camera_Open)
        self.pbtRun.setEnabled(False)
        self.pbtRun.clicked.connect(self.pbtRun_slot)
        self.pbtClose.clicked.connect(self.stopcamera)

        #设置两个radiobutton不可使用
        self.radwh.setEnabled(False)
        self.radauto.setEnabled(False)

        self.cmbmodel.currentIndexChanged.connect(self.CmbmodelIndexChanged)
        self.cmbtimes.currentIndexChanged.connect(self.CmbtimesIndexChanged)
        self.cmbmin.currentIndexChanged.connect(self.CmbminIndexChanged)
        self.cmbmax.currentIndexChanged.connect(self.CmbmaxIndexChanged)
        self.slider.valueChanged.connect(self.LcdNumberChange)
        self.lcdNumber.display(self.slider_value)
        self.lcdNumber.setStyleSheet("color: red;")
        self.setWindowIcon(QIcon(':/images/C:/Users/萝卜土豆/Pictures/Saved Pictures/nw.jpg'))

    #返回按钮逻辑
    def BackToMainWindow(self):
        
        if self.Camera_isOpened:
            QMessageBox.warning(self,'警告','摄像头未释放，请先关闭摄像头！')
            return
        self.close()
        self.parent.show()

    #打开摄像头
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
        

    #开始识别按钮槽函数
    def pbtRun_slot(self):
        camera_thread = threading.Thread(target=self.Camera_Runing)
        camera_thread.start()
        
    #摄像头多线程运行
    def Camera_Runing(self):
        while self.Camera_isOpened:
            #read()返回两个值，第一个判断视频是否播放完，True为在播放，Fasle为已播放完
            #第二个值为截取的当前帧，就是一张图片，利用Face_detect_demo()进行处理
            flag,frame = self.cap.read()
            self.FaceDetect(frame)

    #停止摄像头并释放
    def stopcamera(self):
        self.Camera_isOpened = False
        self.cap.release()
        QMessageBox.information(self,'提示','摄像头已关闭')
        
    #检测函数
    def FaceDetect(self,frame):

        #直接将图像帧frame转换成灰度图像
        gray_img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #加载识别模型
        face_detect = cv.CascadeClassifier(self.face_detecter)
        #进行面部识别
        face = face_detect.detectMultiScale(gray_img,self.slider_value,self.times,0,(self.min,self.min),(self.max,self.max))
        #将识别出的图像框出
        for x,y,w,h, in face:
            cv.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
        # 将 OpenCV 图像转换为 QPixmap 并显示在 QLabel 中
        h, w, c = frame.shape
        bytes_per_line = 3 * w
        q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_BGR888)#注意是BGR

        pixmap = QPixmap.fromImage(q_image).scaled(self.label.size(), aspectMode=Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

    #模型选择
    def CmbmodelIndexChanged(self):
        currentindex = self.cmbmodel.currentText()
        if currentindex == '人脸':
            self.face_detecter = self.model_path_face
            self.min = 100
            self.max = 400
           
        elif currentindex == '眼睛':
            self.face_detecter = self.model_path_eye
            self.min = 50
            self.max = 100
            
        elif currentindex == '左眼':
            self.face_detecter = self.model_path_lefteye
            self.min = 50
            self.max =100
            
        elif currentindex == '全身':
            self.face_detecter = self.model_path_fullbody
            self.min = 300
            self.max = 700
           

     #识别次数选择
    def CmbtimesIndexChanged(self):
        currentindex = self.cmbtimes.currentText()
        if currentindex == '1':
            self.times = int(currentindex)
           
        elif currentindex == '5':
            self.times = int(currentindex)
            
        elif currentindex == '10':
            self.times = int(currentindex)
            
        elif currentindex == '20':
            self.times = int(currentindex)
            

    #目标最小范围
    def CmbminIndexChanged(self):
        currentindex = self.cmbmin.currentText()
        if currentindex == '默认':
            self.min = 100
           
        elif currentindex == '50*50':
            self.min = 50
            
        elif currentindex == '100*100':
            self.min = 100
            
        elif currentindex == '200*200':
            self.min = 200
           

    #目标最大范围
    def CmbmaxIndexChanged(self):
        currentindex = self.cmbmax.currentText()
        if currentindex == '默认':
            self.max = 400
            
        elif currentindex == '500*500':
            self.max = 500
           
        elif currentindex == '600*600':
            self.max = 600
           
        
    #Slider槽函数
    def LcdNumberChange(self,value):
        self.lcdNumber.display(value/100.0)
        self.slider_value = value/100.0
        

if __name__ == '__main__':
    app = QApplication([])
    window = CameraDetect_window(None)
    window.show()
    app.exec()