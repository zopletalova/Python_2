import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg

cisco = yf.Ticker("CSCO")
cisco_df = cisco.history(period="5y")
print(cisco_df.describe())
print(cisco_df.head())
print(cisco_df.columns)

#Podívám se,jak vypadá vývoj akcií
cisco_df[["Close"]].plot()
plt.show()

#Závislost na jedné předchozí hodnotě je samozřejmě vysoká
print(cisco_df["Close"].autocorr(lag=1))
#Další závislosti zobrazuje graf - jsou poměrně vysoké i po x dnech
plot_acf(cisco_df["Close"])
plt.show()

#Tady jsem si nebyla jistá,jestli je to seasonal...
model = AutoReg(cisco_df["Close"], lags=10, trend="t", seasonal=True, period=7)
model_fit = model.fit()

predictions = model_fit.predict(start=cisco_df.shape[0], end=cisco_df.shape[0] + 5)
df_forecast = pd.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pd.concat([cisco_df, df_forecast])
df_with_prediction = df_with_prediction.tail(50)

#Tady mi asi udělal díru v grafu víkend :-)
df_with_prediction[["Close", "Prediction"]].plot()
plt.show()