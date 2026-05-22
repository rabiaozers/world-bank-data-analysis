# 🌍 World Bank Macroeconomic Analysis & Visualization Project

This end-to-end data analytics project explores the relationship between economic growth (**GDP per Capita**), technological infrastructure (**Internet Access**), **Unemployment Rates**, **Education Expenditure**, and **Life Expectancy** across European countries between 2010 and 2022.

## 🚀 Project Architecture

### 📊 Phase 1: SQL Database Management (PostgreSQL)
* Designed a relational database schema optimized with indexes for high-speed querying.
* Transformed long-format World Bank data into a comprehensive macroeconomic analytics matrix using advanced **SQL Views** and **Conditional Aggregation**.

### 🐍 Phase 2: Python Exploratory Data Analysis (EDA)
* Automated data cleaning pipeline for 5 different World Bank indicators using `pandas`.
* Handled missing values (NaN) dynamically by applying country-specific historical mean imputation.
* Performed **Correlation Analysis** and generated visual insights using `seaborn` and `matplotlib`.

### 📉 Phase 3: Interactive Power BI Dashboard
* Connected Power BI directly to the local PostgreSQL instance to ingest live data views.
* Created a multi-page interactive reporting tool featuring:
  * **GDP Per Capita Trend Analysis** for target European internship hubs (Germany, France, Netherlands).
  * **Scatter Plots** visualizing technology adoption vs. economic variables with responsive country slicers.

---

## 📁 Repository Structure
```text
├── dataset/             # Cleaned World Bank CSV files
├── sql/                 # SQL DDL, indexing, and advanced analytical View queries
├── python/              # Python ETL and Exploratory Data Analysis scripts
├── visuals/             # Exported analytical plots (Correlation Heatmap, Trends)
└── World_Bank_Macroeconomic_Dashboard.pbix  # Master Power BI Dashboard File