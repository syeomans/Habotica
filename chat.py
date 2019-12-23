"""Chat class and API functions

This module contains class definitions for Habitica chats. Each function
makes a call to Habitica's V3 API and the custom classes handle Habitica's
JSON objects pythonically.

See https://habitica.com/apidoc/ for Habitica's API documentation.
"""

from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl

class message:
	"""Single message class

	A chat is made of messages. This class handles an individual message.
	To post a message, use the postMessage function of the chat class.

	Args:
		data (JSON): Response object containing the data for this message.

	Attributes:
		data (JSON): Response object containing the data for this message.
		username (str): Name of the user that posted the message. 'system' if
			the post was created by the system.
		userStyles (dict): JSON object of the user's avatar, equipment,
			costume, and etc.
		userId (str): The uuid of the user who posted this message. 'system' if
			the post was created by the system.
		text (str): The text of the message.
		unformattedText (str): The unformatted text of the message.
		info (dict): Info on what spell was cast to trigger this message. Only
			populated if the user is 'system'.
		flagCount (int): The number of users that have flagged this message.
		backer (bool): False if the user who posted is not a backer. Empty
			dictionary if the user is a backer. (I don't make the rules, I just
			write scripts for them.)
		groupId (str): The id of the group to which the chat belongs.
		client (str): Which client was used to post this message (web, app,
			etc.). None if 'system' posted this message.
		flags (dict): The flags raised against this message.
		likes (dict): A dictionary of the user ids that liked this message.
			Keys are user ids, value is True unless user un-liked.
		timestamp (str): Timestamp at time of posting.
		contributor (dict): False if the user who posted is not a contributor.
			Empty dictionary if the user is a contributor. (I think?)
		_id (str): The id of the chat.
		chatId (str): The id of the chat.
		user (str): The display name of the user who posted the message.
	"""
	def __init__(self, data):
		self.data = data
		self.username = data['username'] if 'username' in data.keys() else 'system'
		self.userStyles = data['userStyles'] if 'userStyles' in data.keys() else None
		self.userId = data['uuid']
		self.text = data['text']
		self.unformattedText = data['unformattedText'] if 'unformattedText' in data.keys() else None
		self.info = data['info']
		self.flagCount = data['flagCount']
		self.backer = data['backer'] if 'backer' in data.keys() else False
		self.groupId = data['groupId']
		self.client = data['client'] if 'client' in data.keys() else None
		self.flags = data['flags']
		self.likes = data['likes']
		self.timestamp = data['timestamp']
		self.contributor = data['contributor'] if 'contributor' in data.keys() else False
		self._id = data['_id']
		self.chatId = data['id']
		self.user = data['user'] if 'user' in data.keys() else self.username

	def __repr__(self):
		"""Print function.

		Prints message object's attributes as a dictionary.
		"""
		return(str(self.__dict__))

	def clearFlags(self):
		"""Reset the flag count on a message.

		Resets the flag count on a chat message. Retains the id of the user's
		that have flagged the message. Only visible to moderators. Requires
		the user to have admin permission.

		Args:
			No arguments.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/clearflags'
		return(postUrl(url, self.credentials))

	def deleteMessage(self, previousMsg = None):
		"""Deletes a message from a chat

		Args:
			previousMsg (str): The last message's ID fetched by the client so
				that the whole chat will be returned only if new messages have
				been posted in the meantime. Optional.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		if previousMsg == None:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/clearflags'
		else:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/clearflags?previousMsg=' + previousMsg
		return(deleteUrl(url, self.credentials))

	def flagMessage(self):
		"""Flag a group chat message.

		A message will be hidden from chat if two or more users flag a message.
		It will be hidden immediately if a moderator flags the message. An
		email is sent to the moderators about every flagged message.

		Args:
			No arguments.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/flag'
		return(postUrl(url, self.credentials))

	def likeMessage(self):
		"""Like a group chat message

		Args:
			No arguments.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/like'
		return(postUrl(url, self.credentials))

