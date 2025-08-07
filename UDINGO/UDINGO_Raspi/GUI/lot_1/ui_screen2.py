# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen2BfAzCa.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
from . import resources_rc
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(3000, 2000)
        MainWindow.setStyleSheet(u"background-color: #F3F8FC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 380, 751, 641))
        self.frame.setStyleSheet(u"    background-color: #D6E8EA;  /* RGB(214, 232, 234) */\n"
"    border-radius: 16px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 60, 651, 521))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(65)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(90, 125, 141);\n"
"color: white")
        self.pushButton.setIconSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(90, 125, 141);\n"
"color : white\n"
"\n"
"")
        self.pushButton_3.setIconSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(90, 125, 141);\n"
"color: white\n"
"")
        self.pushButton_4.setIconSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 10, 841, 261))
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(100)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: black;\n"
"")
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1180, 430, 591, 541))
        self.label.setStyleSheet(u"background-image: url(:/parkinglot/park.png);\n"
"    background-repeat: no-repeat;          /* \uc774\ubbf8\uc9c0 \ubc18\ubcf5 \uc548 \ud568 */\n"
"    background-position: center;           /* \uc911\uc559\uc5d0 \ubc30\uce58 */\n"
"    background-origin: content;            /* padding/\uacbd\uacc4 \uc548\ucabd\ubd80\ud130 \uadf8\ub9bc */\n"
"    /* 2) \uc0ac\uc774\uc988 \ub531 \ub9de\ucd94\ub824\uba74 (\uc6d0\ubcf8 \ube44\uc728 \uc720\uc9c0 \uc548 \ud568) */\n"
"    background-attachment: fixed;")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(410, 1560, 160, 86))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.verticalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 3000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.next_screen)
        self.pushButton_4.clicked.connect(MainWindow.next_screen)
        self.pushButton.clicked.connect(MainWindow.next_screen)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrance", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mall", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parking Type?", None))
        self.label.setText("")
    # retranslateUi

