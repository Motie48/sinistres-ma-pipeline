import pandas as pd

# ── Lecture
df = pd.read_csv('data/accidents_maroc.csv')

# ── 1. Typer la date correctement
df['date'] = pd.to_datetime(df['date'])

# ── 2. Extraire des colonnes temporelles (utiles pour dim_date)
df['annee']    = df['date'].dt.year
df['mois']     = df['date'].dt.month
df['mois_nom'] = df['date'].dt.strftime('%B')
df['trimestre']= df['date'].dt.quarter
df['jour_sem'] = df['date'].dt.day_name()

# ── 3. Créer un score de gravité numérique (utile pour les agrégations)
gravite_map = {'Léger': 1, 'Grave': 2, 'Mortel': 3}
df['gravite_score'] = df['gravite'].map(gravite_map)

# ── 4. Colonne heure en entier (pour analyses peak hours)
df['heure_int'] = df['heure'].str.split(':').str[0].astype(int)

# ── 5. Vérification finale
print("=== SHAPE APRÈS TRANSFORM ===")
print(f"{df.shape[0]} lignes, {df.shape[1]} colonnes")

print("\n=== NOUVELLES COLONNES ===")
print(df[['date','annee','mois','trimestre','jour_sem','gravite','gravite_score','heure_int']].head(5))

print("\n=== TYPES FINAUX ===")
print(df.dtypes)

# ── Sauvegarde
df.to_csv('data/accidents_transformed.csv', index=False)
print("\n✅ Fichier transformé sauvegardé : data/accidents_transformed.csv")