class chat:
	"""Chat class

	Contains messages from a party, guild, or private chat.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id. Can use 'party' for the user's party and
			'habitrpg' for the tavern. Default: 'party'.
		data (JSON): Response object containing the data for this message.
			Optional. If this option is not taken, the data will be collected
			from an API call.

	Attributes:
		groupId (str): The id for the group this chat belongs to.
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		messages (list): A list of the last 200 messages for this chat, ordered
			from newest to oldest. Each element is a message object.
	"""
	def __init__(self, credentials, groupId='party', data=None):
		if data == None:
			data = getChat(credentials, groupId)['data']
		self.groupId = groupId
		self.credentials = credentials

		self.messages = [message(i) for i in data]

	def getMessage(self, chatId):
		"""Get a message in this chat from the chat's id.

		Args:
			chatId (str): The id of the message.

		Returns:
			The message matching the given chatId.
		"""
		for i in self.messages:
			if i.chatId == chatId:
				return(i)

	def clearFlags(self, chatId):
		"""Reset the flag count on a message.

		Resets the flag count on a chat message. Retains the id of the user's
		that have flagged the message. Only visible to moderators. Requires
		the user to have admin permission

		Args:
			chatId (str): The chat message id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/clearflags'
		return(postUrl(url, self.credentials))

	def deleteMessage(self, chatId, previousMsg = None):
		"""Deletes a chat message from a group

		Args:
			chatId (str): The chat message id.
			previousMsg (str): The last message's ID fetched by the client so
				that the whole chat will be returned only if new messages have
				been posted in the meantime. Optional.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		if previousMsg == None:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/clearflags'
		else:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/clearflags?previousMsg=' + previousMsg
		return(deleteUrl(url, self.credentials))

	def flagMessage(self, chatId):
		"""Flag a group chat message.

		A message will be hidden from chat if two or more users flag a message.
		It will be hidden immediately if a moderator flags the message. An
		email is sent to the moderators about every flagged message.

		Args:
			chatId (str): The chat message id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/flag'
		return(postUrl(url, self.credentials))

	def likeMessage(self, chatId):
		"""Like a group chat message

		Args:
			chatId (str): The chat message id

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/like'
		return(postUrl(url, self.credentials))

	def markMessagesRead(self):
		"""Mark all messages as read for a group.

		Args:
			No arguments.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/seen'
		return(postUrl(url, self.credentials))

	def postMessage(self, text):
		"""Post a chat message to a group.

		Args:
			text (str): The text of the message.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat'
		payload = {"message": text}
		response = postUrl(url, self.credentials, payload)
		exec("response = " + response.replace('true', 'True').replace('false', 'False'))
		messageData = response['data']['message']
		self.messages = [message(messageData)] + self.messages
		return(response)

def clearFlags(creds, chatId, groupId = 'party'):
	"""Resets the flag count on a chat message.

	Resets the flag count on a chat message. Retains the id of the user's that
	have flagged the message (only visible to moderators). Requires the user
	to have admin permissions.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		chatId (str): The chat message id.
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags'
	return(postUrl(url, creds))

def deleteMessage(creds, chatId, groupId = 'party', previousMsg = None):
	"""Deletes a chat message from a group

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		chatId (str): The chat message id.
		groupId (str): The group id (or 'party'). Default: 'party'.
		previousMsg (str): The last message's ID fetched by the client so
			that the whole chat will be returned only if new messages have
			been posted in the meantime. Optional.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	if previousMsg == None:
		url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags'
	else:
		url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags?previousMsg=' + previousMsg
	return(deleteUrl(url, creds))

def flagMessage(creds, chatId, groupId = 'party'):
	"""Flag a group chat message.

	A message will be hidden from chat if two or more users flag a message.
	It will be hidden immediately if a moderator flags the message. An
	email is sent to the moderators about every flagged message.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		chatId (str): The chat message id.
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/flag'
	return(postUrl(url, creds))

def getChat(creds, groupId = 'party'):
	"""Get chat messages from a group.

	Fetches an array of messages from a group.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat'
	return(getUrl(url, creds))

def getChatData(creds, groupId = 'party'):
	"""Get chat messages from a group. Returns only a list of messages.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	return(getChat(creds, groupId)["data"])

def likeMessage(creds, chatId, groupId = 'party'):
	"""Like a group chat message.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		chatId (str): The chat message id.
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/like'
	return(postUrl(url, creds))

def markMessagesRead(creds, groupId = 'party'):
	"""Mark all messages as read for a group.

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/seen'
	return(postUrl(url, creds))

def postMessage(creds, message, groupId = 'party'):
	"""Post chat message to a group

	Args:
		creds (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		message (str): The message to post.
		groupId (str): The group id (or 'party'). Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat'
	payload = {"message": message}
	return(postUrl(url, creds, payload))
