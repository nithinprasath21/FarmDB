import pymongo

# Set up the MongoDB connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['farm_inventory_db']
