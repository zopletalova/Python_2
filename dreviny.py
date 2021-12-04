import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect
import numpy
import seaborn as sns

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "zuzana.opletalova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
#PASSWORD = os.getenv("DB_PASSWORD")
PASSWORD = "Wx0=CN.K9Ts39j!M"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

inspector = inspect(engine)
print(inspector.get_table_names())

smrk = pd.read_sql("SELECT rok,hodnota from dreviny WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
smrk = smrk.sort_values("rok")
print(smrk)
#print(smrk.head())

smrk.plot(kind="bar",x="rok", y="hodnota", ylabel="těžba", color="purple", title="Těžba smrk a spol.", legend=False)
#ax.figure.savefig("plot.png")
plt.show()

#nahodila_tezba = pd.read_sql("SELECT hodnota, druhtez_cis, druhtez_kod, rok from dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
nahodila_tezba = pd.read_sql("SELECT * from dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
print(nahodila_tezba.head())
print(nahodila_tezba.columns)
nahodila_tezba = nahodila_tezba.sort_values("rok")
nahodila_tezba["prictez_txt"] = nahodila_tezba["prictez_txt"].replace("Exhalační příčina", "Exhalační")
nahodila_tezba["prictez_txt"] = nahodila_tezba["prictez_txt"].replace("Hmyzová příčina", "Hmyzová")
nahodila_tezba["prictez_txt"] = nahodila_tezba["prictez_txt"].replace("Příčina jiná než živelní, exhalační a hmyzová", "Jiná")
nahodila_tezba["prictez_txt"] = nahodila_tezba["prictez_txt"].replace("Živelní příčina", "Živelní")

nahodila_tezba_pivot = pd.pivot_table(nahodila_tezba, values="hodnota", index="rok", columns="prictez_txt", aggfunc=numpy.sum)
print(nahodila_tezba_pivot)
sns.heatmap(nahodila_tezba_pivot, annot=True, fmt=".1f", linewidths=.5, cmap="YlGnBu",cbar=False)
plt.show()

print()
print("Nárůst těžby v posledních letech způsobil hmyz - hmyzová příčina - plus částečně živelní.")
print("V roce 2007 narostla těžba znatelněji kvůli živelní příčině.")
