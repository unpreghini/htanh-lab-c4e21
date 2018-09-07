from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

posts = db['posts']

post = {
    "title": "Unknown",
    "author": "You know who",
    "content": "The one who shall not be named"
}

posts.insert_one(post)
