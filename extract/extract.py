import pandas as pd

# ── Lecture du CSV
df = pd.read_csv('data/accidents_maroc.csv')

# ── Exploration
print("=== SHAPE ===")
print(f"{df.shape[0]} lignes, {df.shape[1]} colonnes")

print("\n=== TYPES ===")
print(df.dtypes)

print("\n=== VALEURS MANQUANTES ===")
print(df.isnull().sum())

print("\n=== APERÇU ===")
print(df.head(5))

print("\n=== STATISTIQUES ===")
print(df.describe())

print("\n=== VALEURS UNIQUES PAR COLONNE ===")
for col in ['region', 'type_accident', 'gravite', 'milieu', 'cause']:
    print(f"{col} : {df[col].unique()}")