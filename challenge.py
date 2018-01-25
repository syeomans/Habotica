from habotica import getUrl
from habotica import postUrl
from habotica import putUrl
from habotica import deleteUrl

def createChallenge(user, groupId, name, shortName, summary = "", description = "", prize = 0):
	"""
	Creates a challenge. Cannot create associated tasks with this route. See createChallengeTasks.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	groupId: The id of the group to which the challenge belongs
	name: String containing the full name of the challenge
	shortName: A shortened name for the challenge, to be used as a tag
	summary (optional): A short summary advertising the main purpose of the challenge; maximum 250 characters; if not supplied, challenge.name will be used
	description (optional): A detailed description of the challenge
	prize (optional): Number of gems offered as a prize to challenge winner. Default value: 0
	official (optional): Whether or not a challenge is an official Habitica challenge (requires admin). Default value: false
	"""
	url = "https://habitica.com/api/v3/challenges"
	payload = {'challenge': {'groupId': groupId, 'name': name, 'shortName': shortName, 'summary': summary, 'description': description, 'prize': prize}, 'official': official}
	return(postUrl(user, url, payload))

def deleteChallenge(user, challengeId):
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(deleteUrl(user, url))

