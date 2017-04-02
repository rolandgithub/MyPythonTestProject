#import TinyDB
from tinydb import TinyDB, Query
import json

UserStoryDatabase = TinyDB('UserStoryDatabase.json')
#print(len(UserStoryDatabase))
#UserStoryDatabase.insert({"RestConnectionInfo":{"host": "localhost", "port":"8001"}})

#Filling userStoryData
userStoryData = {}



TableUserStoryDataSelfscannerXamarin = UserStoryDatabase.table("TBL_UserStoryDataSelfscannerXamarin")
TableUserStoryDataSelfscannerXamarin.insert({"UserStoryId": "TC001","RestConnectionInfo":{"host": "localhost", "port":"8001"}})
TableUserStoryDataSelfscannerXamarin.all()
MyUserStory = Query()
result = TableUserStoryDataSelfscannerXamarin.get(MyUserStory.UserStoryId == 'TC001')
print(result)

#userStoryData = {}



