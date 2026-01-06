import json
import pandas as pd
from sqlalchemy import create_engine, text
import os

# ---------------- DATABASE CONNECTION ----------------

engine = create_engine(
    "postgresql+psycopg2://postgres:Vrishmanyu%4001@localhost:5432/tennis_analytics"
)

print("PostgreSQL connected successfully")

# ---------------- FILE PATH ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "complexes_raw.json")

# ---------------- LOAD JSON ----------------

with open(DATA_PATH, "r", encoding="utf-8") as f:
    complexes_json = json.load(f)

# ---------------- INSERT COMPLEXES (SAFE) ----------------

with engine.begin() as conn:
    for complex_item in complexes_json["complexes"]:
        conn.execute(
            text("""
                INSERT INTO complexes (complex_id, complex_name)
                VALUES (:id, :name)
                ON CONFLICT (complex_id) DO NOTHING
            """),
            {
                "id": complex_item.get("id"),
                "name": complex_item.get("name")
            }
        )

print("Complexes processed")

# ---------------- INSERT VENUES (SAFE + FULL COLUMNS) ----------------

with engine.begin() as conn:
    for complex_item in complexes_json["complexes"]:
        complex_id = complex_item.get("id")

        for venue in complex_item.get("venues", []):
            conn.execute(
                text("""
                    INSERT INTO venues (
                        venue_id,
                        venue_name,
                        city_name,
                        country_name,
                        country_code,
                        timezone,
                        complex_id
                    )
                    VALUES (
                        :venue_id,
                        :venue_name,
                        :city_name,
                        :country_name,
                        :country_code,
                        :timezone,
                        :complex_id
                    )
                    ON CONFLICT (venue_id) DO NOTHING
                """),
                {
                    "venue_id": venue.get("id"),
                    "venue_name": venue.get("name"),
                    "city_name": venue.get("city_name"),
                    "country_name": venue.get("country_name"),
                    "country_code": venue.get("country_code"),
                    "timezone": venue.get("timezone"),
                    "complex_id": complex_id
                }
            )

print("Venues processed")
