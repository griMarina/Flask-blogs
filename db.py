from pymongo import MongoClient

def connect_to_mongo():
    try:
        CONNECT_STRING = 'mongodb+srv://Admin:mongoDb@cluster0.gqvoxyw.mongodb.net/?retryWrites=true&w=majority'
        connection = MongoClient(CONNECT_STRING)
        print('connection OK')
        # blogDB = connection['blogsDB']
        return connection['blogsDB']

    except Exception as e:
        raise e

def get_all_blogs():
    blogs_collection = db['blogs'] 

    blogs = len(list(blogs_collection.find()))

    if blogs == 0:
        all_blogs = [{'title': 'No document found!'}]
        return all_blogs

    else:
        all_blogs = blogs_collection.find()
        return all_blogs


db = connect_to_mongo()