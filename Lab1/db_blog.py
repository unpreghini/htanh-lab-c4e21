# 1. Connect to database
from pymongo import MongoClient
# from bson.objectid import ObjectId

uri = "mongodb://admin:Hanoi1@ds029224.mlab.com:29224/c4e21"
client = MongoClient(uri)

db = client.get_database()

# 2. Select collection

posts = db['posts']

# 3. Create document

post = {
    "title": "Hôm nay là thứ 3",
    "content": "Còn 3 hôm nữa mới là cuối tuần",
}

# 4. Insert document

# posts.insert_one(post)
# print("Done")

post_list = posts.find()
# for post in post_list:
#     print(post)
cond = {
    "title": {"$regex": "hôm nay", "$options": "i"}
}
post = posts.find_one(cond)
print(post)
