# -*- coding: utf-8 -*-

import pandas as pd

notlar=pd.read_csv("grades.csv")
notlar.columns=["soyisim","isim","ssn","sınav1","sınav2","sınav3","sınav4","final","sonuç"]
print(type(notlar))
print(notlar.head())
print(notlar.tail())
print(notlar)
print(notlar["isim"])