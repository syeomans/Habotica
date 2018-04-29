import habotica
import challenge
import json
from classes import user
from task import *
from tag import *
from challenge import *

aalice = user("964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "1d8c9062-f5aa-40d4-85ee-32e7f58171b7")
sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")

tasks = getTasks(aalice.credentials)
#print(tasks)
taskId = tasks['data'][4]['id']
creds = aalice.credentials
userId = aalice.userId
groupId = "party"
position = "1"
itemId = tasks['data'][4]['checklist'][0]['id']

response = updateTask(creds, taskId, text = "I changed this text!")
print(response)
# for task in tasks['data']:
# 	print(task['text'])