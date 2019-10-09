# -*- coding: utf-8 -*-

import pandas as pd

notlar=pd.read_csv("grades.csv")
notlar.columns=["soyisim","isim","ssn","sınav1","sınav2","sınav3","sınav4","final","sonuç"]

print(notlar)
print(notlar.loc[:,"isim"])
print(notlar.loc[:5,"isim"])#burada 5 dahil pandasda dahil olarak 
print(notlar.loc[:5,"isim":"sınav4"])
print(notlar.loc[:5,["isim","soyisim","sınav3"]])
print(notlar.loc[:5,:"sınav2"])
print(notlar.loc[::-1,"isim"])