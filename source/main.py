from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
from interface_sort_by_price import Ui_Dialog
from getDataThread import getData
import time
import sys

class tableModel(QtWidgets.QDialog):
    def __init__(self, data_list_proc, data_list_gp, data_list_ram):
        super(tableModel, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data_list_proc = data_list_proc
        self.data_list_gp = data_list_gp
        self.data_list_ram = data_list_ram
        self.ui.pushButton.clicked.connect(self.build_table_proc)

    def build_table_proc(self):
        #obj = interface_window()
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(len(self.data_list_proc)) 
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Name"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Price"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Link"))
        print(self.data_list_proc)
        for i in range(len(self.data_list_proc)):
            self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.data_list_proc[i].get("Name")))
            self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.data_list_proc[i].get("Price"))))
            self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.data_list_proc[i].get("Link")))


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
        self.thread = QtCore.QThread()
        self.worker = getData()
        self.worker.request = self.list_get_requests[1]
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run_parsing_proc)
        self.thread.finished.connect(lambda : self.ui.pushButton.setEnabled(True))
        self.worker.finished.connect(self.thread.quit)
        print(self.data_about_proc)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.ui.pushButton.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.splash.close)


    def VideocardParsing(self):
        self.thread_2 = QtCore.QThread()
        self.worker_2 = getData()
        self.worker_2.request = self.list_get_requests[0]
        self.worker_2.moveToThread(self.thread_2)
        self.thread_2.started.connect(self.worker_2.run_parsing_gpu)
        self.thread_2.finished.connect(lambda : self.ui.pushButton_4.setEnabled(True))
        self.worker_2.finished.connect(self.thread_2.quit)
        self.worker_2.finished.connect(self.worker_2.deleteLater)
        self.thread_2.finished.connect(self.thread_2.deleteLater)
        self.thread_2.start()
        self.ui.pushButton_4.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.splash.close)
        

    def Ram_DIMMParsing(self):
        self.thread_3 = QtCore.QThread()
        self.worker_3 = getData()
        self.worker_3.request = self.list_get_requests[2]
        self.worker_3.moveToThread(self.thread_3)
        self.thread_3.started.connect(self.worker_3.run_parsing_ram)
        self.thread_3.finished.connect(lambda : self.ui.pushButton_3.setEnabled(True))
        self.worker_3.finished.connect(self.thread_3.quit)
        self.worker_3.finished.connect(self.worker_3.deleteLater)
        self.thread_3.finished.connect(self.thread_3.deleteLater)
        self.thread_3.start()
        self.ui.pushButton_3.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.splash.close)

    def flashSplash(self):
        self.splash.show()

    def Average_Price(self):
        if not self.table_dialog:
            self.table_dialog = tableModel(self.data_about_proc, self.data_about_gp, self.data_about_ram)
        self.table_dialog.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = interface_window()
    application.show()

    sys.exit(app.exec())        