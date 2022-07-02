from socialmediagiris import Ui_MainWindow
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from socialmediagiris2 import Ui_MainWindow2
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.second_page=SecondPage()
        self.ui.btngiris.clicked.connect(self.open2page)
        self.second_page.ui1.profiltakibiinstapy.toggled.connect(self.start)
        self.second_page.ui1.kesfettakip.toggled.connect(self.kesfettakibiprogram)
        self.second_page.ui1.kesfettakipvebegeni.toggled.connect(self.kesfettakipvebegeni)
        self.second_page.ui1.kullanicifotografinibegeninitakipetme.toggled.connect(self.profilfotobegenentakip)
        self.second_page.ui1.konumagoretakipetme.toggled.connect(self.Konumgoretakip)
        self.second_page.ui1.konumagoretakipetme_2.toggled.connect(self.profilKonumatakip)
        self.second_page.ui1.kesfetprofiltakip.toggled.connect(self.kesfetprofiltakip)
        self.second_page.ui1.kesfetbegeni.toggled.connect(self.kesfetbegeni)
        self.second_page.ui1.konumbegeni.toggled.connect(self.konumbegeni)
        self.second_page.ui1.Anasayfabegeni.toggled.connect(self.anasayfabegeni)
        self.second_page.ui1.kesfetyorum.toggled.connect(self.kesfetyorum)
        self.second_page.ui1.konumyorum.toggled.connect(self.konumyorum)
    def open2page(self):
        otomysql = mysql.connector.connect(host="89.252.183.162",
                                           user="social11_OtomasyonKontrol",
                                           password="Suskun184.",
                                           database="social11_Otomasyon1.0.0")
        self.cursor = otomysql.cursor()
        self.cursor.execute(f"Select*From otomasyon Where mail= '{self.ui.linemail.text()}' and sifre='{self.ui.linesifre.text()}'")
        self.a = self.cursor.fetchone()
        if self.a != None:
            self.second_page.show()


    def start(self):
        self.basla=Instagramtakipcileritakipet(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),
                                               inssifre=self.second_page.ui1.lnlinstagramsifre.text(),
                                               insprofilismi=self.second_page.ui1.lnlprofiltakipedenlertakipet.text())
        self.basla.start()

    def kesfettakibiprogram(self):
        self.basla1=kesfettakip(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),
                                inssifre=self.second_page.ui1.lnlinstagramsifre.text(),
                                kesfetisim=self.second_page.ui1.lnl_kesfettakip.text())
        self.basla1.start()


    def kesfettakipvebegeni(self):
        self.basla2 = Kesfettakipvebegeni(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),kesfetisim=self.second_page.ui1.lnl_kesfettakipvebegeni.text())
        self.basla2.start()

    def profilfotobegenentakip(self):
        self.basla3=Fotografbegeninitakipetme(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),fotolink=self.second_page.ui1.lnlfotobegenitakip.text())
        self.basla3.start()

    def Konumgoretakip(self):
        self.basla4=Konumagoretakip(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),konumlink=self.second_page.ui1.lnl_konumagoretakipetme.text())
        self.basla4.start()
    def profilKonumatakip(self):
        self.basla5=Konumtakipprofil(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),konumlink=self.second_page.ui1.lnl_konumagoretakipetme_2.text())
        self.basla5.start()
    def kesfetprofiltakip(self):
        self.basla6=Kesfetprofiltakip(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),kesfetisim=self.second_page.ui1.lnl_kesfettakip_2.text())
        self.basla6.start()
    def kesfetbegeni(self):
        self.basla7=Kesfetbegeni(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),kesfetisim=self.second_page.ui1.lnlkesfetbegeni.text())
        self.basla7.start()
    def konumbegeni(self):
        self.basla8=Konumbegeni(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),konumlink=self.second_page.ui1.lnlkonumbegeni.text())
        self.basla8.start()
    def anasayfabegeni(self):
        self.basla9=Anasayfabegeni(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text())
        self.basla9.start()
    def kesfetyorum(self):
        self.basla10=Kesfetyorum(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),kesfetisim=self.second_page.ui1.lnlkesfetbegeni_3.text(),yorum=self.second_page.ui1.kesfetyorumtext.text())
        self.basla10.start()
    def konumyorum(self):
        self.basla11=Konumyorum(inskullaniciadi=self.second_page.ui1.lnlinstagramkullaniciadi.text(),inssifre=self.second_page.ui1.lnlinstagramsifre.text(),konumlink=self.second_page.ui1.lnlkonumbegeni_3.text(),yorum=self.second_page.ui1.konumyorumtext.text())
        self.basla11.start()

class SecondPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui1=Ui_MainWindow2()
        self.ui1.setupUi(self)



class Instagramtakipcileritakipet(QThread):
    sonuc=pyqtSignal(object)
    def __init__(self,inskullaniciadi,inssifre,insprofilismi):
        super().__init__()
        self.inskullaniciadi=inskullaniciadi
        self.inssifre=inssifre
        self.insprofilismi=insprofilismi
    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(20)  #zaman
        self.browser.get(f"https://www.instagram.com/{self.insprofilismi}")
        time.sleep(15)
        self.browser.find_element(By.XPATH,"//ul/li/a/div/span[@class='_ac2a']").click()
        time.sleep(5)
        sayac=1
        sayacbitir=350
        while True:
            if sayac != sayacbitir:
                try:
                    if "İstek Gönderildi" or "Takiptesin" not in self.browser.page_source:
                        a = self.browser.find_element(By.XPATH,"//div/button/div[text()='Takip Et']")
                        a.click()
                        time.sleep(20)
                        sayac=sayac+1
                except selenium.common.exceptions.ElementClickInterceptedException:
                    self.browser.get(f"https://www.instagram.com/{self.insprofilismi}")
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div/span").click()

                except:
                    self.browser.get(f"https://www.instagram.com/{self.insprofilismi}")
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div/span").click()
            else:
                self.browser.close()

class kesfettakip(QThread):
    sonuc=pyqtSignal(object)
    def __init__(self,inskullaniciadi,inssifre,kesfetisim):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.kesfetisim=kesfetisim


    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(20)
        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_L4']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 400
        while True:
            if sayac!=sayacbitir:
                if "_9AhH0" in self.browser.page_source:
                    time.sleep(15)
                    self.browser.refresh()
                    try:
                        if "beğenme" or "beğendi" in self.browser.page_source:
                            self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div").click()
                            time.sleep(15)
                            try:
                                if "İstek Gönderildi" or "Takiptesin" not in self.browser.page_source:
                                    a = self.browser.find_element(By.XPATH, "//div/div/div/div/div/button/div[text()='Takip Et']")
                                    a.click()
                                    time.sleep(1000)  #zaman
                                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                                    time.sleep(15)
                                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                    time.sleep(15)
                                    self.browser.refresh()
                                    time.sleep(15)
                                    sayac=sayac+1
                            except selenium.common.exceptions.NoSuchElementException:
                                self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                                time.sleep(15)
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                time.sleep(15)
                                self.browser.refresh()
                                time.sleep(15)
                            except:
                                self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                                time.sleep(15)
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                time.sleep(15)
                                self.browser.refresh()
                                time.sleep(15)
                    except selenium.common.exceptions.NoSuchElementException:
                        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                        time.sleep(15)
                        self.browser.refresh()
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        time.sleep(15)
                        self.browser.refresh()
                        time.sleep(15)
                else:
                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                    time.sleep(15)
                    self.browser.refresh()
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()
                    time.sleep(15)
            else:
                break


class Kesfettakipvebegeni(QThread):
    sonuc=pyqtSignal(object)
    def __init__(self,inskullaniciadi,inssifre,kesfetisim):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.kesfetisim=kesfetisim


    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 400
        while True:
            if sayac!=sayacbitir:
                try:
                    if "_9AhH0" in self.browser.page_source:
                        time.sleep(15)
                        self.browser.refresh()
                        time.sleep(15)
                        try:
                            if "beğenme" in self.browser.page_source:
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div").click()
                                time.sleep(15)
                                a = self.browser.find_element(By.XPATH,"//div/div/div/div/div/button/div[text()='Takip Et']")
                                a.click()
                                self.browser.refresh()
                                time.sleep(1000)
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
                                sayac=sayac+1
                                self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                                time.sleep(15)
                                self.browser.refresh()
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                time.sleep(15)

                            else:
                                self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                                time.sleep(15)
                                self.browser.refresh()
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                time.sleep(15)
                                self.browser.refresh()

                        except:
                            self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                            time.sleep(15)
                            self.browser.refresh()
                            self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                            time.sleep(15)
                            self.browser.refresh()

                    else:
                        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                        time.sleep(15)
                        self.browser.refresh()
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        time.sleep(15)
                        self.browser.refresh()

                except:
                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                    time.sleep(15)
                    self.browser.refresh()
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()


