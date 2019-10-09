# -*- coding: utf-8 -*-

data1={
       "id":[1,2,3,4],
       "name":["fahrettin","emirhan","kaan","yusuf"],
       "lastname":["okur","kılıç","şen","önder"]

       }

data2={
      "id":[1,3,4,7,1],
      "order":["Eggs","apple","lemon","kebab","yogurt"],
      "time":["noon","afternoon","night","morning","night"]
      
      }
import pandas as pd

data1Df=pd.DataFrame(data1)
data2Df=pd.DataFrame(data2)

print(data1Df)
print(data2Df)
print("\n*********************\n")
print(pd.merge(data1Df,data2Df,on="id"))#burada sadece ortak olanları getirdi.
print("\n*************************************************\n")
print(pd.merge(data1Df,data2Df,on="id",how="inner"))#burda id aynı olanlar yan yana geldi
print("\n*********************\n")
print(pd.merge(data1Df,data2Df,on="id",how="left"))
#burada id si aynı olanı al ama soldan aynı olmayanı al demek yani 2 numaradki bilgiler nan
print("\n*********************\n")
print(pd.merge(data1Df,data2Df,on="id",how="right"))
#buda leftin tam tersi
print("\n*********************\n")
print(pd.concat([data1Df,data2Df]))#buda data birleştirmeye yara
print("\n*********************\n")
print(pd.concat([data1Df,data2Df],axis=1))#böyle yapınca yan olarak alır verileri

