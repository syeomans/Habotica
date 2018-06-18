from urlFunctions import getUrl
from urlFunctions import postUrl
from urlFunctions import putUrl
from urlFunctions import deleteUrl

def allocateAttributePoint(creds, stat=None):
	"""
	User - Allocate a single attribute point

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	stat: String	Default ='str' Allowed values: "str", "con", "int", "per"
	"""
	url = "https://habitica.com/api/v3/user/allocate"
	payload = {'stat': stat}
	return(postUrl(url, creds, payload))

def allocateAllAttributePoints(creds):
	"""
	Uses the user's chosen automatic allocation method, or if none, assigns all to STR. 
	Note: will return success, even if there are 0 points to allocate.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	stat: String. Default ='str'. Allowed values: "str", "con", "int", "per".
	"""
	url = "https://habitica.com/api/v3/user/allocate-now"
	return(postUrl(url, creds))

def allocateAttributePoints(creds, INT=None, STR=None, CON=None, PER=None):
	"""
	User - Allocate multiple attribute points

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	INT: number of attribute points to allocate to intelligence
	STR: number of attribute points to allocate to strength
	CON: number of attribute points to allocate to constitution
	PER: number of attribute points to allocate to perception
	"""
	url = "https://habitica.com/api/v3/user/allocate"
	payload = {'stats': {'int': INT, 'str': STR, 'con': CON, 'per': PER}}
	return(postUrl(url, creds, payload))

def blockUnblock(creds, uuid):
	"""
	User - Block / unblock a user from sending you a PM

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	uuid: The user id of the user to block / unblock
	"""
	url = "https://habitica.com/api/v3/user/block/" + str(uuid)
	return(postUrl(url, creds))

def buyHealthPotion(creds):
	"""
	User - Buy a health potion

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/buy-health-potion"
	return(postUrl(url, creds))

def buyMysterySet(creds, key):
	"""
	Buy a mystery set with a mystic hourglass

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	key: The shorthand date of the mystery set. ex: '201703' is the key for March 2017's mystery item set.
		To see all current mystery set keys, use the content library: getContent('mystery').keys() 
		Keys as of June 18, 2018:
		[u'201703', u'301703', u'201601', u'301404', u'201603', u'201602', u'201605', u'201604', u'201607', u'201606', 
		u'201609', u'201608', u'201403', u'201402', u'wondercon', u'201407', u'201406', u'201405', u'201404', u'201701', 
		u'201409', u'201408', u'201704', u'201705', u'201706', u'201707', u'201508', u'201509', u'201502', u'201503', 
		u'201501', u'201506', u'201507', u'201504', u'201505', u'201708', u'201709', u'201612', u'201610', u'201611', 
		u'201712', u'201711', u'201710', u'301405', u'201805', u'201804', u'201803', u'201802', u'201801', u'201410', 
		u'201411', u'201412', u'301704', u'201511', u'201510', u'201512', u'201702']
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = "https://habitica.com/api/v3/user/buy-mystery-set/" + str(key)
	return(postUrl(url, creds))
