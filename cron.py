from urlFunctions import postUrl

def cron(creds):
	"""
	Runs cron.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/cron"
	# payload = {'challenge': {'groupId': groupId, 'name': name, 'shortName': shortName, 'summary': summary, 'description': description, 'prize': prize}, 'official': official}
	# payload = {}
	# return(postUrl(url, creds, payload))
	return(postUrl(url, creds))