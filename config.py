import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    MONGO_DBNAME = os.environ.get("MONGODB_DBNAME")    
    MONGO_URI = f'mongodb://{os.environ.get("MONGODB_URI")}/{MONGO_DBNAME}'
    REMEMBER_COOKIE_NAME = "remember_me"
    

    