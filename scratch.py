from user import user
import pprint
import task

#aalice = user("964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "1d8c9062-f5aa-40d4-85ee-32e7f58171b7")
sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")
print(sam.userV)

#response = sam.authenticatedProfile

# response = task.getTasks(sam.credentials)
# tasks = response['data']
# print(tasks[0].keys())
# print('')
# print(tasks[0]['type'])


# for task in tasks:
# 	print(task)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(response)