import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+pg8000://postgres:admin123@localhost:5432/sinistres_ma"
)

sqlite = create_engine('sqlite:///data/sinistres_ma.db')
dim_date     = pd.read_sql("SELECT * FROM dim_date", sqlite)
dim_region   = pd.read_sql("SELECT * FROM dim_region", sqlite)
dim_accident = pd.read_sql("SELECT * FROM dim_accident", sqlite)
fait         = pd.read_sql("SELECT * FROM fait_accident", sqlite)

dim_date.to_sql('dim_date', engine, if_exists='replace', index=False)
print(f"✅ dim_date : {len(dim_date)} lignes")
dim_region.to_sql('dim_region', engine, if_exists='replace', index=False)
print(f"✅ dim_region : {len(dim_region)} lignes")
dim_accident.to_sql('dim_accident', engine, if_exists='replace', index=False)
print(f"✅ dim_accident : {len(dim_accident)} lignes")
fait.to_sql('fait_accident', engine, if_exists='replace', index=False)
print(f"✅ fait_accident : {len(fait)} lignes")

print("\n🎯 Migration SQLite → PostgreSQL terminée !")