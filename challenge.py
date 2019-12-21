"""Challenge class and API functions

This module contains class definitions for Habitica challenges. Each function
makes a call to Habitica's V3 API and the custom classes handle Habitica's
JSON objects pythonically.

See https://habitica.com/apidoc/ for Habitica's API documentation.
"""

from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl
from Habotica.task import createChallengeTask, getChallengeTasks, habit, daily, todo, reward
from Habotica.group import group

class challenge:
	"""Challenge class

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (string): ID of the challenge. Optional if [data] is given.
			You can find this in the URL of the challenge's page on Habitica.
			default: None
		data (JSON): Optional JSON object containing the data for this
			challenge. If this option is not taken, the data will be found with
			an extra API call.
			default: None

	Attributes:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		group (group): The group associated with the challenge. See "Group"
			documentation for details.
		prize (int): Number of gems awarded to the winner of the challenge.
		memberCount (int): Number of users participanting in the challenge.
		description (str): A detailed description of the challenge.
		official (bool): True if the challenge was created by Habitica admins.
		summary (str): A short summary advertising the main purpose of the
			challenge. Maximum 250 characters.
		tasksOrder (dict): Ordered lists of habit, daily, reward, and todo ids.
		createdAt (str): Timestamp of when the challenge was created.
		updatedAt (str): Timestamp of when the challenge was last modified.
		id (str): The challenge's id.
		shortName (str): A shortened name for the challenge, to be used as a tag
		_id (str): The challenge's id.
		leader (dict): Info on the challenge leader (id, name, etc.).
		categories (dict): Info on the challenge's category/categories.
		name (str): String containing the full name of the challenge..
		todos (task/todo): A list of the challenge's todos.
		habits (task/habit): A list of the challenge's habits.
		dailys (task/daily): A list of the challenge's dailys.
		rewards (task/reward): A list of the challenge's rewards.
	"""
	def __init__(self, credentials, challengeId=None, data=None):
		if data == None:
			data = getChallenge(credentials, challengeId)['data']

		self.credentials = credentials
		self.group = group(credentials, data['group']['id'], data['group']) if 'group' in data.keys() else None

		self.prize = data['prize'] if 'prize' in data.keys() else None
		self.memberCount = data['memberCount'] if 'memberCount' in data.keys() else None
		self.description = data['description'] if 'description' in data.keys() else None
		self.official = data['official'] if 'official' in data.keys() else None
		self.summary = data['summary'] if 'summary' in data.keys() else None
		self.tasksOrder = data['tasksOrder'] if 'tasksOrder' in data.keys() else None
		self.createdAt = data['createdAt'] if 'createdAt' in data.keys() else None
		self.updatedAt = data['updatedAt'] if 'updatedAt' in data.keys() else None
		self.id = data['id'] if 'id' in data.keys() else None
		self.shortName = data['shortName'] if 'shortName' in data.keys() else None
		self._id = data['_id'] if '_id' in data.keys() else None
		self.leader = data['leader'] if 'leader' in data.keys() else None
		self.categories = data['categories'] if 'categories' in data.keys() else None
		self.name = data['name'] if 'name' in data.keys() else None

		try:
			self.todos = [todo(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'todos')['data']]
		except:
			self.todos = None
		try:
			self.habits = [habit(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'habits')['data']]
		except:
			self.habits = None
		try:
			self.dailys = [daily(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'dailys')['data']]
		except:
			self.dailys = None
		try:
			self.rewards = [reward(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'rewards')['data']]
		except:
			self.rewards = None

	def __repr__(self):
		"""Print function.

		Prints challenge object's data as a dictionary.
		"""
		return(str(self.__dict__))

	def deleteChallenge(self):
		"""Deletes a challenge.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success
		"""
		url = "https://habitica.com/api/v3/challenges/" + self.id
		return(deleteUrl(url, self.credentials))

	def exportChallenge(self):
		"""Exports a challenge in CSV.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success
		"""
		url = "https://habitica.com/api/v3/challenges/" + self.id + "/export/csv"
		return(getUrl(url, self.credentials))

	def selectChallengeWinner(self, winnerId):
		"""Selects a winner for a challenge.

		Args:
			winnerId (str): The id of the winning user.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success
		"""
		url = "https://habitica.com/api/v3/challenges/" + self.id + "/selectWinner/" + winnerId
		return(postUrl(url, self.credentials))

	def updateChallenge(self, name = "", summary = "", description = "", leader = ""):
		"""Updates challenge info.

		Updates the name, description, or leader of a challenge. User must be
		the challenge leader.

		Args:
			name (str): The new full name of the challenge. Optional.
			summary (str): The new challenge summary. Optional.
			description (str): The new challenge description. Optional.
			leader (str): The UUID of the new challenge leader. Optional.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success
		"""
		url = "https://habitica.com/api/v3/challenges/" + self.id

		payload = {}
		if name != "":
			payload["name"] = name
		if summary != "":
			payload["summary"] = summary
		if description != "":
			payload["description"] = description
		if leader != "":
			payload["leader"] = leader

		return(putUrl(url, self.credentials, payload))

