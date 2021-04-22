from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
from interface_sort_by_price import Ui_Dialog
from getDataThread import getDataThreadProc, getDataThreadVideocard, getDataThreadRAM
import time
import sys

class tableModel(QtWidgets.QDialog):
    def __init__(self):
        super(tableModel, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.build_table_proc)

    def build_table_proc(self):
        obj = interface_window()
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(len(obj.data_about_proc)) 
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Name"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Price"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Link"))
        print(obj.data_about_proc)
        for i in range(len(obj.data_about_proc)):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(obj.data_about_proc[i].get("Name")))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(obj.data_about_proc[i].get("Price"))))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(obj.data_about_proc[i].get("Link")))


class interface_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(interface_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.flashSplash)
        self.ui.pushButton.released.connect(self.ProcessorParsing)
        self.ui.pushButton_4.clicked.connect(self.flashSplash)
        self.ui.pushButton_4.released.connect(self.VideocardParsing)
        self.ui.pushButton_3.clicked.connect(self.flashSplash)
        self.ui.pushButton_3.released.connect(self.Ram_DIMMParsing)
        self.ui.SortByPriceBtn.clicked.connect(self.Average_Price)
        self.list_get_requests = [        
            "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/", 
            "https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/",
            "https://www.dns-shop.ru/catalog/17a89a3916404e77/operativnaya-pamyat-dimm/"
        ]
        self.table_dialog = None
        self.data_about_proc = list()
        self.data_about_gp = list()
        self.data_about_ram = list()
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap('C:/Users/Sergey/Desktop/parser/parser/resource/icons8-loading-bar-100.png'))
 
    def ProcessorParsing(self):
        get_thread = getDataThreadProc(self.list_get_requests[1])
        get_thread.start()
        QtCore.QTimer.singleShot(5000, self.splash.close)


    def VideocardParsing(self):
        get_thread = getDataThreadVideocard(self.list_get_requests[0])
        get_thread.start()
        QtCore.QTimer.singleShot(5000, self.splash.close)
        

    def Ram_DIMMParsing(self):
        get_thread = getDataThreadRAM(self.list_get_requests[2])
        get_thread.start()
        QtCore.QTimer.singleShot(5000, self.splash.close)

    def flashSplash(self):
        self.splash.show()

    def Average_Price(self):
        if not self.table_dialog:
            self.table_dialog = tableModel()
        self.table_dialog.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = interface_window()
    application.show()

    sys.exit(app.exec())        