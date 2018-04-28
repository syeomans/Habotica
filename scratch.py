import habotica
import challenge
import json
from classes import user
from task import *
from tag import *
from challenge import *

aalice = user("964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "1d8c9062-f5aa-40d4-85ee-32e7f58171b7")
sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")

tags = getTags(aalice.credentials)
tagId = tags['data'][0]['id']
print(tagId)
print("")

response = json.loads(createTask(aalice.credentials, "Create task: success!", "todo", priority="0.1"))
print(response)
print("")

taskId = response['data']['id']
print(taskId)
print("")

checklistResponse = addChecklist(aalice.credentials, taskId, "Create checklist item: success!")
checklistId = json.loads(checklistResponse)['data']['checklist'][0]['id']

tagResponse = addTag(aalice.credentials, taskId, tagId)
print(tagResponse)
print("")

print(deleteChecklist(aalice.credentials, taskId, checklistId))
print("")

print(taskId)
print(tagId)
print(removeTag(aalice.credentials, taskId, tagId))
print("")

print(deleteTask(aalice.credentials, taskId))
print("")