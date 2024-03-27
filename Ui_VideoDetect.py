# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoDetect.ui'
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

class Ui_VideoDetect(object):
    def setupUi(self, VideoDetect):
        if not VideoDetect.objectName():
            VideoDetect.setObjectName(u"VideoDetect")
        VideoDetect.resize(763, 503)
        self.gridLayout = QGridLayout(VideoDetect)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbtBack = QPushButton(VideoDetect)
        self.pbtBack.setObjectName(u"pbtBack")
        self.pbtBack.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(15)
        self.pbtBack.setFont(font)

        self.gridLayout.addWidget(self.pbtBack, 0, 0, 1, 1)

        self.pbtSelect = QPushButton(VideoDetect)
        self.pbtSelect.setObjectName(u"pbtSelect")
        self.pbtSelect.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.pbtSelect.setFont(font1)

        self.gridLayout.addWidget(self.pbtSelect, 1, 0, 1, 1)

        self.radwh = QRadioButton(VideoDetect)
        self.radwh.setObjectName(u"radwh")
        font2 = QFont()
        font2.setPointSize(12)
        self.radwh.setFont(font2)
        self.radwh.setChecked(True)

        self.gridLayout.addWidget(self.radwh, 2, 0, 1, 1)

        self.radauto = QRadioButton(VideoDetect)
        self.radauto.setObjectName(u"radauto")
        self.radauto.setFont(font2)

        self.gridLayout.addWidget(self.radauto, 3, 0, 1, 1)

        self.label_2 = QLabel(VideoDetect)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 42))
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.cmbmodel = QComboBox(VideoDetect)
        self.cmbmodel.addItem("")
        self.cmbmodel.addItem("")
        self.cmbmodel.addItem("")
        self.cmbmodel.addItem("")
        self.cmbmodel.setObjectName(u"cmbmodel")
        font3 = QFont()
        font3.setFamilies([u"Microsoft Sans Serif"])
        font3.setPointSize(12)
        self.cmbmodel.setFont(font3)

        self.gridLayout.addWidget(self.cmbmodel, 5, 0, 1, 1)

        self.label_5 = QLabel(VideoDetect)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 42))
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.cmbtimes = QComboBox(VideoDetect)
        self.cmbtimes.addItem("")
        self.cmbtimes.addItem("")
        self.cmbtimes.addItem("")
        self.cmbtimes.addItem("")
        self.cmbtimes.setObjectName(u"cmbtimes")
        self.cmbtimes.setFont(font3)

        self.gridLayout.addWidget(self.cmbtimes, 7, 0, 1, 1)

        self.label_6 = QLabel(VideoDetect)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 42))
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_4 = QLabel(VideoDetect)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.cmbmin = QComboBox(VideoDetect)
        self.cmbmin.addItem("")
        self.cmbmin.addItem("")
        self.cmbmin.addItem("")
        self.cmbmin.addItem("")
        self.cmbmin.setObjectName(u"cmbmin")
        self.cmbmin.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.cmbmin, 10, 0, 1, 1)

        self.label_7 = QLabel(VideoDetect)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.cmbmax = QComboBox(VideoDetect)
        self.cmbmax.addItem("")
        self.cmbmax.addItem("")
        self.cmbmax.addItem("")
        self.cmbmax.setObjectName(u"cmbmax")
        self.cmbmax.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.cmbmax, 12, 0, 1, 1)

        self.splitter_2 = QSplitter(VideoDetect)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setFont(font)
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
        self.pbtRun.setFont(font)
        self.splitter_2.addWidget(self.pbtRun)

        self.gridLayout.addWidget(self.splitter_2, 12, 1, 1, 1)

        self.pbtClose = QPushButton(VideoDetect)
        self.pbtClose.setObjectName(u"pbtClose")
        self.pbtClose.setMinimumSize(QSize(0, 30))
        self.pbtClose.setFont(font1)

        self.gridLayout.addWidget(self.pbtClose, 12, 2, 1, 1)

        self.label = QLabel(VideoDetect)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 0, 1, 12, 2)


        self.retranslateUi(VideoDetect)

        QMetaObject.connectSlotsByName(VideoDetect)
    # setupUi

    def retranslateUi(self, VideoDetect):
        VideoDetect.setWindowTitle(QCoreApplication.translate("VideoDetect", u"\u89c6\u9891\u8bc6\u522b", None))
        self.pbtBack.setText(QCoreApplication.translate("VideoDetect", u"\u8fd4\u56de", None))
        self.pbtSelect.setText(QCoreApplication.translate("VideoDetect", u"\u9009\u62e9\u89c6\u9891", None))
        self.radwh.setText(QCoreApplication.translate("VideoDetect", u"\u56fa\u5b9a\u957f\u5bbd\u6bd4", None))
        self.radauto.setText(QCoreApplication.translate("VideoDetect", u"\u7a97\u53e3\u81ea\u9002\u5e94", None))
        self.label_2.setText(QCoreApplication.translate("VideoDetect", u"\u6a21\u578b\u9009\u62e9:", None))
        self.cmbmodel.setItemText(0, QCoreApplication.translate("VideoDetect", u"\u4eba\u8138", None))
        self.cmbmodel.setItemText(1, QCoreApplication.translate("VideoDetect", u"\u773c\u775b", None))
        self.cmbmodel.setItemText(2, QCoreApplication.translate("VideoDetect", u"\u5de6\u773c", None))
        self.cmbmodel.setItemText(3, QCoreApplication.translate("VideoDetect", u"\u5168\u8eab", None))

        self.label_5.setText(QCoreApplication.translate("VideoDetect", u"\u8bc6\u522b\u6b21\u6570\uff1a", None))
        self.cmbtimes.setItemText(0, QCoreApplication.translate("VideoDetect", u"1", None))
        self.cmbtimes.setItemText(1, QCoreApplication.translate("VideoDetect", u"5", None))
        self.cmbtimes.setItemText(2, QCoreApplication.translate("VideoDetect", u"10", None))
        self.cmbtimes.setItemText(3, QCoreApplication.translate("VideoDetect", u"20", None))

        self.label_6.setText(QCoreApplication.translate("VideoDetect", u"\u76ee\u6807\u8303\u56f4\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("VideoDetect", u"MIN:", None))
        self.cmbmin.setItemText(0, QCoreApplication.translate("VideoDetect", u"\u9ed8\u8ba4", None))
        self.cmbmin.setItemText(1, QCoreApplication.translate("VideoDetect", u"50*50", None))
        self.cmbmin.setItemText(2, QCoreApplication.translate("VideoDetect", u"100*100", None))
        self.cmbmin.setItemText(3, QCoreApplication.translate("VideoDetect", u"200*200", None))

        self.label_7.setText(QCoreApplication.translate("VideoDetect", u"MAX:", None))
        self.cmbmax.setItemText(0, QCoreApplication.translate("VideoDetect", u"\u9ed8\u8ba4", None))
        self.cmbmax.setItemText(1, QCoreApplication.translate("VideoDetect", u"500*500", None))
        self.cmbmax.setItemText(2, QCoreApplication.translate("VideoDetect", u"600*600", None))

        self.label_3.setText(QCoreApplication.translate("VideoDetect", u"\u7f29\u653e\u500d\u7387:", None))
#if QT_CONFIG(tooltip)
        self.slider.setToolTip(QCoreApplication.translate("VideoDetect", u"\u8c03\u6574\u6a21\u578b\u53c2\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.pbtRun.setText(QCoreApplication.translate("VideoDetect", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.pbtClose.setText(QCoreApplication.translate("VideoDetect", u"\u5173\u95ed\u89c6\u9891", None))
        self.label.setText("")
    # retranslateUi

