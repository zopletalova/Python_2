import pandas
import requests
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

data = pandas.read_csv("water-potability.csv")
print(data.shape)

print(data.head())

print(data.isna().sum())

data = data.dropna()
print(data.shape)

print(data["Potability"].value_counts(normalize=True))

X = data.drop(columns=["Potability"])
y = data["Potability"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(X_train)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(y_pred)

ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
    display_labels=clf.classes_,
    cmap=plt.cm.Blues,
)
plt.show()

#Teď změníme oproti lekci pohled na úspěšnost modelu
#Nechceme označovat nepitnou vodu jako pitnou

ks = [19, 21, 23, 25, 27, 31, 33, 35, 37, 39, 41, 43]
precision_scores = []

for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    precision_scores.append(precision_score(y_test, y_pred))

plt.plot(ks, precision_scores, color="Red")

plt.show()

clf = KNeighborsClassifier(n_neighbors=41)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

#Nová confusion matrix
ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
    display_labels=clf.classes_,
    cmap=plt.cm.Reds,
)
plt.show()

print()
print("Nakonec jsme se podívali na 41 sousedů a precision score je lepší než hodnota u f1 score:")
print(precision_score(y_test, y_pred))
print("Je to asi tím, že jsme se podívali na víc sousedů a taky nám vadí jen označení nepitné vody za pitnou. Naopak nám nevadí označení pitné vody za nepitnou")
print("(F1 score totiž spojuje obojí.)")
print()
print("Výpočet z matice: 1-(TP/(TP+FP)) = 1-(22/(22+54))")
print(1-(22/(22+54)))
