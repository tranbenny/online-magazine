from pymongo import MongoClient

class MongoConnection:

    def __init__(self):
        self.client = MongoClient()

    def setDatabase(self, dbName):
        self.dbName = dbName
        self.database = self.client[self.dbName]

    def setCollection(self, collectionName):
        self.collectionName = collectionName
        self.collection = self.database[self.collectionName]

    def getDatabase(self):
        if self.dbName is None:
            raise TypeError('Database name is not set')
        else:
            return self.dbName

    def getCollection(self):
        if self.collectionName is None:
            raise TypeError('Database name is not set')
        else:
            return self.collectionName

    # CRUD Operations
    def insertOne(self, value):
        posts = self.database.posts
        post_id = posts.insert(value).inserted_id
        return post_id

    def insertMany(self, values):
        posts = self.database.posts
        result = posts.insert_many(values)
        return result.inserted_ids

    def findOne(self, queryValues):
        post = self.database.posts.find_one(queryValues)
        return post

    def findMany(self, queryValues):
        posts = self.database.posts
        searchResults = []
        for post in posts.find(queryValues):
            searchResults.append(post)
        return searchResults