class Fotografbegeninitakipetme(QThread):
    sonuc = pyqtSignal(object)
    def __init__(self,inskullaniciadi,inssifre,fotolink):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.fotolink=fotolink

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(self.fotolink)
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div").click()
        sayac=1
        sayacbitir=400
        while True:
            if sayac !=sayacbitir:
                time.sleep(10)
                try:
                    time.sleep(10)
                    a = self.browser.find_element(By.XPATH, "//div/div/div/div/div/button/div[text()='Takip Et']")
                    a.click()
                    time.sleep(1000)
                    sayac=sayac+1
                    print(sayac)



                except:
                    self.browser.get(self.fotolink)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div").click()

            else:
                break


class Konumagoretakip(QThread):
    sonuc = pyqtSignal(object)
    def __init__(self, inskullaniciadi, inssifre, konumlink):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.konumlink=konumlink

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(self.konumlink)
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac=1
        sayacbitir=450
        while True:
            if sayac !=sayacbitir:
                time.sleep(10)
                try:
                    if "_9AhH0" in self.browser.page_source:
                        time.sleep(15)
                        self.browser.refresh()
                        time.sleep(15)
                        try:
                            if "beğenme" in self.browser.page_source:
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div").click()
                                time.sleep(15)
                                a = self.browser.find_element(By.XPATH, "//div/div/div/div/div/button/div[text()='Takip Et']")
                                a.click()
                                time.sleep(1000) #sayac
                                self.browser.get(self.konumlink)
                                time.sleep(20)
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                self.browser.refresh()
                                time.sleep(15)
                            else:
                                self.browser.get(self.konumlink)
                                time.sleep(20)
                                self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                                self.browser.refresh()
                                time.sleep(15)
                        except:
                            self.browser.get(self.konumlink)
                            time.sleep(20)
                            self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                            self.browser.refresh()
                            time.sleep(15)
                    else:
                        self.browser.get(self.konumlink)
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        self.browser.refresh()
                        time.sleep(15)
                except:
                    self.browser.get(self.konumlink)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    self.browser.refresh()
                    time.sleep(15)



class Konumtakipprofil(QThread):
    sonuc = pyqtSignal(object)

    def __init__(self, inskullaniciadi, inssifre, konumlink):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.konumlink = konumlink

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(self.konumlink)
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 450
        while True:
            if sayac != sayacbitir:
                time.sleep(15)
                try:
                    if "Takip Et" in self.browser.page_source:
                        self.browser.find_element(By.XPATH,"//button/div[text()='Takip Et']").click()
                        time.sleep(1000) #zaman
                        self.browser.get(self.konumlink)
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        self.browser.refresh()
                        time.sleep(15)

                    else:
                        self.browser.get(self.konumlink)
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        self.browser.refresh()
                        time.sleep(15)
                except:
                    self.browser.get(self.konumlink)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    self.browser.refresh()
                    time.sleep(15)
            else:
                break


class Kesfetprofiltakip(QThread):
    sonuc = pyqtSignal(object)

    def __init__(self, inskullaniciadi, inssifre, kesfetisim):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.kesfetisim = kesfetisim

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 400
        while True:
            if sayac !=sayacbitir:
                time.sleep(15)
                try:
                    if "Takip Et" in self.browser.page_source:
                        self.browser.find_element(By.XPATH,"//button/div[text()='Takip Et']").click()
                        time.sleep(1000) #zaman
                        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        self.browser.refresh()
                        time.sleep(20)
                    else:
                        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        self.browser.refresh()
                        time.sleep(20)
                except:
                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    self.browser.refresh()
                    time.sleep(20)
            else:
                break



"""
Beğeni işlemleri
"""

