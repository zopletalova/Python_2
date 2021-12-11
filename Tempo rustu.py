import pandas as pd
import matplotlib.pyplot as plt
import requests
import statistics
import seaborn
from scipy import stats


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

crypto = pd.read_csv("crypto_prices.csv")
#print(crypto.columns)

crypto = crypto[["Name", "Date", "Close"]]
#print(crypto.head())

crypto["Date"] = pd.to_datetime(crypto["Date"])
crypto = crypto.sort_values("Date")

monero = crypto[crypto["Name"]== "Monero"]
monero = monero[["Date", "Close"]]
monero["Change_pct"] = monero["Close"].pct_change()
monero = monero.dropna()
print("MONERO (head):")
print(monero.head())
print()
Gmean = statistics.geometric_mean(monero["Change_pct"] + 1)
print(f"Geometrický průměr procentuální mezidenní změny je "+ str(round(Gmean-1,5))+".")
