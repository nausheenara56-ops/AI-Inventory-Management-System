# migrate_to_inventory.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
old = client["inventory_full_system"]
new = client["inventory"]

# Migrate products
products = list(old["products"].find())
if products:
    new["products"].delete_many({})
    new["products"].insert_many(products)
    print(f"{len(products)} products migrated")

# Migrate users
users = list(old["users"].find())
if users:
    new["users"].delete_many({})
    new["users"].insert_many(users)
    print(f" {len(users)} users migrated")

# Migrate employees
employees = list(old["employees"].find())
if employees:
    new["employees"].delete_many({})
    new["employees"].insert_many(employees)
    print(f" {len(employees)} employees migrated")

print("Migration complete!")