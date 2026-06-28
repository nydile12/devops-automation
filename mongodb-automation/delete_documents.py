from pymongo import MongoClient

client = MongoClient("mongodb+srv://nydile12:nydile1234@cluster0.lgu3gt4.mongodb.net/?appName=Cluster0")

db = client['devops_db']
collection = db['users']

print(f"Before delete: {collection.count_documents({})} documents")

result = collection.delete_one({"name": "User1"})
print(f"Deleted {result.deleted_count} document")

result = collection.delete_many({"level": "Junior"})
print(f"Deleted {result.deleted_count} documents")

print(f"After delete: {collection.count_documents({})} documents")

print("\nRemaining Users:")
for user in collection.find():
    print(f"  → {user['name']} - {user['role']}")

client.close()
print("\nDone!")