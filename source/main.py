from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
from interface_sort_by_price import Ui_Dialog
from getDataThread import getData
from save_func_diff_format import open_data
import time
import sys
import itertools
import os.path

class ViewMode(QtWidgets.QDialog):
    def __init__(self):
        super(ViewMode, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data_proccesors = list()
        self.data_gpu = list()
        self.data_ram = list()
        self._toggle_buttons_()

    def _toggle_buttons_(self):
        dir = os.path.abspath(os.curdir)
        if os.path.exists(dir[:-6] + 'data/' + 'data1Proc.picle') is True and os.path.exists(dir[:-6] + 'data/' + 'data2Proc.picle') is True:
            self.ui.pushButton.clicked.connect(self.build_table_proc)
        else: 
            self.ui.pushButton.setEnabled(False)    
        if os.path.exists(dir[:-6] + 'data/' + 'data1Gpu.picle') is True and os.path.exists(dir[:-6] + 'data/' + 'data2Gpu.picle') is True:
            self.ui.pushButton_2.clicked.connect(self.build_table_gpu)
        else:
            self.ui.pushButton_2.setEnabled(False)
        if os.path.exists(dir[:-6] + 'data/' + 'data1Ram.picle') is True and os.path.exists(dir[:-6] + 'data/' + 'data2Ram.picle') is True:
            self.ui.pushButton_3.clicked.connect(self.build_table_ram)
        else:
            self.ui.pushButton_3.setEnabled(False)    

    def build_table_proc(self):
        dir = os.path.abspath(os.curdir)
        list_frwrd = open_data(dir[:-6] + 'data/' + 'data1Proc.picle')
        list_bck = open_data(dir[:-6] + 'data/' + 'data2Proc.picle')
        list_bck = list(reversed(list_bck))
        self.data_proccesors = list(itertools.chain(list_frwrd, list_bck))
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(self.data_proccesors) + 1) 
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(365)
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Название товара"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Цена товара"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Ссылка на товар"))
        print(len(self.data_proccesors))
        for i in range(len(self.data_proccesors)):
            self.ui.tableWidget.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(self.data_proccesors[i].get("Название товара")))
            self.ui.tableWidget.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(str(self.data_proccesors[i].get("Цена товара"))))
            self.ui.tableWidget.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(self.data_proccesors[i].get("Ссылка на товар")))

    def build_table_gpu(self):
        dir = os.path.abspath(os.curdir)
        list_frwrd = open_data(dir[:-6] + 'data/' + 'data1Gpu.picle')
        list_bck = open_data(dir[:-6] + 'data/' + 'data2Gpu.picle')
        list_bck = list(reversed(list_bck))
        self.data_gpu = list(itertools.chain(list_frwrd, list_bck))
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(self.data_gpu) + 1) 
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(365)
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Название товара"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Цена товара"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Ссылка на товар"))
        print(len(self.data_gpu))
        for i in range(len(self.data_gpu)):
            self.ui.tableWidget.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(self.data_gpu[i].get("Название товара")))
            self.ui.tableWidget.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(str(self.data_gpu[i].get("Цена товара"))))
            self.ui.tableWidget.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(self.data_gpu[i].get("Ссылка на товар")))

    def build_table_ram(self):
        dir = os.path.abspath(os.curdir)
        list_frwrd = open_data(dir[:-6] + 'data/' + 'data1Ram.picle')
        list_bck = open_data(dir[:-6] + 'data/' + 'data2Ram.picle')
        list_bck = list(reversed(list_bck))
        self.data_ram = list(itertools.chain(list_frwrd, list_bck))
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(self.data_ram) + 1) 
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(365)
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Название товара"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Цена товара"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Ссылка на товар"))
        print(len(self.data_ram))
        for i in range(len(self.data_ram)):
            self.ui.tableWidget.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(self.data_ram[i].get("Название товара")))
            self.ui.tableWidget.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(str(self.data_ram[i].get("Цена товара"))))
            self.ui.tableWidget.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(self.data_ram[i].get("Ссылка на товар")))

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
        self.ui.ViewModeBtn.clicked.connect(self.View)
        self.list_get_requests = [        
            "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/", 
            "https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/",
            "https://www.dns-shop.ru/catalog/17a89a3916404e77/operativnaya-pamyat-dimm/"
        ]
        self.ViewMode_ = None
        self.data_about_proc = list()
        self.data_about_gp = list()
        self.data_about_ram = list()
        dir = os.path.abspath(os.curdir)
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap(dir[:-6] + 'resource/icons8-loading-bar-100.png'))
 
    def ProcessorParsing(self):
        #self._toggle_buttons_(False)
        self.thread = QtCore.QThread()
        self.worker = getData()
        self.worker.request = self.list_get_requests[1]
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run_parsing_proc)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(lambda : self.ui.pushButton.setEnabled(True))
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.ui.pushButton.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.splash.close)


    def VideocardParsing(self):
        #self._toggle_buttons_(False)
        self.thread_2 = QtCore.QThread()
        self.worker_2 = getData()
        self.worker_2.request = self.list_get_requests[0]
        self.worker_2.moveToThread(self.thread_2)
        self.thread_2.started.connect(self.worker_2.run_parsing_gpu)
        self.worker_2.finished_1.connect(self.thread_2.quit)
        self.worker_2.finished_1.connect(self.worker_2.deleteLater)
        self.worker_2.finished_1.connect(lambda : self.ui.pushButton_4.setEnabled(True))
        #self.worker_2.finished_1.connect(lambda : self._toggle_buttons_(True))
        self.thread_2.finished.connect(self.thread_2.deleteLater)
        self.thread_2.start()
        self.ui.pushButton_4.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.splash.close)
        

    def Ram_DIMMParsing(self):
        #self._toggle_buttons_(False)
        self.thread_3 = QtCore.QThread()
        self.worker_3 = getData()
        self.worker_3.request = self.list_get_requests[2]
        self.worker_3.moveToThread(self.thread_3)
        self.thread_3.started.connect(self.worker_3.run_parsing_ram)
        self.worker_3.finished_2.connect(self.thread_3.quit)
        self.worker_3.finished_2.connect(self.worker_3.deleteLater) 
        self.worker_3.finished_2.connect(lambda : self.ui.pushButton_3.setEnabled(True))
        self.thread_3.finished.connect(self.thread_3.deleteLater)
        self.thread_3.start()
        self.ui.pushButton_3.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.splash.close)

    def flashSplash(self):
        self.splash.show()

    def View(self):
        self.ViewMode_ = None
        if not self.ViewMode_:
            self.ViewMode_ = ViewMode()
        self.ViewMode_.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = interface_window()
    application.show()

    sys.exit(app.exec())        