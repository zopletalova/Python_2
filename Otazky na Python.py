import pandas as pd
import requests
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
  f.write(r.content)

pyth_df = pd.read_csv("MLTollsStackOverflow.csv")

print(pyth_df.head())
print(pyth_df.columns)

#Podívám se,jak vypadá vývoj sloupce python
pyth_df[["python"]].plot()
plt.show()

#Dekompozice
decompose = seasonal_decompose(pyth_df["python"], model='multiplicative', period=12)
decompose.plot()
plt.show()

#Hot Winters
mod = ExponentialSmoothing(pyth_df["python"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
pyth_df["HWint"] = res.fittedvalues
pyth_df[["HWint", "python"]].plot()
plt.show()

#predikce
df_forecast = pd.DataFrame(res.forecast(24), columns=["pyth_pred"])
df_with_prediction = pd.concat([pyth_df, df_forecast])
df_with_prediction[["python", "pyth_pred"]].plot()
plt.show()