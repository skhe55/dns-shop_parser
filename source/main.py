from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
from dns_shop_pars import DnsShopParser, webdriver, NoSuchElementException, StaleElementReferenceException, By, WebDriverWait, EC, time, csv, pd, xlsxwriter
from save_func_diff_format import upload_to_csv_file, upload_to_xlsx_file, upload_to_json_file
import sys


class interface_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(interface_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ProcessorParsing)
        self.ui.pushButton_4.clicked.connect(self.VideocardParsing)
        self.ui.pushButton_3.clicked.connect(self.Ram_DIMMParsing)
        self.data_about_proc = list()
        self.data_about_gp = list()
        self.data_about_ram = list()
        self.list_get_requests = [        
            "https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/", 
            "https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/",
            "https://www.dns-shop.ru/catalog/17a89a3916404e77/operativnaya-pamyat-dimm/"
        ]
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
        self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
 
    def ProcessorParsing(self):
        processors = DnsShopParser(self.driver, self.list_get_requests[1], self.ignored_exceptions)
        price, name, link = processors.parse()
        print(price)
        index = processors.average_price_pool(price, 3099, 5000)
        self.data_about_proc = processors.print_average_price_prod(price, name, link, index)
        upload_to_xlsx_file(self.data_about_proc, "Processors")
        upload_to_csv_file(self.data_about_proc, "Processors")
        upload_to_json_file(self.data_about_proc, "Processors")


    def VideocardParsing(self):
        videocards = DnsShopParser(self.driver, self.list_get_requests[0], self.ignored_exceptions)
        price, name, link = videocards.parse()
        print(price)
        index = videocards.average_price_pool(price, 5000, 15000)
        self.data_about_gp = videocards.print_average_price_prod(price, name, link, index)
        upload_to_xlsx_file(self.data_about_gp, "Videocards")
        upload_to_csv_file(self.data_about_gp, "Videocards")
        upload_to_json_file(self.data_about_gp, "Videocards")

    def Ram_DIMMParsing(self):
        ram = DnsShopParser(self.driver, self.list_get_requests[2], self.ignored_exceptions)
        price, name, link = ram.parse()
        print(price)
        index = ram.average_price_pool(price, 2000, 2500)
        self.data_about_ram = ram.print_average_price_prod(price, name, link, index)
        upload_to_xlsx_file(self.data_about_ram, "ram_dimm")
        upload_to_csv_file(self.data_about_ram, "ram_dimm")
        upload_to_json_file(self.data_about_ram, "ram_dimm")

 

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = interface_window()
    application.show()

    sys.exit(app.exec())        