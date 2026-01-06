
from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.sequence_bot
prefs = db.sequence_prefs

DEFAULT = {
    "use_episode": True,
    "use_season": False,
    "use_quality": False,
    "season": 1,
    "quality": "1080p"
}

def get_prefs(user_id):
    data = prefs.find_one({"_id": user_id})
    if not data:
        prefs.insert_one({"_id": user_id, **DEFAULT})
        return DEFAULT.copy()
    for k, v in DEFAULT.items():
        data.setdefault(k, v)
    return data

def toggle(user_id, key):
    data = get_prefs(user_id)
    data[key] = not data.get(key, False)
    prefs.update_one({"_id": user_id}, {"$set": {key: data[key]}})
    return data
