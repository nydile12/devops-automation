from pymongo import MongoClient

client = MongoClient("")
db = client['devops_db']
collection = db['users']

print("Connected to MongoDB Atlas!")
print(f"Database: {db.name}")
print(f"Collection: {collection.name}")

client.close()
print("Connection closed!")