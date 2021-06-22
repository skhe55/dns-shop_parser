from os import name
from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
from interface_sort_by_price import Ui_Dialog
from getDataThread import getData
from save_func_diff_format import open_data, upload_to_csv_file, upload_to_json_file, upload_to_xlsx_file, upload_to_db_file
from dns_shop_pars import DnsShopParser
import time
import sys
import itertools
import os.path
from SplashScreen import Ui_SplashScreen

counter = 0
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.progressBarValue(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress (self):
        global counter
        value = counter
        htmlText = """<html><head/><body><p><span style=" font-size:48pt;">{VALUE}</span><span style=" font-size:48pt; vertical-align:super;">%</span></p></body></html>"""
        newHtml = htmlText.replace("{VALUE}", str(value))
        self.ui.labelPercentage.setText(newHtml)

        if value >= 100: value = 1.000
        self.progressBarValue(value)

        if counter > 100:
            self.timer.stop()
            self.main = interface_window()
            self.main.show()
            self.close()
        counter += 1

    def progressBarValue(self, value):
        styleSheet = """
        QFrame{
        	border-radius: 150px;
	        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(199, 200, 188, 0), stop:{STOP_2} rgba(106, 200, 104, 255));
        }
        """
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgress.setStyleSheet(newStylesheet)

class ViewMode(QtWidgets.QDialog):
    def __init__(self):
        super(ViewMode, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data_proccesors = list()
        self.data_gpu = list()
        self.data_ram = list()
        self._toggle_buttons_()
        self.ui.push_csv.clicked.connect(lambda checked, nameFormatFile = 'csv': self.PushingDataInFile(nameFormatFile))
        self.ui.push_json.clicked.connect(lambda checked, nameFormatFile = 'json': self.PushingDataInFile(nameFormatFile))
        self.ui.push_xlsx.clicked.connect(lambda checked, nameFormatFile = 'xlsx': self.PushingDataInFile(nameFormatFile))
        self.ui.push_db.clicked.connect(lambda checked, nameFormatFile = 'db': self.PushingDataInFile(nameFormatFile))

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

    def getDataTable(self):
        NameList = []
        PriceList = []
        LinkList = []
        ResultList = []
        parser = DnsShopParser()
        count = 1
        for i in range(self.ui.tableWidget.rowCount() - 1):
            try:
                NameList.append(self.ui.tableWidget.item(count, 0).text())
                PriceList.append(self.ui.tableWidget.item(count, 1).text())
                LinkList.append(self.ui.tableWidget.item(count, 2).text())
                count += 1
            except AttributeError as ex:
                print(ex)
        ResultList = parser._conversion_to_(NameList, PriceList, LinkList)
        return ResultList

    def PushingDataInFile(self, nameFormatFile:str):
        dataList = self.getDataTable()
        if nameFormatFile == 'xlsx':
            upload_to_xlsx_file(dataList)
        elif nameFormatFile == 'csv':
            upload_to_csv_file(dataList)
        elif nameFormatFile == 'json':
            upload_to_json_file(dataList) 
        elif nameFormatFile == 'db':
            for i in range(len(dataList)):
                upload_to_db_file(dataList, i)           

    def build_table_proc(self, _text):
        self.ui.comboBox.activated[str].connect(self.build_table_proc)
        dir = os.path.abspath(os.curdir)
        list_frwrd = open_data(dir[:-6] + 'data/' + 'data1Proc.picle')
        list_bck = open_data(dir[:-6] + 'data/' + 'data2Proc.picle')
        list_bck = list(reversed(list_bck))
        self.data_proccesors = list(itertools.chain(list_frwrd, list_bck))
        _pars_obj = DnsShopParser()
        self.ui.comboBox.clear()
        _min_border = int(self.ui.lineEdit.text())
        _max_border = int(self.ui.lineEdit_2.text()) 
        all_indx = _pars_obj.indexing_list(self.data_proccesors)
        manufactures_data = _pars_obj.most_manufactures(self.data_proccesors, all_indx)
        self.ui.comboBox.addItem('All')
        for i in range(len(manufactures_data)):
            for key, value in manufactures_data[i].items():
                if value != 0:
                    self.ui.comboBox.addItem(str(key) + '\t' + str(value))

        _text = _pars_obj.get_symb_of_str(_text)
        _text = _text.replace('\t', '')
        indx_list = _pars_obj.avg_price(self.data_proccesors, _min_border, _max_border, _text)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(indx_list) + 1) 
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(365)
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Название товара"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Цена товара"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Ссылка на товар"))
        self.ui.label_3.setText('Всего товаров:' + str(len(indx_list)))
        count = 0
        for i in indx_list:
            self.ui.tableWidget.setItem(count + 1, 0, QtWidgets.QTableWidgetItem(self.data_proccesors[i].get("Название товара")))
            self.ui.tableWidget.setItem(count + 1, 1, QtWidgets.QTableWidgetItem(str(self.data_proccesors[i].get("Цена товара"))))
            self.ui.tableWidget.setItem(count + 1, 2, QtWidgets.QTableWidgetItem(self.data_proccesors[i].get("Ссылка на товар")))
            count += 1
       
    def build_table_gpu(self, _text):
        self.ui.comboBox.activated[str].connect(self.build_table_gpu)
        dir = os.path.abspath(os.curdir)
        list_frwrd = open_data(dir[:-6] + 'data/' + 'data1Gpu.picle')
        list_bck = open_data(dir[:-6] + 'data/' + 'data2Gpu.picle')
        list_bck = list(reversed(list_bck))
        self.data_gpu = list(itertools.chain(list_frwrd, list_bck))
        _pars_obj = DnsShopParser()
        self.ui.comboBox.clear()
        _min_border = int(self.ui.lineEdit.text())
        _max_border = int(self.ui.lineEdit_2.text())
        all_indx = _pars_obj.indexing_list(self.data_gpu)
        manufactures_data = _pars_obj.most_manufactures(self.data_gpu, all_indx)
        self.ui.comboBox.addItem('All')
        for i in range(len(manufactures_data)):
            for key, value in manufactures_data[i].items():
                if value != 0:
                    self.ui.comboBox.addItem(str(key) + '\t' + str(value))

        _text = _pars_obj.get_symb_of_str(_text)
        _text = _text.replace('\t', '')
        indx_list = _pars_obj.avg_price(self.data_gpu, _min_border, _max_border, _text)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(indx_list) + 1) 
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(365)
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Название товара"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Цена товара"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Ссылка на товар"))
        self.ui.label_3.setText('Всего товаров:' + str(len(indx_list)))
        count = 0
        for i in indx_list:
            self.ui.tableWidget.setItem(count + 1, 0, QtWidgets.QTableWidgetItem(self.data_gpu[i].get("Название товара")))
            self.ui.tableWidget.setItem(count + 1, 1, QtWidgets.QTableWidgetItem(str(self.data_gpu[i].get("Цена товара"))))
            self.ui.tableWidget.setItem(count + 1, 2, QtWidgets.QTableWidgetItem(self.data_gpu[i].get("Ссылка на товар")))
            count += 1

    def build_table_ram(self, _text):
        self.ui.comboBox.activated[str].connect(self.build_table_ram)
        dir = os.path.abspath(os.curdir)
        list_frwrd = open_data(dir[:-6] + 'data/' + 'data1Ram.picle')
        list_bck = open_data(dir[:-6] + 'data/' + 'data2Ram.picle')
        list_bck = list(reversed(list_bck))
        self.data_ram = list(itertools.chain(list_frwrd, list_bck))
        _pars_obj = DnsShopParser()
        self.ui.comboBox.clear()
        _min_border = int(self.ui.lineEdit.text())
        _max_border = int(self.ui.lineEdit_2.text())
        all_indx = _pars_obj.indexing_list(self.data_ram)
        manufactures_data = _pars_obj.most_manufactures(self.data_ram, all_indx)
        self.ui.comboBox.addItem('All')
        for i in range(len(manufactures_data)):
            for key, value in manufactures_data[i].items():
                if value != 0:
                    self.ui.comboBox.addItem(str(key) + '\t' + str(value))

        _text = _pars_obj.get_symb_of_str(_text)
        _text = _text.replace('\t', '')
        indx_list = _pars_obj.avg_price(self.data_ram, _min_border, _max_border, _text)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(indx_list) + 1) 
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setDefaultSectionSize(365)
        self.ui.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Название товара"))
        self.ui.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("Цена товара"))
        self.ui.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("Ссылка на товар"))
        self.ui.label_3.setText('Всего товаров:' + str(len(indx_list)))
        count = 0
        for i in indx_list:
            self.ui.tableWidget.setItem(count + 1, 0, QtWidgets.QTableWidgetItem(self.data_ram[i].get("Название товара")))
            self.ui.tableWidget.setItem(count + 1, 1, QtWidgets.QTableWidgetItem(str(self.data_ram[i].get("Цена товара"))))
            self.ui.tableWidget.setItem(count + 1, 2, QtWidgets.QTableWidgetItem(self.data_ram[i].get("Ссылка на товар")))
            count += 1  


class interface_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(interface_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.flashSplash)
        self.ui.pushButton.released.connect(self.ProcessorParsing)
        #self.ui.pushButton_4.clicked.connect(self.flashSplash)
        self.ui.pushButton_4.released.connect(self.VideocardParsing)
        #self.ui.pushButton_3.clicked.connect(self.flashSplash)
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
        #self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap(dir[:-6] + 'resource/icons8-loading-bar-100.png'))
 
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
        #QtCore.QTimer.singleShot(5000, self.splash.close)


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
        self.thread_2.finished.connect(self.thread_2.deleteLater)
        self.thread_2.start()
        self.ui.pushButton_4.setEnabled(False)
        #QtCore.QTimer.singleShot(5000, self.splash.close)
        

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
        #QtCore.QTimer.singleShot(5000, self.splash.close)

    def flashSplash(self):
        self.splash.show()

    def View(self):
        self.ViewMode_ = None
        if not self.ViewMode_:
            self.ViewMode_ = ViewMode()
        self.ViewMode_.show() 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = SplashScreen()
    #application.show()

    sys.exit(app.exec())        