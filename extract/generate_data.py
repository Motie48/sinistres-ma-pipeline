import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000

df = pd.DataFrame({
    'date': pd.date_range('2020-01-01', periods=n, freq='6h').strftime('%Y-%m-%d'),
    'heure': pd.date_range('2020-01-01', periods=n, freq='6h').strftime('%H:%M'),
    'region': np.random.choice(['Casablanca-Settat','Rabat-Salé','Marrakech-Safi',
                                 'Fès-Meknès','Tanger-Tétouan','Souss-Massa','Oriental'], n),
    'type_accident': np.random.choice(['Collision frontale','Dérapage',
                                        'Renversement','Choc obstacle','Collision arrière'], n),
    'gravite': np.random.choice(['Léger','Grave','Mortel'], n, p=[0.6, 0.3, 0.1]),
    'nb_victimes': np.random.randint(1, 8, n),
    'nb_vehicules': np.random.randint(1, 4, n),
    'milieu': np.random.choice(['Urbain','Rural'], n, p=[0.55, 0.45]),
    'cause': np.random.choice(['Excès de vitesse','Alcool','Téléphone',
                                'Fatigue','Priorité non respectée'], n),
})

df.to_csv('data/accidents_maroc.csv', index=False)
print(f"✅ Dataset créé : {len(df)} lignes")
print(df.head(3))
print(f"\nColonnes : {list(df.columns)}")