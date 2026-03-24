from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["inventory_ai"]

product_collection = db["products"]
suppliers_collection = db["suppliers"]
catergories_collection = db["catergories"]
employees_collection = db["employees"]
users_collection = db["users"]
