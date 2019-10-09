# -*- coding: utf-8 -*-

import pandas as pd

data=[10,20,30,40,50]
df=pd.DataFrame(data)
print(df)


knowledge=[["fahrettin",21,"Denizli"],["ahmet",10,"Adana"],["Göksel",21,"Çanakkale"]]
dataf=pd.DataFrame(knowledge,index=[1,2,3],columns=["NAME","AGE","CİTY"])
print(dataf)
#print(dataf["NAME"])
# del dataf["AGE"]   # iki türlüde istenen kolon silinebilir
#print("\n\n",dataf)
# dataf.pop("CİTY") #buda pandas ın verdiği bir özellik
#print("\n\n",dataf)

print("\n",dataf.loc[3]) #satır olarak verdi
print("\n",dataf.iloc[2]) #bu index matığı ile çalışıyor yani 0 dan başlıyor
knowledge2=[["Himmet",31,"Ankara"],["Bekir",18,"Hatay"]]
dataf2=pd.DataFrame(knowledge2,columns=["NAME","AGE","CİTY"])

dataf3=dataf.append(dataf2)
print(dataf3)
print(dataf3.head()) # ilk baştaki 5 veriyi gösterir
print(dataf3.tail()) 