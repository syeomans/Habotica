from urlFunctions import getUrl
from urlFunctions import postUrl
from urlFunctions import putUrl
from urlFunctions import deleteUrl

def clearChatFlags(creds, chatId, groupId = 'party'):
	"""
	Resets the flag count on a chat message. Retains the id of the user's that have flagged the message. 
	(Only visible to moderators)

	Permission: Admin	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags'
	return(postUrl(url, creds))

def deleteChatMessage(creds, chatId, groupId = 'party', previousMsg = None):
	"""
	Deletes a chat message from a group

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	previousMsg: The last message's ID fetched by the client so that the whole chat will be returned only if new 
    	messages have been posted in the meantime
	"""
	if previousMsg == None:
		url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags'
	else:
		url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags?previousMsg=' + previousMsg
	return(deleteUrl(url, creds))

def flagChatMessage(creds, chatId, groupId = 'party'):
	"""
	Chat - Flag a group chat message. A message will be hidden from chat if two or more users flag a message. It will be hidden immediately 
	if a moderator flags the message. An email is sent to the moderators about every flagged message.	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/flag'
	return(postUrl(url, creds))

def getChat(creds, groupId = 'party'):
	"""
	Chat - Get chat messages from a group. Fetches an array of messages from a group.	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID

	return keys: userV, notifications, data, appVersion, success
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat'
	return(getUrl(url, creds))

def getChatData(creds, groupId = 'party'):
	"""
	Chat - Get chat messages from a group. Returns only a list of messages. 
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	return(getChat(creds, groupId)["data"])

def getNotifications(creds, groupId = 'party'):
	"""
	Chat - Get notifications for a user. 	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID

	return keys: seen, data, id, type
	"""
	return(getChat(creds, groupId)["notifications"])

def likeChatMessage(creds, chatId, groupId = 'party'):
	"""
	Chat - Like a group chat message	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/like'
	return(postUrl(url, creds))

def markMessagesRead(creds, groupId = 'party'):
	"""
	Chat - Mark all messages as read for a group	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/seen'
	return(postUrl(url, creds))

def postChatMessage(creds, message, groupId = 'party'):
	"""
	Chat - Post chat message to a group
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	message: The message to post
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat'
	payload = {"message": message}
	return(postUrl(url, creds, payload))
