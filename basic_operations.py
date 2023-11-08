from datetime import datetime
import os
# Import the `pprint` function to print nested data
from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient
import bson

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)
print('****')
# Get a reference to the 'sample_mflix' database:
db = client['sample_mflix']

# List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# Get a reference to the 'movies' collection:
movies = db['movies']

# Get the document with the title 'Blacksmith Scene':
pprint(movies.find_one({'title': 'The Great Train Robbery'}))

# Insert a document for the movie 'Parasite':
insert_result = movies.insert_one({
    "title": "Parasite",
    "year": 2020,
    "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. "
            "But their easy life gets complicated when their deception is threatened with exposure.",
    "released": datetime(2020, 2, 7, 0, 0, 0),
})

# Save the inserted_id of the document you just created:
parasite_id = insert_result.inserted_id
print("_id of inserted document: {parasite_id}".format(parasite_id=parasite_id))
# Look up the document you just created in the collection:
print(movies.find_one({'_id': bson.ObjectId(parasite_id)}))
