import pandas as pd
import matplotlib.pyplot as plt
import requests
import statistics
import seaborn

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

crypto = pd.read_csv("crypto_prices.csv")
#print(crypto.columns)

crypto = crypto[["Name", "Date", "Close"]]
#print(crypto.head())

crypto["Date"] = pd.to_datetime(crypto["Date"])
crypto = crypto.sort_values("Date")

aave = crypto[crypto["Name"]== "Aave"]
bitcoin = crypto[crypto["Name"]== "Bitcoin"]
litecoin = crypto[crypto["Name"]== "Litecoin"]
binance = crypto[crypto["Name"]== "Binance Coin"]
usd = crypto[crypto["Name"]== "USD Coin"]
xrp = crypto[crypto["Name"]== "XRP"]
cardano = crypto[crypto["Name"]== "Cardano"]
chain = crypto[crypto["Name"]== "Chainlink"]
cosmos = crypto[crypto["Name"]== "Cosmos"]
wrapped = crypto[crypto["Name"]== "Wrapped Bitcoin"]
crypto_coin = crypto[crypto["Name"]== "Crypto.com Coin"]
uniswap = crypto[crypto["Name"]== "Uniswap"]
dogecoin = crypto[crypto["Name"]== "Dogecoin"]
tron = crypto[crypto["Name"]== "TRON"]
eos = crypto[crypto["Name"]== "EOS"]
tether = crypto[crypto["Name"]== "Tether"]
ethereum = crypto[crypto["Name"]== "Ethereum"]
stellar = crypto[crypto["Name"]== "Stellar"]
iota = crypto[crypto["Name"]== "IOTA"]
solana = crypto[crypto["Name"]== "Solana"]
monero = crypto[crypto["Name"]== "Monero"]
polkadot = crypto[crypto["Name"]== "Polkadot"]
nem = crypto[crypto["Name"]== "NEM"]

aave = aave.rename(columns={"Close": "Aave"})
aave = aave[["Aave","Date"]]
bitcoin = bitcoin.rename(columns={"Close": "Bitcoin"})
bitcoin = bitcoin[["Bitcoin","Date"]]
litecoin = litecoin.rename(columns={"Close": "Litecoin"})
litecoin = litecoin[["Litecoin","Date"]]
binance = binance.rename(columns={"Close": "Binance Coin"})
binance = binance[["Binance Coin", "Date"]]
usd = usd.rename(columns={"Close": "USD Coin"})
usd = usd[["USD Coin","Date"]]
xrp = xrp.rename(columns={"Close": "XRP"})
xrp = xrp[["XRP","Date"]]
cardano = cardano.rename(columns={"Close": "Cardano"})
cardano = cardano[["Cardano","Date"]]
chain = chain.rename(columns={"Close": "Chainlink"})
chain = chain[["Chainlink","Date"]]
cosmos = cosmos.rename(columns={"Close": "Cosmos"})
cosmos = cosmos[["Cosmos","Date"]]
wrapped = wrapped.rename(columns={"Close": "Wrapped Bitcoin"})
wrapped = wrapped[["Wrapped Bitcoin","Date"]]
crypto_coin = crypto_coin.rename(columns={"Close": "Crypto.com Coin"})
crypto_coin = crypto_coin[["Crypto.com Coin","Date"]]
uniswap = uniswap.rename(columns={"Close": "Uniswap"})
uniswap = uniswap[["Uniswap","Date"]]
dogecoin = dogecoin.rename(columns={"Close": "Dogecoin"})
dogecoin = dogecoin[["Dogecoin","Date"]]
tron = tron.rename(columns={"Close": "TRON"})
tron = tron[["TRON","Date"]]
eos = eos.rename(columns={"Close": "EOS"})
eos = eos[["EOS","Date"]]
tether = tether.rename(columns={"Close": "Tether"})
tether = tether[["Tether","Date"]]
ethereum = ethereum.rename(columns={"Close": "Ethereum"})
ethereum = ethereum[["Ethereum","Date"]]
stellar = stellar.rename(columns={"Close": "Stellar"})
stellar = stellar[["Stellar","Date"]]
iota = iota.rename(columns={"Close": "IOTA"})
iota = iota[["IOTA","Date"]]
solana = solana.rename(columns={"Close": "Solana"})
solana = solana[["Solana","Date"]]
monero = monero.rename(columns={"Close": "Monero"})
monero = monero[["Monero","Date"]]
polkadot = polkadot.rename(columns={"Close": "Polkadot"})
polkadot = polkadot[["Polkadot","Date"]]
nem = nem.rename(columns={"Close": "NEM"})
nem = nem[["NEM","Date"]]

