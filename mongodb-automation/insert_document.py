from pymongo import MongoClient

client = MongoClient("")
db = client['devops_db']
collection = db['users']

user = {
    "name": "Nydile",
    "role": "DevOps Engineer",
    "skills": ["Python", "MongoDB", "AWS"],
    "experience": 3
}

result = collection.insert_one(user)
print(f"Inserted document ID: {result.inserted_id}")

users = [
    {"name": "User1", "role": "Developer", "experience": 2},
    {"name": "User2", "role": "SRE", "experience": 4},
    {"name": "User3", "role": "CloudOps", "experience": 1}
]

result = collection.insert_many(users)
print(f"Inserted {len(result.inserted_ids)} documents")

client.close()