CREATE OR REPLACE VIEW v_macroeconomic_matrix AS
SELECT 
    country_name,
    country_code,
    year,
    -- İçinde GDP geçen değerlerin en büyüğünü al
    MAX(CASE WHEN LOWER(indicator_name) LIKE '%gdp per capita%' THEN ROUND(value, 2) END) AS gdp_per_capita,
    -- İçinde internet geçen değerlerin en büyüğünü al
    MAX(CASE WHEN LOWER(indicator_name) LIKE '%internet%' THEN ROUND(value, 2) END) AS internet_usage_pct,
    -- İçinde unemployment geçen değerlerin en büyüğünü al
    MAX(CASE WHEN LOWER(indicator_name) LIKE '%unemployment%' THEN ROUND(value, 2) END) AS unemployment_rate,
    -- İçinde education geçen değerlerin en büyüğünü al
    MAX(CASE WHEN LOWER(indicator_name) LIKE '%education expenditure%' OR LOWER(indicator_name) LIKE '%expenditure on education%' THEN ROUND(value, 2) END) AS edu_expenditure_pct,
    -- İçinde life expectancy geçen değerlerin en büyüğünü al
    MAX(CASE WHEN LOWER(indicator_name) LIKE '%life expectancy%' THEN ROUND(value, 2) END) AS life_expectancy
FROM world_bank_data
WHERE year BETWEEN 2010 AND 2022
GROUP BY country_name, country_code, year;