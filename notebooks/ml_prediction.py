import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("Starting Machine Learning Pipeline...")

# 1. Database Connection
engine = create_engine('postgresql://postgres:postgres@localhost:5432/world_bank_project')
query = "SELECT * FROM v_macroeconomic_matrix;"
df = pd.read_sql(query, engine)

# 2. Handle Missing Values (Historical Mean Imputation)
for col in ['gdp_per_capita', 'internet_usage_pct', 'unemployment_rate', 'edu_expenditure_pct', 'life_expectancy']:
    df[col] = df.groupby('country_code')[col].transform(lambda x: x.fillna(x.mean()))
df = df.dropna()

# 3. Feature & Target Selection
# X: Independent variables (Predictors)
features = ['internet_usage_pct', 'unemployment_rate', 'edu_expenditure_pct', 'life_expectancy']
X = df[features]

# y: Dependent variable (Target to predict -> GDP per Capita)
y = df['gdp_per_capita']

# 4. Train-Test Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Dataset split completed. Train rows: {len(X_train)}, Test rows: {len(X_test)}")

# 5. Model Initialization & Training
model = LinearRegression()
model.fit(X_train, y_train)

print("Model training completed successfully!")

# 6. Model Evaluation (Predicting on Test Data)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\n --- MODEL PERFORMANCE METRICS ---")
print(f" R2 Score (Coefficient of Determination): {r2:.4f} (Out of 1.00)")
print(f" Mean Absolute Error (MAE): ${mae:.2f} USD")

# 7. Simulation (Future Scenario Prediction)
# Let's simulate a European country profile:
sample_data = {
    'internet_usage_pct': [92.0],
    'unemployment_rate': [4.5],
    'edu_expenditure_pct': [5.8],
    'life_expectancy': [82.0]
}
sample_country = pd.DataFrame(sample_data)

predicted_gdp = model.predict(sample_country)


print("\n--- FUTURE SCENARIO PREDICTION ---")
print(f" Predicted GDP per Capita for this profile: ${predicted_gdp[0]:.2f} USD")