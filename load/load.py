import pandas as pd
from sqlalchemy import create_engine

# ── Connexion SQLite (zéro config, fichier local)
engine = create_engine('sqlite:///data/sinistres_ma.db')

# ── Lecture des données transformées
df = pd.read_csv('data/accidents_transformed.csv')

# ── Chargement dans la table brute
df.to_sql('accidents_brut', engine, if_exists='replace', index=False)

print("✅ Données chargées dans SQLite")
print(f"   {len(df)} lignes insérées dans la table 'accidents_brut'")

# ── Vérification
df_check = pd.read_sql("SELECT COUNT(*) as total FROM accidents_brut", engine)
print(f"   Vérification DB : {df_check['total'][0]} lignes confirmées")