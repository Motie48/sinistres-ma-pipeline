import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/sinistres_ma.db')

# ── REQ 1 : Accidents par région (classement)
print("=== 1. TOP RÉGIONS PAR NOMBRE D'ACCIDENTS ===")
q1 = """
SELECT r.region,
       COUNT(*) as nb_accidents,
       SUM(f.nb_victimes) as total_victimes,
       ROUND(AVG(f.gravite_score), 2) as gravite_moyenne
FROM fait_accident f
JOIN dim_region r ON f.id_region = r.id_region
GROUP BY r.region
ORDER BY nb_accidents DESC
"""
print(pd.read_sql(q1, engine).to_string(index=False))

# ── REQ 2 : Évolution annuelle
print("\n=== 2. ÉVOLUTION ANNUELLE DES ACCIDENTS ===")
q2 = """
SELECT d.annee,
       COUNT(*) as nb_accidents,
       SUM(f.nb_victimes) as total_victimes
FROM fait_accident f
JOIN dim_date d ON f.id_date = d.id_date
GROUP BY d.annee
ORDER BY d.annee
"""
print(pd.read_sql(q2, engine).to_string(index=False))

# ── REQ 3 : Accidents mortels par cause
print("\n=== 3. CAUSES DES ACCIDENTS MORTELS ===")
q3 = """
SELECT a.cause,
       COUNT(*) as nb_mortels
FROM fait_accident f
JOIN dim_accident a ON f.id_accident = a.id_accident
WHERE f.gravite_score = 3
GROUP BY a.cause
ORDER BY nb_mortels DESC
"""
print(pd.read_sql(q3, engine).to_string(index=False))

# ── REQ 4 : Urbain vs Rural
print("\n=== 4. COMPARAISON URBAIN VS RURAL ===")
q4 = """
SELECT a.milieu,
       COUNT(*) as nb_accidents,
       ROUND(AVG(f.nb_victimes), 2) as moy_victimes,
       ROUND(AVG(f.gravite_score), 2) as gravite_moy
FROM fait_accident f
JOIN dim_accident a ON f.id_accident = a.id_accident
GROUP BY a.milieu
"""
print(pd.read_sql(q4, engine).to_string(index=False))

# ── REQ 5 : Top mois accidentogènes
print("\n=== 5. MOIS LES PLUS ACCIDENTOGÈNES ===")
q5 = """
SELECT d.mois_nom, d.mois,
       COUNT(*) as nb_accidents,
       SUM(f.nb_victimes) as total_victimes
FROM fait_accident f
JOIN dim_date d ON f.id_date = d.id_date
GROUP BY d.mois, d.mois_nom
ORDER BY nb_accidents DESC
LIMIT 5
"""
print(pd.read_sql(q5, engine).to_string(index=False))

print("\n✅ 5 requêtes analytiques exécutées avec succès")