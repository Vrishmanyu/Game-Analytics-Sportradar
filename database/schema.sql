
CREATE TABLE categories (
  category_id VARCHAR(50) PRIMARY KEY,
  category_name VARCHAR(100)
);

CREATE TABLE competitions (
  competition_id VARCHAR(50) PRIMARY KEY,
  competition_name VARCHAR(100),
  parent_id VARCHAR(50),
  type VARCHAR(20),
  gender VARCHAR(10),
  category_id VARCHAR(50)
);

CREATE TABLE complexes (
  complex_id VARCHAR(50) PRIMARY KEY,
  complex_name VARCHAR(100)
);

CREATE TABLE venues (
  venue_id VARCHAR(50) PRIMARY KEY,
  venue_name VARCHAR(100),
  city_name VARCHAR(100),
  country_name VARCHAR(100),
  country_code VARCHAR(10),
  timezone VARCHAR(100),
  complex_id VARCHAR(50)
);

CREATE TABLE competitors (
  competitor_id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(100),
  country VARCHAR(100),
  country_code VARCHAR(10),
  abbreviation VARCHAR(10)
);

CREATE TABLE competitor_rankings (
  id SERIAL PRIMARY KEY,
  rank INT,
  movement INT,
  points INT,
  competitions_played INT,
  competitor_id VARCHAR(50)
);
