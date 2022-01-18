# import pandas as pd

# leggi da file .csv
# wine_measurements= pd.read_csv("winequality-red.csv")

# stampa le prime e ultime 5 righe
# print(wine_measurements.head())
# print(wine_measurements.tail())

# stampa le prime e ultime 10 righe
# print(wine_measurements.head(10))
# print(wine_measurements.tail(10))

import pandas as pd

wine_measurements = pd.read_csv("winequality-red.csv")
# stampa il numero di righe e colonne
# print(wine_measurements.shape)
# stampa le informazioni sul dataframe (colonne, tipo di dato, dimensione, ecc.)
print(wine_measurements.info())
# stampa informazioni sui tipi di dato di ogni colonna
# print(wine_measurements.dtypes())
# stampa una serie di statistiche sui dati di ogni colonna
print(wine_measurements.describe())
# stampa una descrizione della singola colonna specificata
print(wine_measurements["fixed_acidity"].describe())
# stampa la media
print(wine_measurements.mean())
# stampa la media di una singola colonna
print(wine_measurements["fixed_acidity"].mean())

# restituisce la colonna "citric_acid"
print(wine_measurements["citric_acid"])
# restituisce le righe tra la numero 10 e la numero 20
print(wine_measurements.loc[10:20])
# print(wine_measurements.iloc[10:20])
# restituisce la seconda, la quinta e l'ottava riga
# print(wine_measurements.loc[[1, 4, 7]])
print(wine_measurements.iloc[[1, 4, 7]])
# restituisce la riga 10, 12 e 14 delle colonne specificate
print(wine_measurements.loc[[10, 12, 14], ["citric_acid", "pH", "quality"]])

# esempio senza header
wine_df_no_header = pd.read_csv("winequality-red.csv", header=None)
print(wine_df_no_header.shape)
# stampa la riga 10, 12 e 14 delle colonne 2, 3 e 4
print(wine_df_no_header.loc[[10, 12, 14], [2, 3, 4]])

# legge solo le prime 100 righe del file
wine_df_100= pd.read_csv("winequality-red.csv", nrows=100)

# salta le righe e prende solo dalla 1500esima in poi
wine_df_skip = pd.read_csv("winequality-red.csv", skiprows=1500)
print(wine_df_skip.shape)

# wine_measurements.loc[:, ["pH"]].plot()
# wine_measurements.loc[0:10, ["pH", "alcohol"]].plot()

print(wine_measurements.loc[1:4, ["pH", "alcohol"]])

