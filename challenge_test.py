import habotica
import challenge

aalice = {'x-api-user': "964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", 'x-api-key': "1d8c9062-f5aa-40d4-85ee-32e7f58171b7"}
sam = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}
# print(habotica.postChat(aalice, "Test"))

party = str(habotica.getUserProfile(aalice)['party']['_id'])
print(party)
response = challenge.createChallenge(aalice, "964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "AALiCE's Challenge", "AALiCE's Challenge", summary = "I learned how to create a challenge! ")

print(response)