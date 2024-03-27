from PySide6.QtWidgets import QApplication,QWidget,QFileDialog,QMessageBox
from Ui_PictureDetect import Ui_Form
from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QPixmap,QImage,QIcon
import os
import sys
import cv2 as cv
import unicodedata
import icon_rc

class PictureDetect_window(QWidget,Ui_Form):
    #传递信号给主窗口
    SendValueToMainwindow = Signal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.file_name = None
        #radwh_is_checked初始时为选中状态，radauto_is_checked相反
        self.radwh_is_checked = 1
        self.radauto_is_checked = 0

        # 获取可执行文件所在的路径
        if getattr(sys, 'frozen', False):
            current_path = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            current_path = os.path.dirname(os.path.abspath(__file__))

        self.model_path_face = os.path.join(current_path,"models", "haarcascade_frontalface_alt2.xml")
        self.model_path_eye = os.path.join(current_path,"models", "haarcascade_eye.xml")
        self.model_path_lefteye = os.path.join(current_path,"models", "haarcascade_lefteye_2splits.xml")
        self.model_path_fullbody = os.path.join(current_path,"models", "haarcascade_fullbody.xml")

        #默认选择此模型，绝对路径
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
        self.pbtSelect.clicked.connect(self.File_Open)
        self.pbtRun.clicked.connect(self.FaceDetect)
        self.radwh.clicked.connect(self.onRadioButtonClicked)
        self.radauto.clicked.connect(self.onRadioButtonClicked)
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
        self.close()
        self.parent.show()

    #打开图片按钮
    def File_Open(self):
        file_name,_= QFileDialog.getOpenFileName(self,'打开图片','','Images (*.png *.jpg)')
        self.file_name = file_name #将file_name保存到全局变量self.file_name
        if file_name:
            with open(file_name,'r') as file:

                if self.radwh_is_checked == 1:
                    #固定长宽比
                    pixmap = QPixmap(file_name).scaled(self.label.size(), aspectMode=Qt.KeepAspectRatio)
                    self.label.setPixmap(pixmap)
                    self.label.setAlignment(Qt.AlignCenter)

                elif self.radauto_is_checked == 1:
                    #自适应
                    pixmap = QPixmap(file_name)
                    self.label.setPixmap(pixmap)
                    self.label.setScaledContents(True)
                    

    #检测函数
    def FaceDetect(self):
        
        if self.file_name == None:
            QMessageBox.warning(self,"警告","请先导入图片")
            return
        for char in self.file_name:
            if not char.isalpha() or unicodedata.name(char).startswith('CJK UNIFIED'):
                QMessageBox.warning(self,'警告','图片路径和图片名字不能包含中文！')
                return
        #拿到选择的图片
        img = cv.imread(self.file_name)
        #将图片转换成灰度图像
        gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        #加载识别模型
        face_detect = cv.CascadeClassifier(self.face_detecter)
        #进行面部识别
        face = face_detect.detectMultiScale(gray_img,self.slider_value,self.times,0,(self.min,self.min),(self.max,self.max))
        #将识别出的图像框出
        for x,y,w,h, in face:
            cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
        if len(face) == 0:
            QMessageBox.warning(self, "警告", "未识别到{0}".format(self.targget))
            return
        # 将 OpenCV 图像转换为 QPixmap 并显示在 QLabel 中
        h, w, c = img.shape
        bytes_per_line = 3 * w
        q_image = QImage(img.data, w, h, bytes_per_line, QImage.Format_BGR888)#注意是BGR

        pixmap = QPixmap.fromImage(q_image).scaled(self.label.size(), aspectMode=Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

    #RadioButton响应函数
    def onRadioButtonClicked(self):
        if self.radwh.isChecked():
            self.radwh_is_checked = 1
            self.radauto_is_checked = 0
            #首先判断self.file_name是否为空
            if self.file_name != None:
                pixmap = QPixmap(self.file_name).scaled(self.label.size(), aspectMode=Qt.KeepAspectRatio)
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(False)
                self.label.setAlignment(Qt.AlignCenter)
            
        elif self.radauto.isChecked():
            self.radwh_is_checked = 0
            self.radauto_is_checked = 1
            #首先判断self.file_name是否为空
            if self.file_name != None:
                pixmap = QPixmap(self.file_name)
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(True)

    #模型选择
    def CmbmodelIndexChanged(self):
        currentindex = self.cmbmodel.currentText()
        if currentindex == '人脸':
            self.face_detecter = self.model_path_face
            self.targget = currentindex
            self.min = 100
            self.max = 400
            
        elif currentindex == '眼睛':
            self.face_detecter = self.model_path_eye
            self.targget = currentindex
            self.min = 50
            self.max = 100
            
        elif currentindex == '左眼':
            self.face_detecter = self.model_path_lefteye
            self.targget = currentindex
            self.min = 50
            self.max =100
            
        elif currentindex == '全身':
            self.face_detecter = self.model_path_fullbody
            self.targget = currentindex
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
    app = QApplication()
    window = PictureDetect_window()
    window.show()
    app.exec()