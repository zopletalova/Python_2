import pandas as pd
import requests
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)
pollution = pd.read_csv("air_polution_ukol.csv")
print(pollution.head())
# Převod data
pollution["date"] = pd.to_datetime(pollution["date"], format="%Y/%m/%d")
pollution["month"] = pollution["date"].dt.month
pollution["year"] = pollution["date"].dt.year
print(pollution.head())
print()
pollution_pivot = pd.pivot_table(pollution, values="pm25", index="month", columns="year", aggfunc=numpy.mean)
print(pollution_pivot)
sns.heatmap(pollution_pivot, annot=True, fmt=".1f", linewidths=.5, cmap="YlGn")
plt.show()
print("Největší znečištění je v zimních měsících, přes léto klesá.")

# Dny v týdnu
pollution["week_day"] = pollution["date"].dt.dayofweek
pollution["week_day"] = pollution["week_day"].replace([0, 1, 2, 3, 4, 5, 6], ["0-pondělí", "1-úterý", "2-středa", "3-čtvrtek", "4-pátek", "5-sobota", "6-neděle"])
print(pollution.head())
print()
pollution_pivot_day = pd.pivot_table(pollution, values="pm25", columns="week_day", aggfunc=numpy.mean)
pollution_grouped = pollution.groupby(["week_day"]).mean("pm25")
pollution_grouped = pollution_grouped["pm25"]
print(pollution_grouped)
pollution_grouped.plot(kind="line", xlabel="day of week", ylabel="pollution",
                      title="Průměrné znečištění v jednotlivých dnech týdne", )
plt.show()
print("Znečištění v rámci pracovního týdne postupně narůstá, během víkendu klesne.")
