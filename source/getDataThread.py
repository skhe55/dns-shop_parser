from PyQt5 import QtCore
from save_func_diff_format import upload_to_csv_file, upload_to_xlsx_file, upload_to_json_file
from dns_shop_pars import DnsShopParser, webdriver, NoSuchElementException, StaleElementReferenceException, WebDriverWait, EC, By


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class getDataThreadProc(QtCore.QThread):
    def __init__(self, request):
        QtCore.QThread.__init__(self)
        self.ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
        self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        self.request = request

    def __del__(self):
        self.wait()

    def run(self):
        processors = DnsShopParser(self.driver, self.request, self.ignored_exceptions)
        price, name, link = processors.parse()
        data_about_proc = processors.print_all_prod(price, name, link)
        upload_to_xlsx_file(data_about_proc, "Processors")
        upload_to_csv_file(data_about_proc, "Processors")
        upload_to_json_file(data_about_proc, "Processors")

class getDataThreadVideocard(QtCore.QThread):
    def __init__(self, request):
        QtCore.QThread.__init__(self)
        self.ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
        self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        self.request = request

    def __del__(self):
        self.wait()

    def run(self):
        videocards = DnsShopParser(self.driver, self.request, self.ignored_exceptions)
        price, name, link = videocards.parse()
        print(price)
        data_about_gp = videocards.print_all_prod(price, name, link)
        upload_to_xlsx_file(data_about_gp, "Videocards")
        upload_to_csv_file(data_about_gp, "Videocards")
        upload_to_json_file(data_about_gp, "Videocards")

class getDataThreadRAM(QtCore.QThread):         
    def __init__(self, request):
        QtCore.QThread.__init__(self)
        self.ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
        self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        self.request = request

    def __del__(self):
        self.wait()

    def run(self):
        ram = DnsShopParser(self.driver, self.request, self.ignored_exceptions)
        price, name, link = ram.parse()
        data_about_ram = ram.print_all_prod(price, name, link)
        upload_to_xlsx_file(data_about_ram, "ram_dimm")
        upload_to_csv_file(data_about_ram, "ram_dimm")
        upload_to_json_file(data_about_ram, "ram_dimm")    