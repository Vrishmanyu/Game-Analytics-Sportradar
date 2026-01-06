import json
import pandas as pd
from sqlalchemy import create_engine

# ---------------- DATABASE CONNECTION ----------------
engine = create_engine(
    "postgresql+psycopg2://postgres:Vrishmanyu%4001@localhost:5432/tennis_analytics"
)

print("PostgreSQL connected successfully")

# ---------------- LOAD JSON ----------------
with open("data/complexes_raw.json", "r", encoding="utf-8") as f:
    complexes_json = json.load(f)

# ---------------- PREPARE VENUES ----------------
venues_rows = []

for complex_item in complexes_json["complexes"]:
    complex_id = complex_item.get("id")

    for venue in complex_item.get("venues", []):
        venues_rows.append({
            "venue_id": venue.get("id"),
            "venue_name": venue.get("name"),
            "complex_id": complex_id
        })

df_venues = pd.DataFrame(venues_rows)

# ---------------- INSERT INTO DB ----------------
df_venues.to_sql(
    "venues",
    engine,
    if_exists="append",
    index=False
)

print("Venues inserted:", len(df_venues))
