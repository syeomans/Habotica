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

def deleteUser(creds, password, feedback=""):
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
	
	Remove a social authentication method (only facebook supported) from a user profile. 
	The user must have local authentication enabled
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/auth/social/" + network
	return(deleteUrl(url, creds))

def disableClasses(creds):
	"""
	Disable classes
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/disable-classes"
	return(postUrl(url, creds))

def equip(creds, itemType, key):
	"""
	Disable classes
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	itemType: The type of item to equip or unequip
		Allowed values: "mount", "pet", "costume", "equipped"
	key: The item to equip or unequip
	"""
	url = "https://habitica.com/api/v3/user/equip/" + itemType + "/" + key
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

def markPMsRead(creds):
	"""
	Marks Private Messages as read
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/mark-pms-read"
	return(postUrl(url, creds))

def movePinnedItem(creds, typ, path, position):
	"""
	Move a pinned item in the rewards column to a new position after being sorted
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	type (shortened to typ because reserved words): No idea. It's missing from the docs.
	path: The unique item path used for pinning (string)
	position: Where to move the task (number) 
		0 = top of the list. 
		-1 = bottom of the list. (-1 means push to bottom). 
		First position is 0

	Returns an array of the new pinned items in order
	"""
	url = "https://habitica.com/api/v3/user/move-pinned-item/" + typ + "/" + path + "/move/to/" + position
	return(postUrl(url, creds))

def openMysteryBox(creds):
	"""
	Open the Mystery Item box
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}	
	"""
	url = "https://habitica.com/api/v3/user/open-mystery-item"
	return(postUrl(url, creds))

def purchaseGemItem(creds, itemType, key):
	"""
	Purchase Gem or Gem-purchasable item
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	itemType: Type of item to purchase.
		Allowed values: "gems", "eggs", "hatchingPotions", "premiumHatchingPotions", ",", ","
	key: Item's key (use "gem" for purchasing gems)
	"""
	url = "https://habitica.com/api/v3/user/purchase/" + itemType + "/" + key
	return(postUrl(url, creds))

def purchaseHourglassItem(creds, itemType, key):
	"""
	Purchase Hourglass-purchasable item
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	itemType: Type of item to purchase.
		Allowed values: "pets", "mounts"
	key: Ex: {Phoenix-Base}. The key for the mount/pet
	"""
	url = "https://habitica.com/api/v3/user/purchase-hourglass/" + itemType + "/" + key
	return(postUrl(url, creds))

def readCard(creds, cardType):
	"""
	Purchase Hourglass-purchasable item
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	cardType: Type of card to read (e.g. - birthday, greeting, nye, thankyou, valentine)
	"""
	url = "https://habitica.com/api/v3/user/read-card/" + cardType
	return(postUrl(url, creds))

def register(creds, username, email, password, confirmPassword):
	"""
	Register a new user with email, login name, and password or attach local auth to a social user
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	username: Login name of the new user. Must be 1-36 characters, containing only a-z, 0-9, hyphens (-), or underscores (_).
	email: Email address of the new user
	password: Password for the new user
	confirmPassword: Password confirmation
	"""
	url = "https://habitica.com/api/v4/user/auth/local/register"
	payload = {"username": username, "email": email, "password": password, "confirmPassword": confirmPassword}
	return(postUrl(url, creds, payload))

def releaseMounts(creds):
	"""
	Release mounts
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/release-mounts"
	return(postUrl(url, creds))

def releasePetsAndMounts(creds):
	"""
	Release pets and mounts and grants Triad Bingo
	
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/release-both"
	return(postUrl(url, creds))

def reroll(creds):
	"""
	Reroll a user using the Fortify Potion

	Note: User must either have enough gems or be >= lv 100

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/user/reroll"
	return(postUrl(url, creds))



# Test script
sam = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}
#from content import *
#print(getContent('eggs').keys())

#print(login(sam, 'Wolf', 'Gold'))
