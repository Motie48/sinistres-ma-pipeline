import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+pg8000://postgres:admin123@localhost:5432/sinistres_ma"
)

# ── WF 1 : Classement des régions par accidents (RANK)
print("=== 1. CLASSEMENT RÉGIONS (RANK) ===")
q1 = """
SELECT r.region,
       COUNT(*) as nb_accidents,
       RANK() OVER (ORDER BY COUNT(*) DESC) as classement
FROM fait_accident f
JOIN dim_region r ON f.id_region = r.id_region
GROUP BY r.region
"""
print(pd.read_sql(q1, engine).to_string(index=False))

# ── WF 2 : Cumul mensuel des victimes (SUM OVER)
print("\n=== 2. CUMUL MENSUEL VICTIMES ===")
q2 = """
SELECT d.annee, d.mois,
       SUM(f.nb_victimes) as victimes_mois,
       SUM(SUM(f.nb_victimes)) OVER (
           PARTITION BY d.annee
           ORDER BY d.mois
       ) as cumul_annuel
FROM fait_accident f
JOIN dim_date d ON f.id_date = d.id_date
GROUP BY d.annee, d.mois
ORDER BY d.annee, d.mois
LIMIT 12
"""
print(pd.read_sql(q2, engine).to_string(index=False))

# ── WF 3 : Moyenne mobile accidents (AVG OVER)
print("\n=== 3. MOYENNE MOBILE PAR MOIS ===")
q3 = """
SELECT d.annee, d.mois,
       COUNT(*) as nb_accidents,
       ROUND(AVG(COUNT(*)) OVER (
           ORDER BY d.annee, d.mois
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 1) as moyenne_mobile_3mois
FROM fait_accident f
JOIN dim_date d ON f.id_date = d.id_date
GROUP BY d.annee, d.mois
ORDER BY d.annee, d.mois
LIMIT 12
"""
print(pd.read_sql(q3, engine).to_string(index=False))

print("\n✅ Window functions exécutées avec succès !")