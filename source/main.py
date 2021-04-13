from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
from Parser import Parser
import sys
import json
## &page=2

## https://www.asos.com/ru/men/novinki/novinki-odezhda/cat/?cid=6993&nlid=mw%7Cновинки%7Cновое%7Coдежда&page=2
class interface_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(interface_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.load_link)
        self.ui.pushButton_2.clicked.connect(self.save_in_json)
        self.prod_data = []
    def load_link(self):
        url_link = self.ui.lineEdit.text()
        p = Parser()
        p.type_prs_1(url_link)
        self.prod_data = p.type_prs_1(url_link)

    def save_in_json(self):
        with open("product_data_list.json", "w", encoding="utf-8") as file:
            json.dump(self.prod_data, file, indent=12, ensure_ascii=False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = interface_window()
    application.show()

    sys.exit(app.exec())        