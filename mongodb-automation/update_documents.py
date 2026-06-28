from pymongo import MongoClient

client = MongoClient("mongodb+srv://nydile12:nydile1234@cluster0.lgu3gt4.mongodb.net/?appName=Cluster0")

db = client['devops_db']
collection = db['users']

result = collection.update_one(
    {"name": "Nydile"},
    {"$set": {"role": "Senior DevOps Engineer",
               "experience": 4}}
)
print(f"Updated {result.modified_count} document")

result = collection.update_many(
    {"experience": {"$lt": 3}},
    {"$set": {"level": "Junior"}}
)
print(f"Updated {result.modified_count} documents")

print("\nAfter Update:")
for user in collection.find():
    print(f"  → {user['name']} - {user['role']} - {user.get('level','Senior')}")

client.close()
print("\nDone")