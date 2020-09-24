import pymongo

try:
    mongo_py = pymongo.MongoClient()

    db = mongo_py['six']
    collection = db['stu']

    one = {'name':'张三','age':'14'}

    collection.insert_one(one)
except Exception as e:
    print(e)
finally:
    mongo_py.close()
