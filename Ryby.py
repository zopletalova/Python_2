import requests
import pandas as pd
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

fish = pd.read_csv("Fish.csv")

print(fish.head())
print(fish.columns)

mod1 = smf.ols(formula="Weight ~ Length2", data=fish)
res1 = mod1.fit()
print(res1.summary())
print()

print("Koeficient determinace modelu více než 84 pct,což není napoprvé vůbec špatné.")
print()

mod2 = smf.ols(formula="Weight ~ Length2 + Height", data=fish)
res2 = mod2.fit()
print(res2.summary())
print()

print("Výsledek - koeficient determinace ještě trochu vyšší a tím pádem model kvalitnější.")
print()

print(fish["Species"].unique())
print(fish["Species"].unique().shape)

prumery = fish.groupby("Species")["Weight"].mean()
fish["Weight_avg"] = fish["Species"].map(prumery)

mod3 = smf.ols(formula="Weight ~ Length2 + Height + Weight_avg", data=fish)
res3 = mod3.fit()
print(res3.summary())
print()
print("Nakonec jsme koeficient determinace vylepšili na 90 pct.")
