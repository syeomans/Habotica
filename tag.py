"""Tag API functions.

This module contains functions to interact with Habitica tags. Each function
makes a call to Habitica's V3 API.

See https://habitica.com/apidoc/ for Habitica's API documentation.
"""

from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl

def createTag(credentials, name):
	"""Create a new tag.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		name (str): The name of the tag to be added.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tags"
	payload = {"name": name}
	return(postUrl(url, credentials, payload))

def deleteTag(credentials, tagId):
	"""Delete a user tag given its ID.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		tagId (str): the tag's ID.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tags/" + tagId
	return(deleteUrl(url, credentials))

def getTag(credentials, tagId):
	"""Get a tag given its ID. Returns a dictionary with the tag's name and ID.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		tagId (str): the tag's ID.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tags/" + tagId
	return(getUrl(url, credentials))

def getTags(credentials):
	"""Gets user's tags. Returns a list of dictionaries of tag names and IDs.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tags/"
	return(getUrl(url, credentials))

def reorderTag(credentials, tagId, position):
	"""Reorder a tag.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		tagId (str): The tag's ID.
		position (int): Position the tag is moving to. Index starts at 0.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/reorder-tags/"
	payload = {"tagId": tagId, "to": position}
	return(postUrl(url, credentials, payload))

def updateTag(credentials, tagId, name):
	"""Update a tag's name.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		tagId (str): The tag's ID.
		name (str): The new name of the tag.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tags/" + tagId
	payload = {"name": name}
	return(putUrl(url, credentials, payload))
