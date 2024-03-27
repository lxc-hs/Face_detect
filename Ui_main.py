# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 300)
        Form.setMinimumSize(QSize(770, 300))
        Form.setMaximumSize(QSize(770, 300))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbtPicture = QPushButton(Form)
        self.pbtPicture.setObjectName(u"pbtPicture")
        self.pbtPicture.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setPointSize(12)
        self.pbtPicture.setFont(font2)

        self.gridLayout.addWidget(self.pbtPicture, 0, 0, 1, 1)

        self.pbtCamera = QPushButton(Form)
        self.pbtCamera.setObjectName(u"pbtCamera")
        self.pbtCamera.setMinimumSize(QSize(0, 60))
        self.pbtCamera.setFont(font2)

        self.gridLayout.addWidget(self.pbtCamera, 0, 1, 1, 1)

        self.pbtVideo = QPushButton(Form)
        self.pbtVideo.setObjectName(u"pbtVideo")
        self.pbtVideo.setMinimumSize(QSize(0, 60))
        self.pbtVideo.setFont(font2)

        self.gridLayout.addWidget(self.pbtVideo, 0, 2, 1, 1)

        self.pbtcapture = QPushButton(Form)
        self.pbtcapture.setObjectName(u"pbtcapture")
        self.pbtcapture.setMinimumSize(QSize(0, 60))
        self.pbtcapture.setFont(font2)

        self.gridLayout.addWidget(self.pbtcapture, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4eba\u8138\u68c0\u6d4b\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u4f7f\u7528\u4eba\u8138\u68c0\u6d4b\u7cfb\u7edf\uff01", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u60f3\u8981\u4f7f\u7528\u7684\u529f\u80fd:", None))
        self.pbtPicture.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u8bc6\u522b", None))
        self.pbtCamera.setText(QCoreApplication.translate("Form", u"\u6444\u50cf\u5934\u8bc6\u522b", None))
        self.pbtVideo.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u8bc6\u522b", None))
        self.pbtcapture.setText(QCoreApplication.translate("Form", u"\u4eba\u8138\u622a\u53d6", None))
    # retranslateUi

