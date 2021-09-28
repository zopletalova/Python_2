import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

#TITANIC
df_titanic = pd.read_csv("titanic.csv")
print(df_titanic.head())
print(df_titanic.tail())
#Zkusim pres groupby
df_titanic_grouped = df_titanic.groupby(["Pclass", "Sex"]).sum("Survived")
print(df_titanic_grouped.head(6))
print()
#A ted totez pres pivot
print("Počet přeživších v dané kategorii - pohlaví, třída:")
df_titanic_pivot = pd.pivot_table(df_titanic, index="Pclass", columns="Sex", values="Survived", aggfunc=numpy.sum)
print(df_titanic_pivot)
print()
#Prumer
print("Pravděpodobnost přežití v dané kategorii - pohlaví, třída:")
df_titanic_pivot = pd.pivot_table(df_titanic, index="Pclass", columns="Sex", values="Survived", aggfunc=numpy.mean)
print(df_titanic_pivot)
print()

#Bonus-TITANIC
df_FirstClass = df_titanic[df_titanic["Pclass"] == 1]
df_FirstClass["age_group"] = pd.cut(df_FirstClass["Age"], bins=[0, 12, 19, 65, 100], labels=["Dítě", "Teenager", "Dospělý", "Senior"])
#Tady vidím, že tam nebyla žádná žena starší 65 - proto NaN v kontingenční tabulce
#seniori = df_FirstClass[df_FirstClass['Age'] > 65]
#print(seniori[["Sex", "Age", "Survived"]])
df_FirstClass_pivot = pd.pivot_table(df_FirstClass, index="Sex", columns="age_group", values="Survived",fill_value=0, aggfunc=numpy.mean)
print(df_FirstClass_pivot)
