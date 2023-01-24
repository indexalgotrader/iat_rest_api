import pymongo
from pymongo.server_api import ServerApi

from helpers.environment_variables import *

iat_strats_mongo_client = pymongo.MongoClient(os.getenv('IAT_STRATS_MONGO_DB'), server_api=ServerApi('1'))
iat_strats_db = iat_strats_mongo_client["iat_strats"]
strategy_execution = iat_strats_db["strategy_execution"]
