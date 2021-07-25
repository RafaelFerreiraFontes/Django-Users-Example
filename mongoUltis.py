from os import environ
from pymongo import MongoClient
import environ

def get_db():
    
    env = environ.Env(
        DB_USER=(str, ""),
        DB_PASS=(str, ""),
        DB_URI=(str,"")
    )

    environ.Env.read_env()

    DB_USER = env('DB_USER')
    DB_PASS = env('DB_PASS')
    DB_URI = env('DB_URI')

    client = MongoClient(DB_URI.format(DB_USER, DB_PASS))    

    return client
