from socialmediagiris2 import Ui_MainWindow2
from selenium import webdriver
import time
from PyQt5.QtWidgets import *

class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1=Ui_MainWindow2()
        self.ui1.setupUi(self)

    def instagramprofiltakip(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(5)
        print(str(self.ui1.lnlinstagramkullaniciadi.text()))
        print(self.ui1.lnlinstagramsifre.text())




