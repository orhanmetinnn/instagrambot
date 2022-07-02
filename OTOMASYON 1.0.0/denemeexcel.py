import pandas as pd
import xlsxwriter
import numpy
# sayac=1
# sayacbitir=50

# while True:
#     if sayac != sayacbitir:
#         df = pd.DataFrame({"Personel":[f"Person1"],
#                            "Özel Durum":["Özel durum yok"]})
#         sayac=sayac+1
#         writer=pd.ExcelWriter("vardiya_istanbulmasası.xlsx",engine="xlsxwriter")
#         df.to_excel(writer,sheet_name="Sheet1")
#         writer.save()
#     else:
#         break
#
#
# # df= pd.read_excel("vardiya_istanbulmasasıorhan.xlsx")
# # data=pd.DataFrame(df)
# # print(data)


class vardiya:
    def __init__(self):
        self.gizemdeniz=["Person1","Person2","Person3","Person4","Person5","Person6","Person7","Person8","Person9","Person10","Person11","Person12"]
        self.ozkancuruk=["Person1","Person2","Person3","Person4","Person5","Person6","Person7","Person8","Person9","Person10","Person11","Person12"]
    def a(self):
        sabah=input("Kaç Kişi Gerekli")





# vadi=vardiya()
# print(vadi.a())

b={"kitap":"book"}

if "book" in b.values():
    print(b["kitap"])
else:
    print("başarısız")