# 🚦 Pipeline Analytics — Accidents de Circulation Maroc

Pipeline ETL complet sur données d'accidents routiers au Maroc,
avec modélisation dimensionnelle et requêtes analytiques BI.

## 🏗️ Architecture
CSV (Open Data Maroc)
↓ Extract
pandas (nettoyage + enrichissement)
↓ Transform
PostgreSQL (modèle étoile)
↓ Load
Requêtes analytiques SQL + Window Functions

## ⭐ Modèle étoile
      dim_date
         |
dim_region — fait_accident — dim_accident

| Table | Description |
|-------|-------------|
| fait_accident | 5 000 accidents (mesures) |
| dim_date | 1 250 dates enrichies |
| dim_region | 7 régions du Maroc |
| dim_accident | 50 combinaisons type/cause/milieu |

## 📁 Structure
sinistres_ma_pipeline/
├── extract/   → génération et lecture des données
├── transform/ → nettoyage et enrichissement pandas
├── load/      → chargement SQLite + PostgreSQL
├── sql/       → modèle étoile + requêtes analytiques
└── data/      → fichiers CSV et DB (gitignored)

## 🚀 Lancer le pipeline

```bash
pip install pandas sqlalchemy pg8000
python extract/generate_data.py
python transform/transform.py
python load/load.py
python sql/modele_etoile.py
python sql/requetes_analytiques.py
python sql/window_functions.py
```

## 🔍 Requêtes analytiques

- Top régions par nombre d'accidents
- Évolution annuelle des sinistres
- Causes des accidents mortels
- Comparaison Urbain vs Rural
- Mois les plus accidentogènes

## 🔥 Window Functions SQL

- `RANK()` — classement des régions par sinistralité
- `SUM() OVER` — cumul mensuel des victimes par année
- `AVG() OVER ROWS` — moyenne mobile 3 mois des accidents

## 🛠️ Stack technique

`Python` `pandas` `SQLAlchemy` `PostgreSQL` `SQLite` `SQL` `Git`