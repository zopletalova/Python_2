import pandas as pd
import requests

def check_url(radek):
  if isinstance(radek.image_src, str) == False:
    src = str(radek.image_src)
    image_err = radek.title+" : "+src
  elif radek.image_src.startswith("https://zoopraha.cz/images/") == False:
    image_err = radek.title+" : "+radek.image_src
  elif (radek.image_src.endswith("jpg")|radek.image_src.endswith("JPG")) == False:
    image_err = radek.title+" : "+radek.image_src
  else:
    image_err = ""
  return image_err


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pd.read_csv("lexikon-zvirat.csv", sep=";")
# Alternativa k nastavení indexu
# lexikon = pd.read_csv("lexikon-zvirat.csv", sep=";", index_col="id")

print(lexikon.shape)

# Smažu sloupec se všemi nulami a řádek se všemi nulami
lexikon = lexikon.dropna(axis=1, how="all")
lexikon = lexikon.dropna(how="all")
# Vidím, že se skutečně snížil počet sloupců i řádků o jeden
print(lexikon.shape)

# Nastavení indexu
lexikon = lexikon.set_index("id")

print(lexikon.columns)
print(lexikon.head())

print()
print("Vypisuji seznam zvířat s neplatnou url obrázku - ta je uvedena za dvojtečkou:")
count = 0
for radek in lexikon.itertuples():
    image_err = check_url(radek)
    if image_err != "":
        count = count+1
        print(image_err)
print()
print(f"Počet zvířat se špatnou url obrázku je {count}")