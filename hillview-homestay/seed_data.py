from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(
    os.getenv('MONGO_URI'),
    tlsAllowInvalidCertificates=True
)
db = client[os.getenv('DB_NAME')]

# Clear existing rooms
db.rooms.drop()
db.attractions.drop()

# Insert rooms
rooms = [
    {
        "name": "Hill View Room",
        "description": "Wake up to stunning views of the Western Ghats from your private room with modern amenities.",
        "price": 2500,
        "capacity": 2,
        "bed_type": "Double Bed",
        "image": "room1.jpg",
        "amenities": ["WiFi", "Hot Water",
                      "Hill View", "AC"]
    },
    {
        "name": "Forest Suite",
        "description": "Nestled among the trees, this suite offers a peaceful forest retreat with premium comforts.",
        "price": 3500,
        "capacity": 3,
        "bed_type": "King Bed",
        "image": "room2.jpg",
        "amenities": ["WiFi", "Hot Water",
                      "Forest View", "AC",
                      "Balcony"]
    },
    {
        "name": "Coffee Plantation Room",
        "description": "Overlooking the lush coffee estates, perfect for couples seeking a romantic getaway.",
        "price": 3000,
        "capacity": 2,
        "bed_type": "Queen Bed",
        "image": "room3.jpg",
        "amenities": ["WiFi", "Hot Water",
                      "Garden View", "AC"]
    },
    {
        "name": "Family Cottage",
        "description": "Spacious cottage perfect for families with separate living area and stunning mountain views.",
        "price": 5000,
        "capacity": 6,
        "bed_type": "2 Double Beds",
        "image": "room4.jpg",
        "amenities": ["WiFi", "Hot Water",
                      "Mountain View", "AC",
                      "Living Room"]
    }
]

db.rooms.insert_many(rooms)
print(f"✅ Inserted {len(rooms)} rooms")

# Insert attractions
attractions = [
    {
        "name": "Mullayanagiri Peak",
        "description": "Highest peak in Karnataka offering breathtaking views of the Western Ghats.",
        "distance": "20 km",
        "image": "attraction1.jpg"
    },
    {
        "name": "Baba Budangiri",
        "description": "Sacred hills with ancient caves and stunning natural beauty.",
        "distance": "25 km",
        "image": "attraction2.jpg"
    },
    {
        "name": "Hebbe Falls",
        "description": "Beautiful two-tiered waterfall surrounded by lush greenery.",
        "distance": "35 km",
        "image": "attraction3.jpg"
    },
    {
        "name": "Coffee Museum",
        "description": "Learn about Chickmagalur's famous coffee heritage and history.",
        "distance": "5 km",
        "image": "attraction4.jpg"
    },
    {
        "name": "Kemmangundi",
        "description": "Hill station with rose gardens and panoramic mountain views.",
        "distance": "40 km",
        "image": "attraction5.jpg"
    }
]

db.attractions.insert_many(attractions)
print(f"✅ Inserted {len(attractions)} attractions")

print("\n✅ Seed data inserted successfully!")
client.close()