# -*- coding: utf-8 -*-

import pandas as pd

films=pd.read_csv("imdb-1000.csv")
print(films.columns)
print("filimlerin genel ortalaması=",films.star_rating.mean())
print(films.groupby("genre").star_rating.mean())