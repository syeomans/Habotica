from urlFunctions import postUrl

def runCron(creds):
	"""
	Runs cron.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/cron"
	return(postUrl(url, creds))