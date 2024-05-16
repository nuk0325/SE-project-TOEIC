# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'managerAddcGnwdh.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(359, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 1, 360, 60))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.back_button = QPushButton(self.frame_5)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 60, 60))
        self.home_button = QPushButton(self.frame_5)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(300, 0, 60, 60))
        self.textBrowser = QTextBrowser(self.frame_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(60, 0, 240, 60))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 480, 360, 60))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 361, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 60, 360, 110))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 40, 341, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 41, 16))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 61, 16))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 170, 360, 310))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 10, 161, 31))
        self.textEdit_2 = QTextEdit(self.frame_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(80, 50, 271, 31))
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 10, 100, 31))
        self.textEdit_3 = QTextEdit(self.frame_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(80, 90, 271, 91))
        self.textEdit_4 = QTextEdit(self.frame_3)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(80, 190, 271, 111))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 31, 16))
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 31, 16))
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 31, 16))
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 190, 51, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"\ub4a4\ub85c\uac00\uae30", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">\ub2e8\uc5b4 \uad00\ub9ac</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ucde8\uc18c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"unit 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\uc5b4 \ucd94\uac00", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ub2e8\uc5b4\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ub73b\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\uc5b4 \uc911\ubcf5 \ud655\uc778", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc608\ubb38\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694</p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc608\ubb38 \ud574\uc11d\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\uc5b4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ub73b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc608\ubb38", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc608\ubb38 \ud574\uc11d", None))
    # retranslateUi

