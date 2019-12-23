"""Standalone function to get Habitica's API status."""

from Habotica.urlFunctions import getUrl

def getAPIStatus():
	"""Get Habitica's API status.

	Args:
		No arguments.

	Returns:
		Status string: 'up' if everything is ok.
	"""
	url = "https://habitica.com/api/v3/status"
	return(getUrl(url))