def createChallenge(creds, groupId, name, shortName, summary = " ", description = " ", prize = 0):
	"""Creates a new challenge.

	Creates a challenge. Cannot create associated tasks with this route.
	See createChallengeTasks to create associated tasks.

	Note: I'm not an admin, so I can't support creating official challenges.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The id of the group to which the challenge belongs.
		name (str): String containing the full name of the challenge.
		shortName (str): A shortened name for the challenge, to be used as a tag
		summary (str): A short summary advertising the main purpose of the
			challenge. Maximum 250 characters. If not supplied, challenge.name
			will be used. Optional.
		description (str): A detailed description of the challenge. Optional.
		prize (int): Number of gems offered as a prize to challenge winner.
			Optional. Default value: 0.
		official (bool): Whether or not a challenge is an official Habitica
			challenge. Requires admin privileges. Default value: false.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges"
	payload = {'group': groupId, 'name': name, 'shortName': shortName, 'summary': summary, 'description': description, 'prize': prize}
	return(postUrl(url, creds, payload))

def deleteChallenge(creds, challengeId):
	"""Deletes a challenge.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(deleteUrl(url, creds))

def exportChallenge(creds, challengeId):
	"""Exports a challenge in CSV format.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.

	Returns:
		A CSV file containing challenge data.
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/export/csv"
	return(getUrl(url, creds))

def getChallenge(creds, challengeId):
	"""Get a single challenge given its id.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(getUrl(url, creds))

def getGroupChallenges(creds, groupId):
	"""Get all challenges for a group.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/groups/" + groupId
	return(getUrl(url, creds))

def getChallenges(creds):
	"""Get challenges the user has access to.

	Includes public challenges, challenges belonging to the user's group,
	and challenges the user has already joined.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/user"
	return(getUrl(url, creds))

def joinChallenge(creds, challengeId):
	"""Join a challenge.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/join"
	return(postUrl(url, creds))

def leaveChallenge(creds, challengeId):
	"""Leave a challenge.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/leave"
	return(postUrl(url, creds))

def selectChallengeWinner(creds, challengeId, winnerId):
	"""Select winner for a challenge.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.
		winnerId (str): The id of the winning user.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/selectWinner/" + winnerId
	return(postUrl(url, creds))

def updateChallenge(creds, challengeId, name = "", summary = "", description = "", leader = ""):
	"""Updates challenge info.

	Updates the name, description, or leader of a challenge. User must be
	the challenge leader.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.
		name (str): The new full name of the challenge. Optional.
		summary (str): The new challenge summary. Optional.
		description (str): The new challenge description. Optional.
		leader (str): The UUID of the new challenge leader. Optional.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success
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
