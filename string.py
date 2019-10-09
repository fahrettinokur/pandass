# -*- coding: utf-8 -*-

print("fahrettin okur".upper())

import pandas as pd

orders=pd.read_table("orders.tsv")

print(orders.head())
print(orders.columns)
print(orders.quantity.head(10))
orders.item_name=orders.item_name.str.upper()#bumları string operasyon desinde gördüğümüz çoğu şeyi yapabiliriz
print(orders.item_name) #burada bu bölümdeki str leri büyük harf yaptık
#print(orders.item_name.str.contains("chicken".upper())) #burada chinken var olup olmadığını öğrendik
print("Tavuk isteyen kişilerin sayısı=",orders.item_name.str.contains("chicken".upper()).sum())



orders.choice_description= orders.choice_description.str.replace("[","(").str.replace("]",")")
#sürekli olarak str.replace() yapabilirsin


