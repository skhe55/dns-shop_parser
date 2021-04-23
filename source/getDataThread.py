from PyQt5 import QtCore
from save_func_diff_format import upload_to_csv_file, upload_to_xlsx_file, upload_to_json_file
from dns_shop_pars import DnsShopParser, webdriver, NoSuchElementException, StaleElementReferenceException, WebDriverWait, EC, By


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class getData(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    finished_1 = QtCore.pyqtSignal()
    finished_2 = QtCore.pyqtSignal()
    ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
    request = str()
    data_about_proc = list()
    def run_parsing_proc(self):
        processors = DnsShopParser(self.driver, self.request, self.ignored_exceptions)
        price, name, link = processors.parse()
        self.data_about_proc = processors.print_all_prod(price, name, link)
        upload_to_xlsx_file(self.data_about_proc, "Processors")
        upload_to_csv_file(self.data_about_proc, "Processors")
        upload_to_json_file(self.data_about_proc, "Processors")
        self.finished.emit()   

    def run_parsing_gpu(self):
        videocards = DnsShopParser(self.driver, self.request, self.ignored_exceptions)
        price, name, link = videocards.parse()
        print(price)
        data_about_gp = videocards.print_all_prod(price, name, link)
        upload_to_xlsx_file(data_about_gp, "Videocards")
        upload_to_csv_file(data_about_gp, "Videocards")
        upload_to_json_file(data_about_gp, "Videocards")
        self.finished_1.emit()

    def run_parsing_ram(self):
        ram = DnsShopParser(self.driver, self.request, self.ignored_exceptions)
        price, name, link = ram.parse()
        data_about_ram = ram.print_all_prod(price, name, link)
        upload_to_xlsx_file(data_about_ram, "ram_dimm")
        upload_to_csv_file(data_about_ram, "ram_dimm")
        upload_to_json_file(data_about_ram, "ram_dimm")
        self.finished_2.emit()              

    def _return_data_(self, data_about_prod:list):
        return data_about_prod    