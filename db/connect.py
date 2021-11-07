import os


from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv



load_dotenv(find_dotenv())

DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")
DB_HOST = os.getenv("DB_HOST")

def database():
	return MongoClient(f'mongodb+srv://{DB_USER}:{DB_PASSWD}@{DB_HOST}/myFirstDatabase?retryWrites=true&w=majority')
		