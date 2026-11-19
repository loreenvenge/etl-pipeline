import pandas as pd
import sqlite3

# 1. EXTRACT - Get raw data from source system
try:
    df = pd.read_csv("customers_raw.csv")
except:
    data = {
        'customer_id': [1, 2, 2, 3, 4, 5],
        'first_name': ['Tatenda', 'Rutendo', 'Rutendo', 'Farai', 'Chipo', 'Tawanda'],
        'last_name': ['Moyo', 'Chigumba', 'Chigumba', 'Dube', 'Ncube', 'Shumba'],
        'gender': ['M', 'F', 'F', 'M', 'F', 'M'],
        'phone': ['0771 234 567', '0772 345 678', '0772 345 678', '0733 456 789', '0784 567 890', '0712 678 901'],
        'account_no': ['1001', '1002', '1002', None, '1004', '1005'],
        'join_date': ['2023-01-15', '2023-02-20', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12']
    }
    df = pd.DataFrame(data)

print(f"Extracted {len(df)} raw records")

# 2. TRANSFORM - Clean the data
df = df.drop_duplicates()
df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female'})
df['phone'] = df['phone'].str.replace(" ", "")
df['join_date'] = pd.to_datetime(df['join_date'])
df = df.dropna(subset=['customer_id', 'account_no'])
df['full_name'] = df['first_name'] + " " + df['last_name']
df = df[['customer_id', 'full_name', 'gender', 'phone', 'account_no', 'join_date']]

print(f"Transformed to {len(df)} clean records")

# 3. LOAD - Put clean data into Data Warehouse
conn = sqlite3.connect("bank_warehouse.db")
df.to_sql("dim_customers", conn, if_exists="replace", index=False)
conn.close()

print(f"Loaded {len(df)} clean customers into bank_warehouse.db")
print(df.head())
