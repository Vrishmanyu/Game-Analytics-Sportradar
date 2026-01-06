import streamlit as st
import pandas as pd
import psycopg2

# ---------------- DATABASE CONNECTION ----------------

conn = psycopg2.connect(
    host="localhost",
    database="tennis_analytics",
    user="postgres",
    password="Vrishmanyu@01"
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="Tennis Analytics Dashboard", layout="wide")
st.title("🎾 Tennis Analytics Dashboard")

# ---------------- KPI SECTION ----------------

col1, col2, col3, col4 = st.columns(4)

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM categories;")
col1.metric("Categories", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM competitions;")
col2.metric("Competitions", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM complexes;")
col3.metric("Complexes", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM venues;")
col4.metric("Venues", cur.fetchone()[0])

# ---------------- CATEGORY WISE COMPETITIONS ----------------

st.subheader("📊 Competitions by Category")

df_category = pd.read_sql("""
SELECT c.category_name, COUNT(*) AS total_competitions
FROM competitions co
JOIN categories c
ON co.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_competitions DESC;
""", conn)

st.dataframe(df_category)

# ---------------- MATCH TYPE DISTRIBUTION ----------------

st.subheader("🎯 Match Type Distribution")

df_type = pd.read_sql("""
SELECT type, COUNT(*) AS total
FROM competitions
GROUP BY type;
""", conn)

st.dataframe(df_type)

# ---------------- DOUBLES COMPETITIONS ----------------

st.subheader("🤝 Doubles Competitions")

df_doubles = pd.read_sql("""
SELECT competition_name
FROM competitions
WHERE type = 'doubles'
LIMIT 20;
""", conn)

st.dataframe(df_doubles)

# ---------------- VENUES PER COMPLEX ----------------

st.subheader("🏟️ Venues per Complex")

df_venues = pd.read_sql("""
SELECT c.complex_name, COUNT(v.venue_id) AS venue_count
FROM venues v
JOIN complexes c
ON v.complex_id = c.complex_id
GROUP BY c.complex_name
ORDER BY venue_count DESC
LIMIT 15;
""", conn)

st.dataframe(df_venues)

conn.close()
