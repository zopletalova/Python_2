import pandas as pd
import requests, numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)
london = pd.read_csv("london_merged.csv")

london["date"] = pd.to_datetime(london["timestamp"])
london["year"] = london["date"].dt.year

#print(london.head())

#Počty jízd v jednotlivých letech a podle jednotlivých typů počasí
london_pivot = pd.pivot_table(london, index="weather_code", columns="year", values="cnt", fill_value=0, aggfunc=numpy.sum, margins=True)
print("Počty jízd dle let a počasí:")
print(london_pivot)
print()

#Bonus - Procenta, jak se podílely jízdy v jednotlivých druzích počasí v jednotlivých letech
london_pivot_percantage = london_pivot.div(london_pivot.iloc[-1,:], axis=1)
print("Procentuální zastoupení jízd dle počasí v jednotlivých letech:")
print(london_pivot_percantage)
print("Nejvíce se jezdilo, když bylo hezky :-)")
