from PyQt5 import QtCore
from save_func_diff_format import upload_to_csv_file, upload_to_xlsx_file, upload_to_json_file
from dns_shop_pars import DnsShopParser, webdriver, NoSuchElementException, StaleElementReferenceException, WebDriverWait, EC, By
from multiprocessing import Process

class getData(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    finished_1 = QtCore.pyqtSignal()
    finished_2 = QtCore.pyqtSignal()
    request = str()
 
    def run_parsing_proc(self):
        processors = DnsShopParser()
        url = processors.get_count_pages(self.request)
        page = url[-2:].replace('=', '')
        process_1 = Process(target=processors.forward_parse, args=(int(page), self.request, 'Proc',)) 
        process_1.start()
        process_2 = Process(target=processors.back_parse, args=(int(page), url, 'Proc',))
        process_2.start()
        process_1.join()
        process_2.join()
        self.finished.emit()   

    def run_parsing_gpu(self):
        videocards = DnsShopParser()
        url = videocards.get_count_pages(self.request)
        page = url[-2:].replace('=', '')
        print(page)
        process_1 = Process(target=videocards.forward_parse, args=(int(page), self.request, 'Gpu',)) 
        process_1.start()
        process_2 = Process(target=videocards.back_parse, args=(int(page), url, 'Gpu',))
        process_2.start()
        process_1.join()
        process_2.join()
        self.finished_1.emit()

    def run_parsing_ram(self):
        ram = DnsShopParser()
        url = ram.get_count_pages(self.request)
        page = url[-2:].replace('=', '')
        process_1 = Process(target=ram.forward_parse, args=(int(page), self.request, 'Ram',)) 
        process_1.start()
        process_2 = Process(target=ram.back_parse, args=(int(page), url, 'Ram',))
        process_2.start()
        process_1.join()
        process_2.join()
        self.finished_2.emit()              

   