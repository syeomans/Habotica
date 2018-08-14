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
	"""
	url = "https://habitica.com/api/v3/user/buy-mystery-set/" + str(key)
	return(postUrl(url, creds))

def buyQuest(creds, key):
	"""
	Buy a quest with gold

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	key: The shorthand name of the quest. ex: 'atom1' is the questKey of "Attack of the Mundane, part 1."
		To see all current quest keys, use the content library: getContent('quests').keys() 
		Keys as of Apr. 14, 2018:
		['armadillo', 'atom1', 'atom2', 'atom3', 'axolotl', 'badger', 'basilist', 'beetle', 'bewilder', 'bunny',
		'burnout', 'butterfly', 'cheetah', 'cow', 'dilatory', 'dilatoryDistress1', 'dilatoryDistress2',
		'dilatoryDistress3', 'dilatory_derby', 'dustbunnies', 'dysheartener', 'egg', 'evilsanta', 'evilsanta2',
		'falcon', 'ferret', 'frog', 'ghost_stag', 'goldenknight1', 'goldenknight2', 'goldenknight3', 'gryphon',
		'guineapig', 'harpy', 'hedgehog', 'hippo', 'horse', 'kraken', 'lostMasterclasser1', 'lostMasterclasser2',
		'lostMasterclasser3', 'lostMasterclasser4', 'mayhemMistiflying1', 'mayhemMistiflying2', 'mayhemMistiflying3',
		'monkey', 'moon1', 'moon2', 'moon3', 'moonstone1', 'moonstone2', 'moonstone3', 'nudibranch', 'octopus', 'owl',
		'peacock', 'penguin', 'pterodactyl', 'rat', 'rock', 'rooster', 'sabretooth', 'sheep', 'slime', 'sloth',
		'snail', 'snake', 'spider', 'squirrel', 'stoikalmCalamity1', 'stoikalmCalamity2', 'stoikalmCalamity3',
		'stressbeast', 'taskwoodsTerror1', 'taskwoodsTerror2', 'taskwoodsTerror3', 'treeling', 'trex', 'trex_undead', 
		'triceratops', 'turtle', 'unicorn', 'vice1', 'vice2', 'vice3', 'whale', 'yarn']
	"""
	url = "https://habitica.com/api/v3/user/buy-quest/" + str(key)
	return(postUrl(url, creds))

def buyArmoire(creds, key):
	"""
	Buy an armoire item

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/buy-armoire"
	return(postUrl(url, creds))

def buy(creds, key):
	"""
	Buy gear, armoire or potion

	Under the hood uses UserBuyGear, UserBuyPotion and UserBuyArmoire
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	key: the item to buy. To see all current keys, import Content.py and use print(getContent('gear')['flat'].keys())  (there are a lot of them)
	"""
	url = "https://habitica.com/api/v3/user/buy/" + str(key)
	return(postUrl(url, creds))

def buySpecialSpell(creds, key):
	"""
	Buy special "spell" item
	Includes gift cards (e.g., birthday card), and avatar Transformation Items and their antidotes (e.g., Snowball item and Salt reward).
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	key: The special item to buy. Must be one of the keys from "content.special", such as birthday, snowball, salt.
		To see all current keys, import Content.py and use print(getContent('special').keys())
		Keys as of Aug. 14, 2018:
		['spookySparkles', 'petalFreePotion', 'sand', 'greeting', 'opaquePotion', 
		'shinySeed', 'seafoam', 'valentine', 'thankyou', 'snowball', 'birthday', 
		'congrats', 'goodluck', 'getwell', 'salt', 'nye']
	"""
	url = "https://habitica.com/api/v3/user/buy/" + str(key)
	return(postUrl(url, creds))

def cast(user, spellId, targetId = 'none'):
	"""
	Cast a skill (spell) on a target

	spellId: the skill to cast. Takes a string of characters.
	targetId: Query parameter, necessary if the spell is cast on a party member or task. 
		Not used if the spell is cast on the user or the user's current party.
		Takes a string containing a UUID.

	spellId to name mapping: 
	Mage
		fireball: "Burst of Flames" (target: task ID)
		mpheal: "Ethereal Surge" (target: none)
		earth: "Earthquake" (target: none)
		frost: "Chilling Frost" (target: none)
	Warrior 
		smash: "Brutal Smash" (target: taskId)
		defensiveStance: "Defensive Stance" (target: none)
		valorousPresence: "Valorous Presence" (target: none)
		intimidate: "Intimidating Gaze" (target: none)
	Rogue 
		pickPocket: "Pickpocket" (target: taskId)
		backStab: "Backstab" (target: taskId)
		toolsOfTrade: "Tools of the Trade" (target: none)
		stealth: "Stealth" (target: none)
	Healer 
		heal: "Healing Light" (target: none)
		protectAura: "Protective Aura" (target: none)
		brightness: "Searing Brightness" (target: none)
		healAll: "Blessing" (target: none)
	"""
	if targetId == 'none':
		url = 'https://habitica.com/api/v3/user/class/cast/' + spellId
	else:
		url = 'https://habitica.com/api/v3/user/class/cast/' + spellId + '?' + targetId
	print("Casting " + spellId)
	response = postUrl(user, url)
	return(response)

def changeClass(creds, newClass):
	"""
	Change class
	
	User must be at least level 10. If ?class is defined and user.flags.classSelected is false it'll change the class. 
	If user.preferences.disableClasses it'll enable classes, otherwise it sets user.flags.classSelected to false (costs 3 gems)

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	newClass: one of {warrior|rogue|wizard|healer}
	"""
	url = "https://habitica.com/api/v3/user/change-class?class=" + newClass
	return(postUrl(url, creds))

def deleteMessage(creds, messageId):
	"""
	Delete a message

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	id: te id of the message to delete
	"""
	url = "https://habitica.com/api/v3/user/messages/" + messageId
	return(deleteUrl(url, creds))

def deleteAllMessages(creds):
	"""
	Delete all messages

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/messages"
	return(deleteUrl(url, creds))

def deleteUser(creds, password, feedback):
	"""
	Delete an authenticated user's account

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	password: The user's password if the account uses local authentication
	feedback: User's optional feedback explaining reasons for deletion
	"""
	url = "https://habitica.com/api/v3/user"
	payload = {'password': password, 'feedback', feedback}
	return(deleteUrl(url, creds, payload))

def deleteSocialAuthentication(creds, network):
	"""
	Delete social authentication method

	Remove a social authentication method (only facebook supported) from a user profile. The user must have local authentication enabled
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/auth/social/" + network
	return(deleteUrl(url, creds))


### Test ###
# from content import *
# print(getContent('special').keys())

"""
['spookySparkles', 'petalFreePotion', 'sand', 'greeting', 'opaquePotion', 
'shinySeed', 'seafoam', 'valentine', 'thankyou', 'snowball', 'birthday', 
'congrats', 'goodluck', 'getwell', 'salt', 'nye']
"""