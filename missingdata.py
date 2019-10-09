# -*- coding: utf-8 -*-

#burdaki amaç gelen verilerin belki bazı kolonları boş kalcak birkaçının
#onlara işlem yapmaya yarıyot
import pandas as pd

url="http://bit.ly/uforeports"

data=pd.read_csv(url)
#print(data)
#print(data.columns)
#print(data.isnull().head(100))#burada true olanlar boş
#print(data.notnull().head(100))#tam tersi boş ise false
#print(data.isnull().sum())
#print(data[data.City.isnull()])


print(data.columns)
print(data.shape)
#data=data.dropna(how="any") #bu halde satırda bozukveri varsa o satırı sil
#how="all" ise bütün satırlar nan olursa siler
#data=data.dropna(subset=["City","Colors Reported"],how="any")
data["Shape Reported"].fillna(value="belirsiz",inplace=True)
print(data["Shape Reported"].value_counts(dropna=False))
print(data.shape)
print(data.isnull().head(20).sum())




