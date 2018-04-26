from urlFunctions import getUrl
from urlFunctions import postUrl
from urlFunctions import putUrl
from urlFunctions import deleteUrl

def createChallenge(creds, groupId, name, shortName, summary = " ", description = " ", prize = 0, official = False):
	"""
	Creates a challenge. Cannot create associated tasks with this route. See createChallengeTasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group to which the challenge belongs. Type: UUID
	name: String containing the full name of the challenge. Type: String
	shortName: A shortened name for the challenge, to be used as a tag. Type: String
	summary (optional): A short summary advertising the main purpose of the challenge; maximum 250 characters; if not supplied, challenge.name will be used
	description (optional): A detailed description of the challenge
	prize (optional): Number of gems offered as a prize to challenge winner. Default value: 0
	official (optional): Whether or not a challenge is an official Habitica challenge (requires admin). Default value: false
	"""
	url = "https://habitica.com/api/v3/challenges"
	#payload = {'challenge': {'groupId': groupId, 'name': name, 'shortName': shortName, 'summary': summary, 'description': description, 'prize': prize}, 'official': official}
	payload = {}
	return(postUrl(url, creds, payload))

def deleteChallenge(creds, challengeId):
	"""
	Delete a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(deleteUrl(url, creds))

def exportChallenge(creds, challengeId):
	"""
	Export a challenge in CSV

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID

	Returns a csv file. 
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/export/csv"
	return(getUrl(url, creds))

def getChallenge(creds, challengeId):
	"""
	Get a single challenge given its id.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(getUrl(url, creds))

def getGroupChallenges(creds, groupId):
	"""
	Get all challenges for a group

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group to which the challenge belongs. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/groups/" + groupId
	return(getUrl(url, creds))

def getChallenges(creds):
	"""
	Get challenges the user has access to. Includes public challenges, challenges belonging to the user's group, and challenges the user has already joined.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/challenges/user"
	return(getUrl(url, creds))

def joinChallenge(creds, challengeId):
	"""
	Join a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/join"
	return(postUrl(url, creds))

def leaveChallenge(creds, challengeId):
	"""
	Leave a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/leave"
	return(postUrl(url, creds))

def selectChallengeWinner(creds, challengeId, winnerId):
	"""
	Select winner for a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	winnerId: The _id of the winning user. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/selectWinner/" + winnerId
	return(postUrl(url, creds))

def updateChallenge(creds, challengeId, name = "", summary = "", description = "", leader = ""):
	"""
	Update the name, description, or leader of a challenge. User must be challenge leader.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
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

	return(putUrl(url, creds, payload))
