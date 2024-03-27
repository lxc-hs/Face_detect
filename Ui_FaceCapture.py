# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FaceCapture.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 504)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(108, 30))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(630, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 0, 1, 5, 2)

        self.ledname = QLineEdit(Form)
        self.ledname.setObjectName(u"ledname")
        self.ledname.setMinimumSize(QSize(0, 30))
        self.ledname.setMaximumSize(QSize(108, 16777215))

        self.gridLayout.addWidget(self.ledname, 3, 0, 1, 1)

        self.pbtSelect = QPushButton(Form)
        self.pbtSelect.setObjectName(u"pbtSelect")
        self.pbtSelect.setMinimumSize(QSize(0, 40))
        self.pbtSelect.setMaximumSize(QSize(108, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.pbtSelect.setFont(font1)

        self.gridLayout.addWidget(self.pbtSelect, 1, 0, 1, 1)

        self.pbtRun = QPushButton(Form)
        self.pbtRun.setObjectName(u"pbtRun")
        font2 = QFont()
        font2.setPointSize(15)
        self.pbtRun.setFont(font2)

        self.gridLayout.addWidget(self.pbtRun, 5, 1, 1, 1)

        self.pbtBack = QPushButton(Form)
        self.pbtBack.setObjectName(u"pbtBack")
        self.pbtBack.setMinimumSize(QSize(0, 50))
        self.pbtBack.setMaximumSize(QSize(108, 16777215))
        self.pbtBack.setFont(font2)

        self.gridLayout.addWidget(self.pbtBack, 0, 0, 1, 1)

        self.pbtClose = QPushButton(Form)
        self.pbtClose.setObjectName(u"pbtClose")
        self.pbtClose.setMinimumSize(QSize(0, 30))
        self.pbtClose.setFont(font1)

        self.gridLayout.addWidget(self.pbtClose, 5, 2, 1, 1)

        self.labshow = QLabel(Form)
        self.labshow.setObjectName(u"labshow")

        self.gridLayout.addWidget(self.labshow, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4eba\u8138\u622a\u53d6", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u5148\u8f93\u5165\u59d3\u540d\uff1a", None))
        self.label.setText("")
        self.pbtSelect.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.pbtRun.setText(QCoreApplication.translate("Form", u"\u622a\u53d6", None))
        self.pbtBack.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.pbtClose.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.labshow.setText("")
    # retranslateUi

