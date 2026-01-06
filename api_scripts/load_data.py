import json
import pandas as pd
from sqlalchemy import create_engine
import os

# ---------------- DATABASE CONNECTION ----------------

engine = create_engine(
    "postgresql+psycopg2://postgres:Vrishmanyu%4001@localhost:5432/tennis_analytics"
)

print("PostgreSQL connected successfully")

# ---------------- FILE PATH (FIXED) ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "competitions_raw.json")

# ---------------- LOAD JSON ----------------

with open(DATA_PATH, "r", encoding="utf-8") as f:
    competitions_json = json.load(f)

from sqlalchemy import text

# ---------------- INSERT CATEGORIES (SAFE) ----------------

inserted_count = 0

with engine.begin() as conn:
    for comp in competitions_json["competitions"]:
        category = comp.get("category")
        if category:
            conn.execute(
                text("""
                    INSERT INTO categories (category_id, category_name)
                    VALUES (:id, :name)
                    ON CONFLICT (category_id) DO NOTHING
                """),
                {"id": category["id"], "name": category["name"]}
            )
            inserted_count += 1

print("Categories processed:", inserted_count)


# ---------------- INSERT COMPETITIONS (SAFE) ----------------

from sqlalchemy import text

inserted_competitions = 0

with engine.begin() as conn:
    for comp in competitions_json["competitions"]:
        conn.execute(
            text("""
                INSERT INTO competitions (
                    competition_id,
                    competition_name,
                    parent_id,
                    type,
                    gender,
                    category_id
                )
                VALUES (
                    :competition_id,
                    :competition_name,
                    :parent_id,
                    :type,
                    :gender,
                    :category_id
                )
                ON CONFLICT (competition_id) DO NOTHING
            """),
            {
                "competition_id": comp.get("id"),
                "competition_name": comp.get("name"),
                "parent_id": comp.get("parent_id"),
                "type": comp.get("type"),
                "gender": comp.get("gender"),
                "category_id": comp.get("category", {}).get("id")
            }
        )
        inserted_competitions += 1

print("Competitions processed:", inserted_competitions)
