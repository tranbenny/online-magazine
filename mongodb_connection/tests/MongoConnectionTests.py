from django.test import TestCase
from OnlineMagazine.mongodb_connection import MongoConnection


class MongoDBConnectionTestCase(TestCase):
    def setUp(self):
        self.dbConnection = MongoConnection()

    def testDBConnection(self):
        sampleDatabase = 'movies'
        dbConnection.setDatabase(sampleDatabase)