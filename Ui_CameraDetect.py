# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CameraDetect.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLCDNumber,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(764, 496)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cmbtimes = QComboBox(Form)
        self.cmbtimes.addItem("")
        self.cmbtimes.addItem("")
        self.cmbtimes.addItem("")
        self.cmbtimes.addItem("")
        self.cmbtimes.setObjectName(u"cmbtimes")
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(12)
        self.cmbtimes.setFont(font)

        self.gridLayout.addWidget(self.cmbtimes, 7, 0, 1, 1)

        self.cmbmodel = QComboBox(Form)
        self.cmbmodel.addItem("")
        self.cmbmodel.addItem("")
        self.cmbmodel.addItem("")
        self.cmbmodel.addItem("")
        self.cmbmodel.setObjectName(u"cmbmodel")
        self.cmbmodel.setFont(font)

        self.gridLayout.addWidget(self.cmbmodel, 5, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 42))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 42))
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 42))
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.radwh = QRadioButton(Form)
        self.radwh.setObjectName(u"radwh")
        self.radwh.setFont(font1)
        self.radwh.setChecked(True)

        self.gridLayout.addWidget(self.radwh, 2, 0, 1, 1)

        self.cmbmax = QComboBox(Form)
        self.cmbmax.addItem("")
        self.cmbmax.addItem("")
        self.cmbmax.addItem("")
        self.cmbmax.setObjectName(u"cmbmax")
        self.cmbmax.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.cmbmax, 12, 0, 1, 1)

        self.pbtBack = QPushButton(Form)
        self.pbtBack.setObjectName(u"pbtBack")
        self.pbtBack.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(15)
        self.pbtBack.setFont(font2)

        self.gridLayout.addWidget(self.pbtBack, 0, 0, 1, 1)

        self.pbtSelect = QPushButton(Form)
        self.pbtSelect.setObjectName(u"pbtSelect")
        self.pbtSelect.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.pbtSelect.setFont(font3)

        self.gridLayout.addWidget(self.pbtSelect, 1, 0, 1, 1)

        self.radauto = QRadioButton(Form)
        self.radauto.setObjectName(u"radauto")
        self.radauto.setFont(font1)

        self.gridLayout.addWidget(self.radauto, 3, 0, 1, 1)

        self.cmbmin = QComboBox(Form)
        self.cmbmin.addItem("")
        self.cmbmin.addItem("")
        self.cmbmin.addItem("")
        self.cmbmin.addItem("")
        self.cmbmin.setObjectName(u"cmbmin")
        self.cmbmin.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.cmbmin, 10, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_3)
        self.slider = QSlider(self.splitter_2)
        self.slider.setObjectName(u"slider")
        self.slider.setMinimumSize(QSize(150, 10))
        self.slider.setMaximumSize(QSize(150, 16777215))
        self.slider.setMinimum(101)
        self.slider.setMaximum(120)
        self.slider.setSliderPosition(110)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(0)
        self.splitter_2.addWidget(self.slider)
        self.lcdNumber = QLCDNumber(self.splitter_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(120, 0))
        self.lcdNumber.setMaximumSize(QSize(120, 16777215))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.lcdNumber.setFont(font4)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setProperty("intValue", 1)
        self.splitter_2.addWidget(self.lcdNumber)
        self.pbtRun = QPushButton(self.splitter_2)
        self.pbtRun.setObjectName(u"pbtRun")
        self.pbtRun.setFont(font2)
        self.splitter_2.addWidget(self.pbtRun)
        self.pbtClose = QPushButton(self.splitter_2)
        self.pbtClose.setObjectName(u"pbtClose")
        self.pbtClose.setMinimumSize(QSize(0, 30))
        self.pbtClose.setFont(font3)
        self.splitter_2.addWidget(self.pbtClose)

        self.gridLayout.addWidget(self.splitter_2, 12, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 0, 1, 12, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6444\u50cf\u5934\u8bc6\u522b", None))
        self.cmbtimes.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.cmbtimes.setItemText(1, QCoreApplication.translate("Form", u"5", None))
        self.cmbtimes.setItemText(2, QCoreApplication.translate("Form", u"10", None))
        self.cmbtimes.setItemText(3, QCoreApplication.translate("Form", u"20", None))

        self.cmbmodel.setItemText(0, QCoreApplication.translate("Form", u"\u4eba\u8138", None))
        self.cmbmodel.setItemText(1, QCoreApplication.translate("Form", u"\u773c\u775b", None))
        self.cmbmodel.setItemText(2, QCoreApplication.translate("Form", u"\u5de6\u773c", None))
        self.cmbmodel.setItemText(3, QCoreApplication.translate("Form", u"\u5168\u8eab", None))

        self.label_6.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u8303\u56f4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b\u6b21\u6570\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6a21\u578b\u9009\u62e9:", None))
        self.radwh.setText(QCoreApplication.translate("Form", u"\u56fa\u5b9a\u957f\u5bbd\u6bd4", None))
        self.cmbmax.setItemText(0, QCoreApplication.translate("Form", u"\u9ed8\u8ba4", None))
        self.cmbmax.setItemText(1, QCoreApplication.translate("Form", u"500*500", None))
        self.cmbmax.setItemText(2, QCoreApplication.translate("Form", u"600*600", None))

        self.pbtBack.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.pbtSelect.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.radauto.setText(QCoreApplication.translate("Form", u"\u7a97\u53e3\u81ea\u9002\u5e94", None))
        self.cmbmin.setItemText(0, QCoreApplication.translate("Form", u"\u9ed8\u8ba4", None))
        self.cmbmin.setItemText(1, QCoreApplication.translate("Form", u"50*50", None))
        self.cmbmin.setItemText(2, QCoreApplication.translate("Form", u"100*100", None))
        self.cmbmin.setItemText(3, QCoreApplication.translate("Form", u"200*200", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"MIN:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"MAX:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7f29\u653e\u500d\u7387:", None))
#if QT_CONFIG(tooltip)
        self.slider.setToolTip(QCoreApplication.translate("Form", u"\u8c03\u6574\u6a21\u578b\u53c2\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.pbtRun.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.pbtClose.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.label.setText("")
    # retranslateUi

