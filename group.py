"""Group class and API functions

This module contains class definitions for Habitica groups. Each function
makes a call to Habitica's V3 API and the custom classes handle Habitica's
JSON objects pythonically.

See https://habitica.com/apidoc/ for Habitica's API documentation.

Todo:
	group.invite() and invite() functions don't work.
	Turn group.quest into a quest object.
	Turn group.tasksOrder into a dict of task objects.
		Maybe make a new attribute 'tasks' instead.
	updateGroup may be missing something. See function for details.
"""
from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl
from Habotica.chat import chat

class group:
	"""Group class

	A group can be a party, a guild, or a purchased group plan.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (string): ID of the group. Can also be 'party', 'habitrpg', etc.
			Default value of None creates an object for the user's party.
		data (JSON): Optional JSON object containing the data for this group.
			If this option is not taken, the data will be found with an extra
			API call.
			default: None

	Attributes:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		leaderOnly (dict): Info hidden to all users except the leader.
		managers (dict): The managers of this group.
		purchased (dict): Info on the group's subscription.
		privacy (str): 'public' or 'private'.
		memberCount (int): Number of members in the group.
		description (str): The group's description.
		summary (str): The group's summary.
		challengeCount (int): The number of challenges this group is hosting.
		_id (str): The group's id.
		quest (dict): The group's active quest.
		tasksOrder (dict): Ordered lists of the group's habits, todos, dailys,
			and rewards. Empty if a group plan hasn't been purchased.
		groupId (str): The group's id.
		balance (int): The number of gems in the group's balance.
		type (str): The type of this group (party, guild, etc.).
			Possible values: party, guilds, privateGuilds, publicGuilds, tavern
		leader (dict): Authenticated profile of the leader of this group.
		categories (list): A list of gild/challenge categories matching this
			group. For more info on categories, visit:
			https://habitica.fandom.com/wiki/Guild_and_Challenge_Categories
		name (str): The name of the group.
		chat (chat): The last 200 messages of the group's chat.
	"""
	def __init__(self, credentials, groupId=None, data=None):
		if data == None:
			data = getGroup(credentials, groupId)['data']

		self.credentials = credentials
		self.leaderOnly = data['leaderOnly'] if 'leaderOnly' in data.keys() else None
		self.managers = data['managers'] if 'managers' in data.keys() else None
		self.purchased = data['purchased'] if 'purchased' in data.keys() else None
		self.privacy = data['privacy'] if 'privacy' in data.keys() else None
		self.memberCount = data['memberCount'] if 'memberCount' in data.keys() else None
		self.description = data['description'] if 'description' in data.keys() else None
		self.summary = data['summary'] if 'summary' in data.keys() else None
		self.challengeCount = data['challengeCount'] if 'challengeCount' in data.keys() else None
		self._id = data['_id'] if '_id' in data.keys() else None
		self.quest = data['quest'] if 'quest' in data.keys() else None
		self.tasksOrder = data['tasksOrder'] if 'tasksOrder' in data.keys() else None
		self.groupId = data['id'] if 'id' in data.keys() else None
		self.balance = data['balance'] if 'balance' in data.keys() else None
		self.type = data['type'] if 'type' in data.keys() else None
		self.leader = data['leader'] if 'leader' in data.keys() else None
		self.categories = data['categories'] if 'categories' in data.keys() else None
		self.name = data['name'] if 'name' in data.keys() else None

		self.chat = chat(self.credentials, self.groupId, data['chat'])

	def __repr__(self):
		"""Print function.

		Prints group object's attributes as a dictionary.
		"""
		return(str(self.__dict__))

	def invite(self, credentials, emails=None, uuids=None):
		"""Invite users to a group

		You can provide both emails and uuids, or just one. You must provide
		at least one.

		Args:
			credentials (dict): Formatted dictionary of user id and api key. If a
				user object has already been created, use user.credentials.
				format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
			emails (list): An array of dictionaries, each representing one
				email address to invite. Keys are 'email' and 'name'.
				email: The email address of the user being invited.
				name(optional): The name of the user being invited.
				ex: [{'email': 'user1email@example.com'},
					{'email': 'user2@email.com', 'name': 'user2'}]
			uuids (list): An array of uuids to invite.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			This function doesn't work.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/invite'
		if emails != None and uuids != None:
			payload = {'emails': emails, 'uuids': uuids}
		elif emails != None:
			payload = {'emails': emails}
		elif uuids != None:
			payload = {'uuids': uuids}
		else:
			return(postUrl(url, credentials))
		# print(payload)
		return(postUrl(url, credentials, payload))

	def removeManager(self, credentials):
		"""Remove a manager from a group

		Args:
			credentials (dict): Formatted dictionary of user id and api key. If a
				user object has already been created, use user.credentials.
				format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/remove-manager'
		return(postUrl(url, credentials))

	def removeMember(self, credentials, memberId):
		"""Remove a member from a group

		Permission: GroupLeader, Admin

		Args:
			credentials (dict): Formatted dictionary of user id and api key. If a
				user object has already been created, use user.credentials.
				format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
			memberId (str): The id of the member to remove.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/removeMember/' + memberId
		return(postUrl(url, credentials))

	def updateGroup(self, credentials):
		"""Remove a member from a group

		Permission: GroupLeader, Admin

		Args:
			credentials (dict): Formatted dictionary of user id and api key. If a
				user object has already been created, use user.credentials.
				format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		TODO:
			There's something missing from the online documentation. I have a
			feeling like there should be a body parameter containing all the
			changes to make. Online documentation:
			https://habitica.com/apidoc/#api-Group-UpdateGroup
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId
		return(putUrl(url, credentials))

