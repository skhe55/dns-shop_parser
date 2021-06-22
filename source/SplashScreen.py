from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(340, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBar = QtWidgets.QFrame(self.centralwidget)
        self.circularProgressBar.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar.setObjectName("circularProgressBar")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBar)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame {\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(199, 200, 188, 0), stop:0.75     rgba(106, 200, 104, 255));\n"
"}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBar)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius:150px;\n"
"    background-color: rgba(199, 200, 188, 120);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBar)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame {\n"
"    border-radius:135px;\n"
"    background-color: rgb(85, 159, 83);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 195, 185))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("QLabel {\n"
"    background-color: none;\n"
"}")
        self.labelTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("QLabel {\n"
"    background-color: none;\n"
"    margin-left:30px;\n"
"    margin-right:30px;\n"
"}")
        self.labelPercentage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelPercentage.setTextFormat(QtCore.Qt.RichText)
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)
        self.labelCredits_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.labelCredits_2.setFont(font)
        self.labelCredits_2.setStyleSheet("QLabel {\n"
"    border-radius:10px;\n"
"    background-color: rgb(109, 202, 105);\n"
"    margin-left: 30px;\n"
"    margin-right:30px;\n"
"}")
        self.labelCredits_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelCredits_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_2.setObjectName("labelCredits_2")
        self.gridLayout.addWidget(self.labelCredits_2, 2, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("QLabel {\n"
"    color: rgb(120, 223, 116);\n"
"    background-color: none;\n"
"    margin-left:30px;\n"
"    margin-right:30px;\n"
"}")
        self.labelCredits.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelTitle.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600; color:#79e276;\">DNS SHOP</span><span style=\" font-weight:600; color:#6ac868;\"/> PARSER</p></body></html>"))
        self.labelPercentage.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span><span style=\" font-size:48pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelCredits_2.setText(_translate("SplashScreen", "loading..."))
        self.labelCredits.setText(_translate("SplashScreen", "by skhe55"))

