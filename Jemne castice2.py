import requests
import pandas as pd
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)
pollution = pd.read_csv("air_polution_ukol.csv")

# Převod data
pollution["date"] = pd.to_datetime(pollution["date"], format="%Y/%m/%d")
pollution["month"] = pollution["date"].dt.month
pollution["year"] = pollution["date"].dt.year
print(pollution.head())

DF_X = pollution[(pollution["year"] == 2019) & (pollution["month"] == 1)]
#print(DF_X.head())
DF_Y = pollution[(pollution["year"] == 2020) & (pollution["month"] == 1)]
#print(DF_Y.head())

print()
print("Hypotéza HO: Leden 19 a 20 mají v průměru stejné pollution hodnoty.")
print("Hypotéza H1: Leden 19 a 20 mají v průměru různé pollution hodnoty.")
print()

x = DF_X["pm25"]
y = DF_Y["pm25"]
print(mannwhitneyu(x, y, alternative="two-sided"))
print()
print("Zamítáme na hladině významnosti 5 pct hypotézu HO, že leden 19 a 20 mají v průměru stejné pollution hodnoty.")
print("Tvrdíme v souladu s hypotézou H1: Leden 19 a 20 mají v průměru různé pollution hodnoty.")