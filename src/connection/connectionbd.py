from pymongo import MongoClient
import certifi

whereCertifi  = certifi.where()

MONGO_URI = "mongodb+srv://Braikan:casillas2604@cluster0.py8on.mongodb.net/?retryWrites=true&w=majority"


def bdConnect():

    try:
        client = MongoClient(MONGO_URI,tlsCAFile =whereCertifi)
        db = client["MiprimerMongo"]
        return db	
    except ConnectionError:
        print("Could not connect to MongoDB")
     
    return db