def addManager(credentials, groupId):
	"""Add a manager to a group

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/add-manager'
	return(postUrl(url, credentials))

def createGroupPlan(credentials):
	"""Create a Group and then redirect to the correct payment

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/create-plan'
	return(postUrl(url, credentials))

def createGroup(credentials, name, groupType, privacy):
	"""Create a Group and then redirect to the correct payment

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		name (str): The name of the group.
		groupType (str): Type of group (guild or party).
			Allowed values: "guild", "party".
		privacy (str): Privacy of group (party MUST be private).
			Allowed values: "private", "public".

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups'
	payload = {'name': name, 'type': groupType, 'privacy': privacy}
	return(postUrl(url, credentials, payload))

def getGroupPlans(credentials):
	"""Get group plans for a user

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/group-plans'
	return(getUrl(url, credentials))

def getGroup(credentials, groupId):
	"""Get the data of a group.

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId
	return(getUrl(url, credentials))

def getGroups(credentials, groupType, paginate, page):
	"""Get groups for a user.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupType (str): The type of groups to retrieve. Must be a query string.
			representing a list of values like 'tavern,party'.
			Possible values: party, guilds, privateGuilds, publicGuilds, tavern.
		paginate: Public guilds support pagination. When true, guilds are
			returned in groups of 30.
			Allowed values: "true", "false"
		page: When pagination is enabled for public guilds, this parameter can
			be used to specify the page number (the initial page is number 0
			and not required).

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/'
	return(getUrl(url, credentials))

def invite(credentials, groupId, emails=None, uuids=None):
	"""Invite users to a group.

	You can provide both emails and uuids, or just one. You must provide at
	least one.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.
		emails (list): An array of dictionaries, each representing one
			email address to invite. Keys are 'email' and 'name'.
			email: The email address of the user being invited.
			name(optional): The name of the user being invited.
			ex: [{'email': 'user1email@example.com'},
				{'email': 'user2@email.com', 'name': 'user2'}]
		uuids (list): An array of uuids to invite.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.

	Todo:
		This function doesn't work.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/invite'
	if emails != None and uuids != None:
		payload = {'emails': emails, 'uuids': uuids}
	elif emails != None:
		payload = {'emails': emails}
	elif uuids != None:
		payload = {'uuids': uuids}
	else:
		return(postUrl(url, credentials))
	# print(payload)
	return(postUrl(url, credentials, payload))

def joinGroup(credentials, groupId):
	"""Join a group.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/join'
	return(postUrl(url, credentials))

def leaveGroup(credentials, groupId, keep=None):
	"""
	Group - Leave a group

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
		keep: Whether or not to keep challenge tasks belonging to the group being left.
			Default value: keep-all
			Allowed values: "remove-all", "keep-all"

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	if keep == None:
		url = 'https://habitica.com/api/v3/groups/:groupId/leave'
	else:
		url = 'https://habitica.com/api/v3/groups/:groupId/leave?keep=' + keep
	return(postUrl(url, credentials))

def rejectInvite(credentials, groupId):
	"""Reject a group invitation.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/reject-invite'
	return(postUrl(url, credentials))

def removeManager(credentials, groupId):
	"""Remove a manager from a group.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/remove-manager'
	return(postUrl(url, credentials))

def removeMember(credentials, groupId, memberId):
	"""Remove a member from a group.

	Permission: GroupLeader, Admin

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.
		memberId: The id of the member to remove.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/removeMember/' + memberId
	return(postUrl(url, credentials))

def updateGroup(credentials, groupId):
	"""Remove a member from a group.

	Permission: GroupLeader, Admin

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. 'party' for the user's party and 'habitrpg'
			for the tavern are accepted.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.

	Todo:
		There's something missing from the online documentation. I have a
		feeling like there should be a body parameter containing all the
		changes to make. Online documentation:
		https://habitica.com/apidoc/#api-Group-UpdateGroup
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId
	return(putUrl(url, credentials))
