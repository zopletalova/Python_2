import requests
import pandas as pd
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)
beton = pd.read_csv("Concrete_Data_Yeh.csv")

print(beton.head())
print(beton.columns)

mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water "
                      " + superplasticizer + coarseaggregate "
                      " + fineaggregate + age", data=beton)
res = mod.fit()
print(res.summary())
print()

print("Koeficient determinace není ani 62 pct. To není nic moc, chtělo by to ještě vylepšovat.")
print("Záporný regresní koeficient má voda. Čím víc vody,tím méně kvalitní beton.")


