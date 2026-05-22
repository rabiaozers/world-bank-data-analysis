SELECT year, indicator_name, value
FROM world_bank_data
WHERE country_code = 'TUR'
ORDER BY indicator_name, year;