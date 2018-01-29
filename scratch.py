import habotica
import challenge
#import uuid

aalice = {'x-api-user': "964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", 'x-api-key': "1d8c9062-f5aa-40d4-85ee-32e7f58171b7"}
sam = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}
# print(habotica.postChat(aalice, "Test"))

party = str(habotica.getUserProfile(aalice)['party']['_id'])
#party2 = uuid.UUID(party)
print("")
#print(party2)
#print(str(type(party2)) +  "\n")
comrades = "u'2ff9822b-27f2-4774-98da-db349b57a38e'"
print(party)
print("")
print(habotica.getUserProfile(aalice)['party'])
print("")
#createChallenge(user, groupId, name, shortName, summary = "", description = "", prize = 0, official = False)
#response = challenge.createChallenge(sam, comrades, "AALiCE's Challenge", "AALiCE's Challenge", summary = "I learned how to create a challenge with the API!", description = "This will be taken down shortly. If you see this, please message me immediately.")

challengeId = "66d18e9b-5ebd-47fa-b279-941d840b7afe"
response = challenge.joinChallenge(aalice, challengeId)
print(response)