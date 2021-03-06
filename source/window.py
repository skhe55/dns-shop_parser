from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 533)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(429, 533))
        MainWindow.setMaximumSize(QtCore.QSize(429, 533))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ViewModeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ViewModeBtn.setGeometry(QtCore.QRect(340, 10, 81, 41))
        self.ViewModeBtn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.ViewModeBtn.setObjectName("ViewModeBtn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 400, 254, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(68, 64))
        self.pushButton.setMaximumSize(QtCore.QSize(68, 64))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 249, 217);\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/proc_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(68, 64))
        self.pushButton_4.setMaximumSize(QtCore.QSize(68, 64))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 249, 217);\n"
"}")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/gpu_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(68, 64))
        self.pushButton_3.setMaximumSize(QtCore.QSize(68, 64))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 249, 217);\n"
"}")
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ram_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 261))
        self.frame.setStyleSheet("background-color: rgb(106, 200, 104);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 260, 431, 261))
        self.frame_2.setStyleSheet("background-color: rgb(199, 200, 188);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame.raise_()
        self.frame_2.raise_()
        self.ViewModeBtn.raise_()
        self.horizontalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DNS PARSER"))
        self.ViewModeBtn.setText(_translate("MainWindow", "View Product"))
