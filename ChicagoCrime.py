import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "zuzana.opletalova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "Wx0=CN.K9Ts39j!M"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

inspector = inspect(engine)
print(inspector.get_table_names())

kradeze = pd.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)

#print(kradeze.head())
#print(kradeze.columns)

kradeze_filtr = kradeze[kradeze["SECONDARY_DESCRIPTION"].isin(["AUTOMOBILE", "automobile"])]
kradeze_filtr = kradeze_filtr[["CASE#", "DATE_OF_OCCURRENCE", "PRIMARY_DESCRIPTION", "LOCATION"]]

kradeze_filtr["DATE_OF_OCCURRENCE"] = pd.to_datetime(kradeze_filtr["DATE_OF_OCCURRENCE"])
kradeze_filtr = kradeze_filtr.sort_values("DATE_OF_OCCURRENCE")

kradeze_filtr["MONTH"] = kradeze_filtr["DATE_OF_OCCURRENCE"].dt.month
kradeze_filtr["YEAR"] = kradeze_filtr["DATE_OF_OCCURRENCE"].dt.year

kradeze_filtr["count"] = 1
print(kradeze_filtr.head())

#Nakonec jsme vybrala variantu 2, protože tam mám už začátek října
#kradeze_filtr_grouped1 = kradeze_filtr.groupby("MONTH")["count"].sum()

kradeze_filtr_grouped2 = kradeze_filtr.groupby(["YEAR","MONTH"])["count"].sum()
print(kradeze_filtr_grouped2)

#kradeze_filtr_grouped1.plot(kind="bar",x="MONTH", ylabel="počet krádeží", color="blue", title="Sezónnost v krádežích", legend=False)
#plt.show()

kradeze_filtr_grouped2.plot(kind="bar", y="count", ylabel="počet krádeží", color="blue", title="Sezónnost v krádežích", legend=False)
plt.show()

print("Nejvíce krádeží bylo v září (910). Syn má hypotézu,že je to to asi proto, že začala škola. :-)")