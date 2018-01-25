from habotica import getUrl
from habotica import postUrl
from habotica import putUrl
from habotica import deleteUrl

def createChallenge(user, groupId, name, shortName, summary = "", description = "", prize = 0, official = False):
	"""
	Creates a challenge. Cannot create associated tasks with this route. See createChallengeTasks.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	groupId: The id of the group to which the challenge belongs. Type: UUID
	name: String containing the full name of the challenge. Type: String
	shortName: A shortened name for the challenge, to be used as a tag. Type: String
	summary (optional): A short summary advertising the main purpose of the challenge; maximum 250 characters; if not supplied, challenge.name will be used
	description (optional): A detailed description of the challenge
	prize (optional): Number of gems offered as a prize to challenge winner. Default value: 0
	official (optional): Whether or not a challenge is an official Habitica challenge (requires admin). Default value: false
	"""
	url = "https://habitica.com/api/v3/challenges"
	payload = {'challenge': {'groupId': groupId, 'name': name, 'shortName': shortName, 'summary': summary, 'description': description, 'prize': prize}, 'official': official}
	return(postUrl(user, url, payload))

def deleteChallenge(user, challengeId):
	"""
	Delete a challenge

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(deleteUrl(user, url))

def exportChallenge(user, challengeId):
	"""
	Export a challenge in CSV

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID

	Returns a csv file. 
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/export/csv"
	return(getUrl(user, url))

def getChallenge(user, challengeId):
	"""
	Get a single challenge given its id.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(getUrl(user, url))

def getGroupChallenges(user, groupId):
	"""
	Get all challenges for a group

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	groupId: The id of the group to which the challenge belongs. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/groups/" + groupId
	return(getUrl(user, url))

def getUserChallenges(user):
	"""
	Get challenges the user has access to. Includes public challenges, challenges belonging to the user's group, and challenges the user has already joined.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	"""
	url = "https://habitica.com/api/v3/challenges/user"
	return(getUrl(user, url))

def joinChallenge(user, challengeId):
	"""
	Join a challenge

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/join"
	return(postUrl(user, url))

def leaveChallenge(user, challengeId):
	"""
	Leave a challenge

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/leave"
	return(postUrl(user, url))

def selectChallengeWinner(user, challengeId, winnerId):
	"""
	Select winner for a challenge

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID
	winnerId: The _id of the winning user. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/selectWinner/" + winnerId
	return(postUrl(user, url))

def updateChallenge(user, challengeId, name = "", summary = "", description = "", leader = ""):
	"""
	Update the name, description, or leader of a challenge. User must be challenge leader.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	challengeId: The challenge _id. Type: UUID
	name (optional): The new full name of the challenge. Type: String
	summary (optional): The new challenge summary. Type: String
	description (optional): The new challenge description. Type: String
	leader (optional): The UUID of the new challenge leader. Type: String
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	
	payload = {}
	if name != "":
		payload["name"] = name
	if summary != "":
		payload["summary"] = summary
	if description != "":
		payload["description"] = description
	if leader != "":
		payload["leader"] = leader

	return(putUrl(user, url, payload))