cryptox = pd.merge(aave, bitcoin, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,litecoin, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,binance, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,usd, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,xrp, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,cardano, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,chain, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,cosmos, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,wrapped, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,crypto_coin, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,uniswap, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,dogecoin, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,tron, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,eos, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,tether, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,ethereum, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,stellar, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,iota, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,solana, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,monero, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,polkadot, on=["Date"], how = "left")
cryptox = pd.merge(cryptox,nem, on=["Date"], how = "left")

crypto_close = cryptox[["Aave", "Bitcoin", "Litecoin", "Binance Coin", "USD Coin", "XRP","Cardano",
                   "Chainlink","Cosmos","Wrapped Bitcoin","Crypto.com Coin","Uniswap","Dogecoin",
                   "TRON","EOS","Tether","Ethereum","Stellar","IOTA","Solana","Monero","Polkadot","NEM"]]

crypto_change = crypto_close.pct_change()
crypto_change = crypto_change.dropna()

print("Tabulka změn:")
print(crypto_change)
print()

print("Parson:")
print(crypto_change.corr())
print()
print("Spearman:")
print(crypto_change.corr(method="spearman"))

#grafy - dva silné
bit_lite = crypto_change[["Bitcoin", "Litecoin"]]
seaborn.jointplot(data = bit_lite, kind='scatter')
plt.show()
bit_wr = crypto_change[["Bitcoin", "Wrapped Bitcoin"]]
seaborn.jointplot(data = bit_wr, kind='scatter')
plt.show()

#grafy - dva slabé
tet_mon = crypto_change[["Tether", "Monero"]]
seaborn.jointplot(data = tet_mon, kind='scatter')
plt.show()
usd_polka = crypto_change[["USD Coin", "Polkadot"]]
seaborn.jointplot(data = usd_polka, kind='scatter')
plt.show()

#doplněk 2
bit = crypto[crypto["Name"]== "Bitcoin"]
lit = crypto[crypto["Name"]== "Litecoin"]
bit_lit2 = pd.merge(bit,lit, on=["Date"], how = "left", suffixes=["BIT", "LIT"])
bit_lit2 = bit_lit2.head(30)
bit_lit2 = bit_lit2[["Date", "CloseBIT", "CloseLIT"]]
bit_lit2 = bit_lit2.sort_values("Date")
bit_lit2.plot(x="Date", kind = "line", title = "Bitcoin vs Litecoin")
plt.show()
print("BITCOIN - LITECOIN: Každý absolutně na jiné úrovni, ale relativně vývoj obdobný.")
print()

tet = crypto[crypto["Name"]== "Tether"]
mon = crypto[crypto["Name"]== "Monero"]
tet_mon2 = pd.merge(tet,mon, on=["Date"], how = "left", suffixes=["TET", "MON"])
tet_mon2 = tet_mon2.head(30)
tet_mon2 = tet_mon2[["Date", "CloseTET", "CloseMON"]]
tet_mon2 = tet_mon2.sort_values("Date")
tet_mon2.plot(x="Date", kind = "line", title = "Tether vs Monero")
plt.show()
print("TETHER - MONERO: Jeden se vlní a druhý je čára - rozdílný trend vývoje.")
