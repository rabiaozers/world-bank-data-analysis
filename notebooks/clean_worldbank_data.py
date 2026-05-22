import pandas as pd
import os

files_to_process = {
    "gdp_per_capita_raw.csv": "gdp_per_capita_cleaned.csv",
    "internet_usage_raw.csv": "internet_usage_cleaned.csv",
    "unemployment_raw.csv": "unemployment_cleaned.csv",
    "education_expenditure_raw.csv": "education_expenditure_cleaned.csv",
    "life_expectancy_raw.csv": "life_expectancy_cleaned.csv"
}

columns_to_keep = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']

year_columns = [str(year) for year in range(2000, 2024)]

print("Data cleaning pipeline started...")

for raw_file, clean_file in files_to_process.items():
    raw_path = os.path.join("dataset", raw_file)
    clean_path = os.path.join("dataset", clean_file)
    
    if not os.path.exists(raw_path):
        print(
f"(Warning: {raw_file} not found in dataset folder. Skipping...")
        continue
        
    print(f"Processing: {raw_file}...")
    
   
    df = pd.read_csv(raw_path, skiprows=4)
    
    
    df = df[columns_to_keep + year_columns]
    
   
    df_long = df.melt(
        id_vars=columns_to_keep,
        value_vars=year_columns,
        var_name='year',
        value_name='value'
    )
    
    
    df_long['value'] = pd.to_numeric(df_long['value'], errors='coerce')
    
    
    df_long = df_long.dropna()
    
   
    df_long.columns = ['country_name', 'country_code', 'indicator_name', 'indicator_code', 'year', 'value']
    
    
    df_long.to_csv(clean_path, index=False)
    print(f"Saved successfully: {clean_file}")

print("All files processed and ready for SQL!")