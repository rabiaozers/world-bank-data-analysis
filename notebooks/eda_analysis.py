import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

print("Connecting to PostgreSQL database...")


engine = create_engine('postgresql://postgres:0538@localhost:5432/world_bank_project')


query = "SELECT * FROM v_macroeconomic_matrix;"
df = pd.read_sql(query, engine)

print("Data successfully loaded into Python. Shape:", df.shape)


df['gdp_per_capita'] = df.groupby('country_code')['gdp_per_capita'].transform(lambda x: x.fillna(x.mean()))
df['internet_usage_pct'] = df.groupby('country_code')['internet_usage_pct'].transform(lambda x: x.fillna(x.mean()))
df['unemployment_rate'] = df.groupby('country_code')['unemployment_rate'].transform(lambda x: x.fillna(x.mean()))
df['edu_expenditure_pct'] = df.groupby('country_code')['edu_expenditure_pct'].transform(lambda x: x.fillna(x.mean()))
df['life_expectancy'] = df.groupby('country_code')['life_expectancy'].transform(lambda x: x.fillna(x.mean()))




numeric_cols = ['gdp_per_capita', 'internet_usage_pct', 'unemployment_rate', 'edu_expenditure_pct', 'life_expectancy']
corr_matrix = df[numeric_cols].corr()

print("\nCorrelation Matrix:")
print(corr_matrix)


plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Between Economic & Social Indicators', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visuals/correlation_heatmap.png')
plt.close()
print("Heatmap saved to 'visuals/correlation_heatmap.png'")


plt.figure(figsize=(12, 6))
target_countries = ['DEU', 'FRA', 'NLD', 'TUR'] 
df_filtered = df[df['country_code'].isin(target_countries)]

sns.lineplot(data=df_filtered, x='year', y='gdp_per_capita', hue='country_name', marker='o', linewidth=2.5)
plt.title('GDP per Capita Trend Over Years (2010-2022)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('GDP per Capita (Current USD)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Countries')
plt.tight_layout()
plt.savefig('visuals/gdp_trend_europe.png')
plt.close()
print(" GDP Trend plot saved to 'visuals/gdp_trend_europe.png'")

print("Phase 2 - Python EDA completed successfully!")