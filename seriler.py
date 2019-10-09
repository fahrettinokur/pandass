# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


data=np.array(["fahrettin","ahmet","hürü"])
s=pd.Series(data,index=[1,2,3]) #kafasına göre verirse 0'dan başlar
print(s)
print(s[1])



data2={"matematik":50,"fizik":78,"kimya":91}
s1=pd.Series(data2)
print(s1)
print("\n\n\n")

data3={"matematik":50,"fizik":78,"kimya":91}
s2=pd.Series(data3,index=["kimya","matematik","fizik"]) 
print(s2) #burdaki index kullanmanın amacı veri yerini değiştirmek
print("Sıfır indexin datası=",s2[0])
print("fizik verisini datası=",s2["fizik"])

series=pd.Series(5,index=[1,2,3,4,5])
print(series)#alışmışın dişinda