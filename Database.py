from pymongo import MongoClient
from config import username, password

def get_database():
  CONNECTION_STRING = f"mongodb+srv://{username}:{password}@cluster0.oaste.mongodb.net/NEWSAGGREGATOR?retryWrites=true&w=majority"
  
  client = MongoClient(CONNECTION_STRING)
  print("Connecting with MongoDb") 
  return client["NEWSAGGREGATOR"]

  
db = get_database()