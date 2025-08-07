# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen1eKazRF.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
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
        self.frame.setGeometry(QRect(260, 380, 751, 641))
        self.frame.setStyleSheet(u"    background-color: #D6E8EA;  /* RGB(214, 232, 234) */\n"
"    border-radius: 16px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 661, 601))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/parkinglot/chair.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(200, 200))
        self.pushButton_2.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border-radius: 8px;")
        icon1 = QIcon()
        icon1.addFile(u":/parkinglot/electric-car.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/parkinglot/car (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/parkinglot/small-car (4).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(200, 200))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(770, 10, 841, 261))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(100)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: black;\n"
"")
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1220, 430, 591, 541))
        self.label.setStyleSheet(u"background-image: url(:/parkinglot/park.png);\n"
"    background-repeat: no-repeat;          /* \uc774\ubbf8\uc9c0 \ubc18\ubcf5 \uc548 \ud568 */\n"
"    background-position: center;           /* \uc911\uc559\uc5d0 \ubc30\uce58 */\n"
"    background-origin: content;            /* padding/\uacbd\uacc4 \uc548\ucabd\ubd80\ud130 \uadf8\ub9bc */\n"
"    /* 2) \uc0ac\uc774\uc988 \ub531 \ub9de\ucd94\ub824\uba74 (\uc6d0\ubcf8 \ube44\uc728 \uc720\uc9c0 \uc548 \ud568) */\n"
"    background-attachment: fixed;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 3000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.next_screen)
        self.pushButton_2.clicked.connect(MainWindow.next_screen)
        self.pushButton_3.clicked.connect(MainWindow.next_screen)
        self.pushButton_4.clicked.connect(MainWindow.next_screen)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Parking Type?", None))
        self.label.setText("")
    # retranslateUi

