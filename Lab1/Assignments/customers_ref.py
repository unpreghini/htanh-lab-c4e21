from pymongo import MongoClient
from matplotlib import pyplot

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(uri)
db = client.get_database()
customers = db['customers']

references = customers.aggregate([
    {'$group': {'_id': '$ref', 'count': {'$sum': 1}}}
])

names = []
count = []
for reference in list(references):
    print(reference['_id'], ':', reference['count'])
    names.append(reference['_id'])
    count.append(reference['count'])

pyplot.pie(count, labels=names, autopct='%.1f%%', shadow=True)
pyplot.title('Customers by Percentage of References')
pyplot.axis('equal')

pyplot.show()
