# import_employees.py
import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_full_system"]
col = db["employees"]

# Read CSV
df = pd.read_csv(r"C:\Users\cc\Downloads\inventory.employees (1).csv")

# Clean and import
records = df.to_dict("records")

# Remove _id field — MongoDB will generate new ones
for r in records:
    if "_id" in r:
        del r["_id"]

# Clear existing and insert fresh
col.delete_many({})
col.insert_many(records)

print(f" {len(records)} employees imported successfully!")