# Bank Customer ETL Pipeline

Built an ETL pipeline in Python and SQL for a bank data warehouse.

### What it does:
- **Extract:** Pulls customer data from CSV source system
- **Transform:** Removes duplicates, fixes gender (M -> Male), cleans phone numbers, converts dates, removes missing account numbers
- **Load:** Loads clean data into SQLite Data Warehouse table `dim_customers`

### Tools Used:
Python, Pandas, SQL, SQLite

### How to Run:
python etl_pipeline.py
