from os import environ
from pymongo import MongoClient
import environ

def get_db():
    
    env = environ.Env(
        DB_USER=(str, ""),
        DB_PASS=(str, "")
    )

    environ.Env.read_env()

    DB_USER = env('DB_USER')
    DB_PASS = env('DB_PASS')

    client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@example-users.tmf25.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")    

    return client
