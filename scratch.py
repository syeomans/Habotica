from user import user
import group

# print("Creating user")
aalice = user("964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "1d8c9062-f5aa-40d4-85ee-32e7f58171b7")
# lauren = user('b9cd2456-61be-487c-8ec7-918a9ae87a78', '64493f4e-0c2d-4e54-9f03-c2183f25acfa')
sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")

email = 'o6647754@nwytg.net'
emails = [{'email': 'user1email@example.com'}, {'email': 'user2@email.com', 'name': 'user2'}]
userIds = [sam.userId, aalice.userId]
response = group.invite(sam.credentials, 'habitrpg', emails=emails)
print(response)

