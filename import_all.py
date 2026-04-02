import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory"]

files = {
    "categories": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/200_unique_categories.csv",
    "counters": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.counters.csv",
    "customers": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.customers.csv",
    "invoices": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.invoices.csv",
    "products": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.products.csv",
    "purchase_orders": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.purchase_orders.csv",
    "sales": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.sales.csv",
    "suppliers": "https://raw.githubusercontent.com/kumarAnuragIITP/InventoryApp/main/inventory%20database/inventory.suppliers.csv",
}

for collection_name, url in files.items():
    try:
        # Read CSV — convert ALL columns to string to avoid int overflow
        df = pd.read_csv(url, dtype=str)
        records = df.to_dict("records")
        db[collection_name].delete_many({})
        db[collection_name].insert_many(records)
        print(f" {collection_name} — {len(records)} records imported")
    except Exception as ex:
        print(f" {collection_name} failed: {ex}")

print("\n All collections imported successfully!")