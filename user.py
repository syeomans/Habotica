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

def feed(creds, pet, food):
	"""
	User - Feed a pet

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	pet: the string for the pet you want to feed. 
		To see all pet UUID strings, use the content library: getContent('pets').keys()
		To see all quest pet UUID strings, use the content library: getContent('premiumPets').keys()
		To see all special pet UUID strings, use the content library: getContent('specialPets').keys()
	food: the string for the food you want to feed your pet. 
		To see all food UUID strings, use the content library: getContent('food').keys()
	"""
	url = "https://habitica.com/api/v3/user/feed/" + pet + "/" + food
	return(postUrl(url, creds))

def getAnonymizedUserData(creds):
	"""
	User - Get anonymized user data

	Returns the user's data without: Authentication information NewMessages/Invitations/Inbox Profile Purchased 
	information Contributor information Special items Webhooks Notifications

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/anonymized"
	return(getUrl(url, creds))

def getAuthenticatedProfile(creds, userFields = None):
	"""
	User - Get the authenticated user's profile

	The user profile contains data related to the authenticated user including (but not limited to); 
		Achievements
		Authentications (including types and timestamps) 
		Challenges 
		Flags (including armoire, tutorial, tour etc...) 
		Guilds History (including timestamps and values) 
		Inbox 
		Invitations (to parties/guilds) 
		Items (character's full inventory)
		New Messages (flags for groups/guilds that have new messages) 
		Notifications 
		Party (includes current quest information) 
		Preferences (user selected prefs) 
		Profile (name, photo url, blurb) 
		Purchased (includes purchase history, gem purchased items, plans) 
		PushDevices (identifiers for mobile devices authorized) 
		Stats (standard RPG stats, class, buffs, xp, etc..) 
		Tags 
		TasksOrder (list of all ids for dailys, habits, rewards and todos)

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	
	userFields: A list of comma separated user fields to be returned instead of the entire document. 
		Notifications are always returned.
		Example usage: "achievements,items.mounts"
	"""
	if userFields == None:
		url = "https://habitica.com/api/v3/user"
		return(getUrl(url, creds))
	else:
		url = "https://habitica.com/api/v3/user?userFields=" + userFields
		return(getUrl(url, creds))

def getGearAvailableForPurchase(creds):
	"""
	User - Get the gear items available for purchase for the authenticated user

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/inventory/buy"
	return(getUrl(url, creds))

def getInAppRewards(creds):
	"""
	User - Get the in app items appearing in the user's reward column

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/in-app-rewards"
	return(getUrl(url, creds))

def hatch(creds, egg, hatchingPotion):
	"""
	User - Hatch a pet

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	egg: the string for the egg you want to hatch 
		To see all egg UUID strings, use the content library: getContent('eggs').keys()
	hatchingPotion: the string for the hatching potion you want to use 
		To see all hatching potion UUID strings, use the content library: getContent('hatchingPotions').keys()
	"""
	url = "https://habitica.com/api/v3/user/hatch/" + egg + "/" + hatchingPotion
	return(postUrl(url, creds))

def login(creds, username, password):
	"""
	User - Login

	Login a user with email / username and password

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	username: Username or email of the user
	password: The user's password
	"""
	url = "https://habitica.com/api/v3/user/auth/local/login"
	payload = {"username": username, "password": password}
	return(postUrl(url, creds, payload))

def sleep(creds):
	"""
	Make the user start / stop sleeping (resting in the Inn)

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/sleep"
	return(postUrl(url, creds))






# Test script
sam = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}
#from content import *
#print(getContent('eggs').keys())

#print(login(sam, 'Wolf', 'Gold'))