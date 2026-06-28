from pymongo import MongoClient

client = MongoClient("")
db = client['devops_db']
collection = db['users']

print("All users")
for user in collection.find():
    print(f" -> {user['name']} - {user['role']}")

print("\nFind One User:")
user = collection.find_one({"name": "Nydile"})
print(f"  → {user['name']} - {user['role']}")

print("\nUsers with experience > 2:")
for user in collection.find({"experience": {"$gt": 2}}):
    print(f"  → {user['name']} - {user['experience']} years")

client.close()
print("\nDone!")