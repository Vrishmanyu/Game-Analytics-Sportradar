import json
import os
from sqlalchemy import create_engine, text

# ---------------- DATABASE CONNECTION ----------------

engine = create_engine(
    "postgresql+psycopg2://postgres:Vrishmanyu%4001@localhost:5432/tennis_analytics"
)

print("PostgreSQL connected successfully")

# ---------------- FILE PATH ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "doubles_rankings_raw.json")

# ---------------- LOAD JSON ----------------

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---------------- RECURSIVE SEARCH FOR RANKINGS ----------------

def find_competitor_rankings(obj):
    results = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "competitor_rankings" and isinstance(v, list):
                results.extend(v)
            else:
                results.extend(find_competitor_rankings(v))

    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_competitor_rankings(item))

    return results

rankings_list = find_competitor_rankings(data)

print(f"Total competitor rankings found: {len(rankings_list)}")

if not rankings_list:
    print("⚠️ No competitor rankings returned by Sportradar API.")
    print("⚠️ This is expected for limited/free API plans.")
    print("⚠️ Pipeline completed without inserting rankings.")
    exit(0)


# ---------------- INSERT COMPETITORS ----------------

with engine.begin() as conn:
    for item in rankings_list:
        competitor = item.get("competitor")
        if competitor:
            conn.execute(
                text("""
                    INSERT INTO competitors (
                        competitor_id,
                        name,
                        country,
                        country_code,
                        abbreviation
                    )
                    VALUES (
                        :id,
                        :name,
                        :country,
                        :country_code,
                        :abbr
                    )
                    ON CONFLICT (competitor_id) DO NOTHING
                """),
                {
                    "id": competitor.get("id"),
                    "name": competitor.get("name"),
                    "country": competitor.get("country"),
                    "country_code": competitor.get("country_code"),
                    "abbr": competitor.get("abbreviation")
                }
            )

print("Competitors processed")

# ---------------- INSERT RANKINGS ----------------

with engine.begin() as conn:
    for item in rankings_list:
        competitor = item.get("competitor")
        if competitor:
            conn.execute(
                text("""
                    INSERT INTO competitor_rankings (
                        competitor_id,
                        rank,
                        movement,
                        points,
                        competitions_played
                    )
                    VALUES (
                        :competitor_id,
                        :rank,
                        :movement,
                        :points,
                        :played
                    )
                    ON CONFLICT DO NOTHING
                """),
                {
                    "competitor_id": competitor.get("id"),
                    "rank": item.get("rank"),
                    "movement": item.get("movement"),
                    "points": item.get("points"),
                    "played": item.get("competitions_played")
                }
            )

print("Rankings processed successfully")
