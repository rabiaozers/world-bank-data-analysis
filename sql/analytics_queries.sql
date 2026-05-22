-- ====================================================================
-- PROJECT: World Bank Data Analysis (Focus: GDP per Capita)
-- PURPOSE: Macroeconomic Insights for European Countries
-- LANGUAGE: PostgreSQL
-- ====================================================================

-- 1. DATA OVERVIEW
-- A quick look at the freshly ingested GDP per capita data.
SELECT * FROM world_bank_data 
WHERE indicator_code LIKE '%NY.GDP.PCAP%' -- Standard World Bank code for GDP per capita
LIMIT 10;


-- 2. EUROPEAN ECONOMIC LEADERBOARD (Year 2022)
-- Ranking European countries based on their prosperity. 
-- Note: You can filter by specific European country codes (e.g., DEU, FRA, NLD, BEL)
SELECT country_name, country_code, year, ROUND(value, 2) AS gdp_per_capita_usd
FROM world_bank_data
WHERE year = 2022
  AND country_code IN ('DEU', 'FRA', 'NLD', 'BEL', 'ITA', 'ESP', 'SWE', 'AUT', 'CHE')
ORDER BY value DESC;


-- 3. INTERNSHIP TARGET BENCHMARKING (Germany vs. France vs. Netherlands)
-- Comparing the historical economic trajectory (2000-2023) of top staj/job destinations.
SELECT year, country_name, ROUND(value, 2) AS gdp_per_capita
FROM world_bank_data
WHERE country_code IN ('DEU', 'FRA', 'NLD')
ORDER BY country_name, year;


-- 4. ADVANCED: IDENTIFYING THE FASTEST GROWING EUROPEAN ECONOMY (CAGR)
-- Technical Showcase: Using window functions to find which country grew its GDP per capita 
-- the fastest between 2010 and 2022. (Guaranteed to impress recruiters!)
WITH gdp_milestones AS (
    SELECT 
        country_name,
        MAX(CASE WHEN year = 2010 THEN value END) AS gdp_2010,
        MAX(CASE WHEN year = 2022 THEN value END) AS gdp_2022
    FROM world_bank_data
    WHERE country_code IN ('DEU', 'FRA', 'NLD', 'BEL', 'ITA', 'ESP', 'SWE', 'TUR')
    GROUP BY country_name
)
SELECT 
    country_name,
    ROUND(gdp_2010, 2) AS gdp_2010,
    ROUND(gdp_2022, 2) AS gdp_2022,
    ROUND(((gdp_2022 - gdp_2010) / gdp_2010) * 100, 2) AS total_growth_percentage
FROM gdp_milestones
WHERE gdp_2010 IS NOT NULL AND gdp_2022 IS NOT NULL
ORDER BY total_growth_percentage DESC;
