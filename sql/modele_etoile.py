import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///data/sinistres_ma.db')
df = pd.read_csv('data/accidents_transformed.csv')

with engine.connect() as conn:

    # ── DIM_DATE
    dim_date = df[['date','annee','mois','mois_nom','trimestre','jour_sem']].drop_duplicates()
    dim_date = dim_date.reset_index(drop=True)
    dim_date.insert(0, 'id_date', dim_date.index + 1)
    dim_date.to_sql('dim_date', engine, if_exists='replace', index=False)
    print(f"✅ dim_date : {len(dim_date)} lignes")

    # ── DIM_REGION
    dim_region = df[['region']].drop_duplicates().reset_index(drop=True)
    dim_region.insert(0, 'id_region', dim_region.index + 1)
    dim_region.to_sql('dim_region', engine, if_exists='replace', index=False)
    print(f"✅ dim_region : {len(dim_region)} lignes")

    # ── DIM_ACCIDENT
    dim_accident = df[['type_accident','cause','milieu']].drop_duplicates().reset_index(drop=True)
    dim_accident.insert(0, 'id_accident', dim_accident.index + 1)
    dim_accident.to_sql('dim_accident', engine, if_exists='replace', index=False)
    print(f"✅ dim_accident : {len(dim_accident)} lignes")

    # ── FAIT_ACCIDENT (table centrale)
    fait = df.merge(dim_date, on=['date','annee','mois','mois_nom','trimestre','jour_sem']) \
             .merge(dim_region, on='region') \
             .merge(dim_accident, on=['type_accident','cause','milieu'])

    fait_final = fait[['id_date','id_region','id_accident',
                        'nb_victimes','nb_vehicules','gravite_score']].copy()
    fait_final.insert(0, 'id_fait', range(1, len(fait_final)+1))
    fait_final.to_sql('fait_accident', engine, if_exists='replace', index=False)
    print(f"✅ fait_accident : {len(fait_final)} lignes")

    print("\n=== MODÈLE ÉTOILE CRÉÉ ===")
    print("fait_accident (centrale)")
    print("  ├── dim_date")
    print("  ├── dim_region")
    print("  └── dim_accident")