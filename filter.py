# -*- coding: utf-8 -*-

import pandas as pd

films=pd.read_csv("imdb-1000.csv")

print(films)
print(films.columns)
print(films.head())
print(films.tail())
print(films["title"].head())
#print(films.title.head())
print(films[["title","star_rating"]].head())
print(films[:9][["title","star_rating"]]) #sonuna head() yaparsan sana baştakini veri buda ayrı bir veri gibi düşün
print(films[
        (films["star_rating"]>=8.9)&(films["star_rating"]<=9.0)]
        [["title","star_rating"]])
print(films.query("star_rating>=9.0 & star_rating<=9.1")[["title","star_rating"]])
#başka yöntemi ise films.query