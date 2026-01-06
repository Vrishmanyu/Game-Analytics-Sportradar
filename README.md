# Game Analytics – Unlocking Tennis Data with Sportradar API

## 📌 Project Overview
This project focuses on collecting, storing, analyzing, and visualizing professional tennis data using the **Sportradar Tennis API**.  
The system demonstrates an end-to-end **data engineering and analytics pipeline**, starting from API data extraction to database storage and interactive dashboard visualization.

The project is developed as part of an academic **Major Project** and showcases real-world concepts such as API integration, ETL pipelines, relational database design, SQL analytics, and Streamlit dashboards.

---

## 🛠️ Technologies Used
- **Python**
- **Sportradar Tennis API**
- **PostgreSQL**
- **SQLAlchemy**
- **Pandas**
- **Streamlit**
- **SQL**

---

## 📁 Project Structure
```text
Game-Analytics-Sportradar/
│
├── api_scripts/
│   ├── fetch_api_data.py
│   ├── load_data.py
│   ├── load_complexes_venues.py
│   └── load_doubles_rankings.py
│
├── data/
│   ├── competitions_raw.json
│   ├── complexes_raw.json
│   └── doubles_rankings_raw.json
│
├── database/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── docs/
│   └── Tennis Analytics Dashboard.pdf
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## 🔄 Data Pipeline Explanation

### 1️⃣ Data Collection
- Tennis data such as competitions, categories, complexes, venues, and rankings is fetched using the Sportradar Tennis API.
- Raw API responses are stored in JSON format inside the `data/` folder.

### 2️⃣ Data Storage
- PostgreSQL is used as the relational database.
- Database tables are created using SQL scripts defined in `database/schema.sql`.

### 3️⃣ Data Processing (ETL)
- Python scripts in `api_scripts/` clean and load raw JSON data into PostgreSQL tables.
- Duplicate data handling is implemented using safe insertion techniques.
- The pipeline is re-runnable without data corruption.

### 4️⃣ Data Analysis
- Business and analytical questions are answered using SQL queries.
- All analytical queries are documented in `database/analysis_queries.sql`.

### 5️⃣ Data Visualization
- An interactive **Streamlit dashboard** displays insights related to:
  - Competitions and categories
  - Venues and complexes
  - Competitor rankings (subject to API availability)
- Dashboard snapshots are provided in PDF format inside the `docs/` folder.

---

## 📊 Dashboard
The Streamlit dashboard provides:
- Competition analytics by category and type
- Venue distribution by country and complex
- Ranking insights where API data is available

Dashboard preview is available here: 
docs/Tennis Analytics Dashboard.pdf

---

## ⚠️ API Limitation Note

The Sportradar trial API does not provide access to doubles rankings data.
This limitation is handled programmatically by:
- Detecting empty or invalid API responses
- Storing a documented placeholder JSON
- Allowing the ETL pipeline to complete without failure

This reflects real-world data engineering practices when working with restricted APIs.

---

## ▶️ How to Run the Project

### Install dependencies
pip install -r requirements.txt

### Run the Streamlit dashboard
python -m streamlit run streamlit_app/app.py

---

## 🎓 Academic Declaration

We hereby declare that this project titled **“Game Analytics – Unlocking Tennis Data with Sportradar API”** is an original work carried out by **Vrishmanyu Singh** and **Shreya Ghosal** as part of our academic curriculum.

All the work presented in this project has been completed by us under academic guidelines.  
The data used in this project has been sourced from publicly available APIs and is used strictly for learning, analysis, and academic demonstration purposes.

This project has not been submitted previously for any other degree, diploma, or certification.

---

## ✅ Conclusion

This project successfully demonstrates an end-to-end sports data analytics pipeline using real-world tennis data.  
By integrating API-based data collection, relational database design, SQL-based analysis, and interactive dashboard visualization, the project highlights practical data engineering and analytics concepts.

Through this work, **Vrishmanyu Singh** and **Shreya Ghosal** gained hands-on experience in handling API limitations, building re-runnable ETL pipelines, and presenting insights through a Streamlit dashboard.  
The project effectively bridges theoretical knowledge with real-world implementation and serves as a strong foundation for advanced analytics and data-driven decision-making.

