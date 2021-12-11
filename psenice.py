import requests
import pandas as pd
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

psenice = pd.read_csv("psenice.csv")
print(psenice.head(100))

print()
print("Hypotéza HO: Rosa a Canadian mají v průměru stejně dlouhá zrna.")
print("Hypotéza H1: Rosa Canadian mají v průměru různě dlouhá zrna.")
print()

x = psenice["Rosa"]
y = psenice["Canadian"]
print(mannwhitneyu(x, y, alternative="two-sided"))

print("Zamítáme hypotézu H0 a tvrdíme, že Rosa Canadian mají v průměru různě dlouhá zrna.")
