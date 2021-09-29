import pandas as pd
import requests
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)
president = pd.read_csv("1976-2020-president.csv")
# print(president.head())

# Pomocí rank určím pořadí v rámci let a států:
president["Rank"] = president.groupby(["year", "state"])["candidatevotes"].rank(method="min", ascending=False)
# Zkontroluji, zda je to ok, třeba pro UTAH roku 1984:
print("KONTROLA - UTAH v roce 1984 - pořadí stran s hodnotou Rank:")
president_u84 = president[(president["year"] == 1984) & (president["state"] == "UTAH")]
print(president_u84[["year", "state", "party_detailed", "candidatevotes", "Rank"]])
print()

# Vyfiltruji pouze vítěze:
president1 = president[(president["Rank"] == 1)]
# Seřadím podle státu a roku:
president1_sorted = president1.sort_values(["state", "year"])

# Pomocí shift přidám sloupec s vítězem následujících voleb:
president1_sorted["party_detailed_next"] = president1_sorted["party_detailed"].shift(periods=-1)
# Vyhodím rok 2020:
president1_sorted = president1_sorted[president1_sorted["year"] != 2020]
# Dodám sloupec changed, hodnota 1 = změna vítěze:
president1_sorted["changed"] = numpy.where(president1_sorted["party_detailed"] != president1_sorted["party_detailed_next"], 1, 0)
# Kontrolní výpis - Florida, 5x změna, což se potvrdí i pak níže ve výsledku
president_Florida = president1_sorted[(president1_sorted["state"] == "FLORIDA")]
print("KONTROLA - Počet změn vítěze voleb zaznamenané ve sloupci changed pro stát FLORIDA")
print(president_Florida[["state", "year", "party_detailed", "party_detailed_next", "changed"]])
print()

# Seskupím podle států a posčítám v rámci nich změny, seřadím od nejvíc "swinging":
president1_final = president1_sorted.groupby(["state"]).sum("changed")
president1_final = president1_final.sort_values(["changed"], ascending=False)
print("VÝSLEDEK - Státy,kde se nejvíc střídaly vítězné strany - počet změn = changed:")
print(president1_final[["changed"]])
print()

# BONUS
# Mám v df president uložen celý soubor upravený přes rank, můžu rovnou použít shift
president["candidatevotes_second"] = president["candidatevotes"].shift(periods=-1)

# Ponechám jen řádky vítězů, ostatní už nepotřebuji
president11 = president[president["Rank"] == 1].copy()
president11["votes_delta"] = president11["candidatevotes"] - president11["candidatevotes_second"]
president11["votes_margin"] = president11["votes_delta"] / president11["totalvotes"]
president11 = president11.sort_values("votes_margin")
print("BONUS - Počty hlasů, o které měla vítězná strana náskok před druhou v pořadí; margin.")
print("Na začátku nejtěsnější rozdíly v historii, na konci největší")
print(president11[["state", "year", "party_detailed", "votes_delta", "votes_margin"]])
