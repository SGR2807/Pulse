from pymongo import MongoClient
from bson.objectid import ObjectId

class DataService:
    def __init__(self):
        self.client = MongoClient('xxxxx')
        self.db = self.client['pulse_db']
        self.collection = self.db['pulse_data']

    def get_data(self):
        data = self.collection.find_one()
        if not data:
            # Create default data if not exists
            default_data = {
                "lcCount": 3,
                "lcVisible": True,
                "streak": 0,
                "bestStreak": 0,
                "lastSprintDate": "",
                "lastStreakDate": "",
                "lc": [],
                "repos": [],
                "companies": [],
                "skills": [],
                "ex": [False],
                "food": [False, False, False],
                "sleep": [False]
            }
            self.collection.insert_one(default_data)
            data = default_data
        
        # Convert ObjectId to string for JSON serialization
        if '_id' in data:
            data['_id'] = str(data['_id'])
        return data

    def save_data(self, data):
        # Remove _id from data if present to avoid immutable field error on update
        if '_id' in data:
            del data['_id']
            
        # Update the single document (upsert=True ensures it's created if missing)
        self.collection.find_one_and_update(
            {},
            {"$set": data},
            upsert=True,
            return_document=True
        )
        return {"status": "success"}