class Kesfetbegeni(QThread):
    def __init__(self, inskullaniciadi, inssifre, kesfetisim):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.kesfetisim = kesfetisim

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 400
        while True:
            if sayac !=sayacbitir:
                time.sleep(15)
                try:
                    if "Beğenmekten Vazgeç" not in self.browser.page_source:
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
                        sayac = sayac + 1
                        time.sleep(1000)
                        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                        time.sleep(15)
                        self.browser.refresh()
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        time.sleep(15)
                    else:
                        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                        time.sleep(15)
                        self.browser.refresh()
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        time.sleep(15)
                except:
                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                    time.sleep(15)
                    self.browser.refresh()
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
            else:
                break



class Konumbegeni(QThread):
    sonuc = pyqtSignal(object)

    def __init__(self, inskullaniciadi, inssifre, konumlink):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.konumlink = konumlink

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(self.konumlink)
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 450
        while True:
            if sayac != sayacbitir:
                time.sleep(10)
                try:
                    if "Beğenmekten Vazgeç" not in self.browser.page_source:
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
                        sayac = sayac + 1
                        time.sleep(1000)  #zaman
                        self.browser.get(self.konumlink)
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        time.sleep(15)
                        self.browser.refresh()
                    else:
                        self.browser.get(self.konumlink)
                        time.sleep(20)
                        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                        time.sleep(15)
                        self.browser.refresh()
                except:
                    self.browser.get(self.konumlink)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()
            else:
                break




class Anasayfabegeni(QThread):
    sonuc = pyqtSignal(object)

    def __init__(self, inskullaniciadi, inssifre):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[1]/a/div/div").click()
        time.sleep(20)
        if "Bildirimleri Aç" in self.browser.page_source:
            self.browser.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]").click()
        sayac=1
        sayacbitir=450
        while True:
            if sayac!=sayacbitir:
                time.sleep(10)
                try:
                    self.browser.find_element(By.XPATH,"//div/span/*[name()='svg'][@aria-label='Beğen']").click()
                    time.sleep(1000)
                except:
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/nav/div[2]/div/div/div[1]/a/div/div").click()
            else:
                break



"""
Yorum işlemleri
"""

class Kesfetyorum(QThread):
    def __init__(self, inskullaniciadi, inssifre, kesfetisim,yorum):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.kesfetisim = kesfetisim
        self.yorum=yorum

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 400
        while True:
            if sayac !=sayacbitir:
                time.sleep(15)
                try:
                    self.browser.find_element(By.CSS_SELECTOR,"textarea.PUqUI.Ypffh").click()
                    time.sleep(3)
                    self.browser.find_element(By.CSS_SELECTOR,"textarea.PUqUI.Ypffh.focus-visible").send_keys(self.yorum)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div").click()
                    time.sleep(1200)
                    sayac=sayac+1
                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()
                except:
                    self.browser.get(f"https://www.instagram.com/explore/tags/{self.kesfetisim}")
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()
            else:
                break



class Konumyorum(QThread):
    sonuc = pyqtSignal(object)

    def __init__(self, inskullaniciadi, inssifre, konumlink,yorum):
        super().__init__()
        self.inskullaniciadi = inskullaniciadi
        self.inssifre = inssifre
        self.konumlink = konumlink
        self.yorum=yorum

    def run(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.inskullaniciadi)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.inssifre)
        time.sleep(15)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(180)
        self.browser.get(self.konumlink)
        time.sleep(20)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
        time.sleep(15)
        self.browser.refresh()
        sayac = 1
        sayacbitir = 450
        while True:
            if sayac != sayacbitir:
                time.sleep(10)
                try:
                    self.browser.find_element(By.CSS_SELECTOR,"textarea.PUqUI.Ypffh").click()
                    time.sleep(3)
                    self.browser.find_element(By.CSS_SELECTOR,"textarea.PUqUI.Ypffh.focus-visible").send_keys(self.yorum)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div").click()
                    time.sleep(1200)
                    sayac=sayac+1
                    self.browser.get(self.konumlink)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()
                except:
                    self.browser.get(self.konumlink)
                    time.sleep(20)
                    self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div").click()
                    time.sleep(15)
                    self.browser.refresh()
            else:
                break














app=QApplication([])
window=MainPage()
window.show()
app.exec_()