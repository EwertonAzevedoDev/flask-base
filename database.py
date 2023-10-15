from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
# Mongo scripts -- mover depois isso pro Config
user = os.environ.get("MONGODB_USER")
psw = os.environ.get("MONGODB_PSW")
uri = os.environ.get("MONGODB_URI")
dbname = os.environ.get("MONGODB_DBNAME")
#mongo_uri = f'mongodb://localhost:27017/politicas_publicas'
#mongo_uri = f'mongodb://{user}:{psw}@{uri}/{dbname}'
mongo_uri = f'mongodb://{uri}/{dbname}'
#mongo = MongoClient(mongo_uri, ssl=False, tlsAllowInvalidCertificates=True).politicas_publicas

