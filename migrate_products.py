# migrate_products.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Source — old database
old_db = client["inventory_ai"]
old_products = list(old_db["products"].find())

# Destination — new database
new_db = client["inventory_full_system"]
new_col = new_db["products"]

# Clear existing and migrate
new_col.delete_many({})

for p in old_products:
    new_product = {
        "product_id": p.get("id", ""),
        "name": p.get("name", ""),
        "category_id": p.get("category", ""),
        "current_stock": p.get("stock", 0),
        "selling_price": p.get("price", 0),
        "reorder_point": p.get("reorder", 0),
        "supplier_id": p.get("supplier", ""),
    }
    new_col.insert_one(new_product)

print(f" {len(old_products)} products migrated successfully!")