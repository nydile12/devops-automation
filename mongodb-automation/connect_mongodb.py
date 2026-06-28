from pymongo import MongoClient

client = MongoClient("mongodb+srv://nydile12:nydile1234@cluster0.lgu3gt4.mongodb.net/?appName=Cluster0")
db = client['devops_db']
collection = db['users']

print("Connected to MongoDB Atlas!")
print(f"Database: {db.name}")
print(f"Collection: {collection.name}")

client.close()
print("Connection closed!")