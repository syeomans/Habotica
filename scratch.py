from user import user
import challenge

# print("Creating user")
aalice = user("964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "1d8c9062-f5aa-40d4-85ee-32e7f58171b7")
# sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")
# print("done")

# testChallengeId = 'bcfbafae-86df-4f3a-ba7e-f2026fb9ead5'
# testChallengeData = challenge.getChallenge(aalice.credentials, testChallengeId)['data']
# testChallenge = challenge.challenge(testChallengeData, aalice.credentials)

# Woods and widgets id: f4f004ef-df81-421f-87eb-9f549b91a7e8
print(aalice.partyId)


# groupId = testChallenge.group['id']
# print(groupId)
# print(testChallenge.group)
# name = 'Python-generated challenge'
# shortName = 'Second python test'
# response = challenge.createChallenge(aalice.credentials, groupId, name, shortName)
# print(response)

