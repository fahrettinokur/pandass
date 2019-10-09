# -*- coding: utf-8 -*-
import pandas as pd

films= pd.read_csv("imdb-1000.csv")

films=films.drop("content_rating",axis=1) #1 olmasu columns anlamına gelir
films=films.drop("duration",axis=1)
films=films.drop(2,axis=0) #979 dan 978 düştü index mantığa göre
rowTodrop=[0,1,3,4,5,6,7,8,9,90]
films=films.drop(rowTodrop,axis=0) #bu yöntemle satır silinebilir bunlar dataframe
print(films)
print(films.mean())

