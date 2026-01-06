import json
import pandas as pd
from sqlalchemy import create_engine

# ------------------ DATABASE CONNECTION ------------------

engine = create_engine(
    "postgresql+psycopg2://postgres:Vrishmanyu%4001@localhost:5432/tennis_analytics"
)

print("PostgreSQL connected successfully")

# ------------------ LOAD JSON ------------------

with open("data/competitions_raw.json", "r") as f:
    competitions_json = json.load(f)

# ------------------ CATEGORIES (SKIPPED) ------------------

print("Categories already exist – skipping category insertion")

# ------------------ INSERT COMPETITIONS ------------------

competitions_rows = []

for comp in competitions_json["competitions"]:
    competitions_rows.append({
        "competition_id": comp.get("id"),
        "competition_name": comp.get("name"),
        "parent_id": comp.get("parent_id"),
        "type": comp.get("type"),
        "gender": comp.get("gender"),
        "category_id": comp.get("category", {}).get("id")
    })

df_competitions = pd.DataFrame(competitions_rows)

df_competitions.to_sql(
    "competitions",
    engine,
    if_exists="append",
    index=False
)

print("Competitions inserted:", len(df_competitions))
