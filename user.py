from urlFunctions import getUrl, postUrl, putUrl, deleteUrl
from task import task, habit, daily, todo, reward, completedTodo, getTasks
import task

def catchKeyError(response, path):
	"""
	Not meant for use outside initializing a user class

	Attempts to set a variable based on a path to the data inside a user's authenticated profile. 
	"""
	try:
		outstr = "output = response" + path
		exec(outstr)
		return(output)
	except KeyError:
		return(None)

class user:
	"""
	Class of User objects. 

	All functions in the User section of the API docs are supported as of 12/31/2018
	"""
	def __init__(self, userID, apiKey):

		#### Properties from User inputs
		self.userID = userID
		self.apiKey = apiKey
		self.credentials = {'x-api-user': self.userID, 'x-api-key': self.apiKey}

		### Properties from authenticated profile
		response = self.getAuthenticatedProfile()
		self.authenticatedProfile = response
		self.userV = response['userV']
		self.notifications = response['notifications']
		self.name = response['data']['profile']['name']
		self.guilds = catchKeyError(response, "['data']['guilds']")
		self.blurb = catchKeyError(response, "['data']['profile']['blurb']") 
		self.challenges = catchKeyError(response, "['data']['challenges']")
		self.inbox = response['data']['inbox']
		self.lastCron = response['data']['lastCron']
		self.training = response['data']['stats']['training']
		self.str = response['data']['stats']['str']
		self.int = response['data']['stats']['int']
		self.per = response['data']['stats']['per']
		self.con = response['data']['stats']['con']
		self.gp = response['data']['stats']['gp']
		self.hp = response['data']['stats']['hp']
		self.maxHP = response['data']['stats']['maxHealth']
		self.mp = response['data']['stats']['mp']
		self.maxMP = response['data']['stats']['maxMP']
		self.exp = response['data']['stats']['exp']
		self.lvl = response['data']['stats']['lvl']
		self.toNextLevel = response['data']['stats']['toNextLevel']
		self.buffs = response['data']['stats']['buffs']
		self._class = response['data']['stats']['class']
		self.points = response['data']['stats']['points']
		self.asleep = response['data']['preferences']['sleep']
		self.wearingCostume = response['data']['preferences']['costume']
		self.shirt = response['data']['preferences']['shirt']
		self.chair = response['data']['preferences']['chair']
		self.hair = response['data']['preferences']['hair']
		self.skin = response['data']['preferences']['skin']
		self.size = response['data']['preferences']['size']
		self.background = response['data']['preferences']['background']
		self.dayStart = response['data']['preferences']['dayStart']
		self.pinnedItems = response['data']['pinnedItems']
		self.habits = response['data']['tasksOrder']['habits']
		self.dailys = response['data']['tasksOrder']['dailys']
		self.todos = response['data']['tasksOrder']['todos']
		self.rewards = response['data']['tasksOrder']['rewards']
		self.needsCron = response['data']['needsCron']
		self.achievements = response['data']['achievements']
		self.pinnedItemsOrder = response['data']['pinnedItemsOrder']
		self.invitations = response['data']['invitations']
		self.unpinnedItems = response['data']['unpinnedItems']
		self.lastLogin = response['data']['auth']['timestamps']['loggedin']
		self.dateCreated = response['data']['auth']['timestamps']['created']
		self.username = response['data']['auth']['local']['username']
		self.email = response['data']['auth']['local']['email']
		self.webhooks = response['data']['webhooks']
		self.loginIncentives = response['data']['loginIncentives']
		self.hatchingPotions = response['data']['items']['hatchingPotions']
		self.currentMount = response['data']['items']['currentMount']
		self.costumeBack = catchKeyError(response, "['data']['items']['gear']['costume']['back']")
		self.costumeBody = catchKeyError(response, "['data']['items']['gear']['costume']['body']")
		self.costumeHead = catchKeyError(response, "['data']['items']['gear']['costume']['head']")
		self.costumeShield = catchKeyError(response, "['data']['items']['gear']['costume']['shield']")
		self.costumeArmor = catchKeyError(response, "['data']['items']['gear']['costume']['armor']")
		self.costumeWeapon = catchKeyError(response, "['data']['items']['gear']['costume']['weapon']")
		self.costumeHeadAccessory = catchKeyError(response, "['data']['items']['gear']['costume']['headAccessory']")
		self.costumeEyewear = catchKeyError(response, "['data']['items']['gear']['costume']['eyewear']")
		self.equippedBack = catchKeyError(response, "['data']['items']['gear']['equipped']['back']")
		self.equippedBody = catchKeyError(response, "['data']['items']['gear']['equipped']['body']")
		self.equippedHead = catchKeyError(response, "['data']['items']['gear']['equipped']['head']")
		self.equippedShield = catchKeyError(response, "['data']['items']['gear']['equipped']['shield']")
		self.equippedArmor = catchKeyError(response, "['data']['items']['gear']['equipped']['armor']")
		self.equippedWeapon = catchKeyError(response, "['data']['items']['gear']['equipped']['weapon']")
		self.equippedHeadAccessory = catchKeyError(response, "['data']['items']['gear']['equipped']['headAccessory']")
		self.equippedEyewear = catchKeyError(response, "['data']['items']['gear']['equipped']['eyewear']")
		self.ownedGear = response['data']['items']['gear']['owned'].keys()
		self.lastDrop = response['data']['items']['lastDrop']
		self.food = response['data']['items']['food']
		self.eggs = response['data']['items']['eggs']
		self.currentPet = response['data']['items']['currentPet']
		self.pets = response['data']['items']['pets']
		self.quests = response['data']['items']['quests']
		self.mounts = response['data']['items']['mounts']
		self.specialItems = response['data']['items']['special']
		self.flags = response['data']['flags']
		self.pushDevices = response['data']['pushDevices']
		self.invitesSent = response['data']['invitesSent']
		self.balance = response['data']['balance']
		self.todosHistory = response['data']['history']['todos']
		self.expHistory = response['data']['history']['exp']
		self.party = catchKeyError(response, "['data']['party']")
		self.partyId = catchKeyError(response, "['data']['party']['_id']")

		### These tag dictionaries are more user-friendly than the raw response
		self.tags = response['data']['tags'] # raw response
		self.tagIdToNameDict = {i['id']:i['name'] for i in response['data']['tags']}
		self.tagNameToIdDict = {i['name']:i['id'] for i in response['data']['tags']}

		### Setting up the user's task lists is tricky because we want this to be done with as few
		### API calls as possible. The getTasks() function gets all of the data in one call, but 
		### the data is returned unsorted. We need to then sort each data point into one of 4 task 
		### lists at the correct index. 
		### Note: This is so ugly and I'm so sorry, but this mess took the execution time of creating  
		### user objects down from 6 seconds to 3 seconds on my machine. 

		# Get the user's tasks. (This contains all data on all tasks, but is unsorted)
		tasks = getTasks(self.credentials)['data']

		# Get the order the tasks should be in. These are lists of uuid's.
		habitOrder =  response['data']['tasksOrder']['habits']
		dailyOrder =  response['data']['tasksOrder']['dailys']
		todoOrder =  response['data']['tasksOrder']['todos']
		rewardOrder =  response['data']['tasksOrder']['rewards']
		
		# Initialize task lists and fill with null values. These will be filled later.
		self.habits = [None for i in range(0,len(habitOrder))]
		self.dailys = [None for i in range(0,len(dailyOrder))]
		self.todos = [None for i in range(0,len(todoOrder))]
		self.rewards = [None for i in range(0,len(rewardOrder))]

		# Go through the unsorted task list. Sort each task into the correct list and index.
		for thisTask in tasks:
			thisType = thisTask['type']
			thisId = thisTask['id']
			# Sort into habit list 
			if thisType == 'habit':
				index = 0
				# Find the correct index
				for uuid in habitOrder:
					if uuid == thisId:
						# Sort into correct index in correct list
						self.habits[index] = thisTask
						break
					# Post-increment
					index += 1
			# Sort into daily list 
			elif thisType == 'daily':
				index = 0
				# Find the correct index
				for uuid in dailyOrder:
					if uuid == thisId:
						# Sort into correct index in correct list
						self.dailys[index] = thisTask
						break
					# Post-increment
					index += 1
			# Sort into todo list 
			elif thisType == 'todo':
				index = 0
				# Find the correct index
				for uuid in todoOrder:
					if uuid == thisId:
						# Sort into correct index in correct list
						self.todos[index] = thisTask
						break
					# Post-increment
					index += 1
			# Sort into reward list 
			elif thisType == 'reward':
				index = 0
				# Find the correct index
				for uuid in rewardOrder:
					if uuid == thisId:
						# Sort into correct index in correct list
						self.rewards[index] = thisTask
						break
					# Post-increment
					index += 1

		# Remove any ghost tasks that may have been picked up. I have no idea what these are, but they
		# definitely exist and I now believe in ghosts. 
		for i in self.habits:
			if i == None: 
				self.habits.remove(i)
		
		# I don't have a way of putting completed todos in order, so marvel at the single line!
		self.completedTodos = [completedTodo(self, i) for i in getTasks(self.credentials, 'completedTodos')['data']]
		# (I know, right?  I could have done the rest of them in one line too if it weren't so slow.)

	def allocateAttributePoint(self, stat=None):
		"""
		User - Allocate a single attribute point
		
		stat: String	Default ='str' Allowed values: "str", "con", "int", "per"
		"""
		url = "https://habitica.com/api/v3/user/allocate"
		payload = {'stat': stat}
		return(postUrl(url, self.credentials, payload))

	def allocateAllAttributePoints(self):
		"""
		Uses the user's chosen automatic allocation method, or if none, assigns all to STR. 
		
		Note: will return success, even if there are 0 points to allocate.
		
		stat: String. Default ='str'. Allowed values: "str", "con", "int", "per".
		"""
		url = "https://habitica.com/api/v3/user/allocate-now"
		return(postUrl(url, self.credentials))

	def allocateAttributePoints(self, INT=None, STR=None, CON=None, PER=None):
		"""
		User - Allocate multiple attribute points
		
		INT: number of attribute points to allocate to intelligence
		STR: number of attribute points to allocate to strength
		CON: number of attribute points to allocate to constitution
		PER: number of attribute points to allocate to perception
		"""
		url = "https://habitica.com/api/v3/user/allocate"
		payload = {'stats': {'int': INT, 'str': STR, 'con': CON, 'per': PER}}
		return(postUrl(url, self.credentials, payload))

	def block(self, uuid):
		"""
		User - Block / unblock a user from sending you a PM
		
		uuid: The user id of the user to block / unblock
		"""
		url = "https://habitica.com/api/v3/user/block/" + str(uuid)
		return(postUrl(url, self.credentials))

	def buyHealthPotion(self):
		"""
		User - Buy a health potion
		
		"""
		url = "https://habitica.com/api/v3/user/buy-health-potion"
		return(postUrl(url, self.credentials))

	def buyMysterySet(self, key):
		"""
		Buy a mystery set with a mystic hourglass
		
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
		return(postUrl(url, self.credentials))

	def buyQuest(self, key):
		"""
		Buy a quest with gold
		
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
		return(postUrl(url, self.credentials))

	def buyArmoire(self, key):
		"""
		Buy an armoire item
		
		"""
		url = "https://habitica.com/api/v3/user/buy-armoire"
		return(postUrl(url, self.credentials))

	def buy(self, key):
		"""
		Buy gear, armoire or potion
		
		Under the hood uses UserBuyGear, UserBuyPotion and UserBuyArmoire
		
		key: the item to buy. To see all current keys, import Content.py and use print(getContent('gear')['flat'].keys())  (there are a lot of them)
		"""
		url = "https://habitica.com/api/v3/user/buy/" + str(key)
		return(postUrl(url, self.credentials))

	def buySpecialSpell(self, key):
		"""
		Buy special "spell" item
		
		Includes gift cards (e.g., birthday card), and avatar Transformation Items and their antidotes (e.g., Snowball item and Salt reward).
		
		key: The special item to buy. Must be one of the keys from "content.special", such as birthday, snowball, salt.
			To see all current keys, import Content.py and use print(getContent('special').keys())
			Keys as of Aug. 14, 2018:
			['spookySparkles', 'petalFreePotion', 'sand', 'greeting', 'opaquePotion', 
			'shinySeed', 'seafoam', 'valentine', 'thankyou', 'snowball', 'birthday', 
			'congrats', 'goodluck', 'getwell', 'salt', 'nye']
		"""
		url = "https://habitica.com/api/v3/user/buy/" + str(key)
		return(postUrl(url, self.credentials))

	def cast(self, spellId, targetId = 'none'):
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
		#print("Casting " + spellId)
		response = postUrl(url, self.credentials)
		return(response)

	def changeClass(self, newClass):
		"""
		Change class
		
		User must be at least level 10. If ?class is defined and user.flags.classSelected is false it'll change the class. 
		If user.preferences.disableClasses it'll enable classes, otherwise it sets user.flags.classSelected to false (costs 3 gems)
		newClass: one of {warrior|rogue|wizard|healer}
		"""
		url = "https://habitica.com/api/v3/user/change-class?class=" + newClass
		return(postUrl(url, self.credentials))

	def deleteMessage(self, messageId):
		"""
		Delete a message
		
		id: te id of the message to delete
		"""
		url = "https://habitica.com/api/v3/user/messages/" + messageId
		return(deleteUrl(url, self.credentials))

	def deleteAllMessages(self):
		"""
		Delete all messages
		
		"""
		url = "https://habitica.com/api/v3/user/messages"
		return(deleteUrl(url, self.credentials))

	def deleteUser(self, password, feedback=""):
		"""
		Delete an authenticated user's account
		
		password: The user's password if the account uses local authentication
		feedback: User's optional feedback explaining reasons for deletion
		"""
		url = "https://habitica.com/api/v3/user"
		payload = {'password': password, 'feedback': feedback}
		return(deleteUrl(url, self.credentials, payload))

	def deleteSocialAuthentication(self, network):
		"""
		Delete social authentication method
		
		Remove a social authentication method (only facebook supported) from a user profile. 
		The user must have local authentication enabled
		
		"""
		url = "https://habitica.com/api/v3/user/auth/social/" + network
		return(deleteUrl(url, self.credentials))

	def disableClasses(self):
		"""
		Disable classes
		
		"""
		url = "https://habitica.com/api/v3/user/disable-classes"
		return(postUrl(url, self.credentials))

	def equip(self, itemType, key):
		"""
		Disable classes
		
		itemType: The type of item to equip or unequip
			Allowed values: "mount", "pet", "costume", "equipped"
		key: The item to equip or unequip
		"""
		url = "https://habitica.com/api/v3/user/equip/" + itemType + "/" + key
		return(postUrl(url, self.credentials))

	def feed(self, pet, food):
		"""
		User - Feed a pet
		
		pet: the string for the pet you want to feed. 
			To see all pet UUID strings, use the content library: getContent('pets').keys()
			To see all quest pet UUID strings, use the content library: getContent('premiumPets').keys()
			To see all special pet UUID strings, use the content library: getContent('specialPets').keys()
		food: the string for the food you want to feed your pet. 
			To see all food UUID strings, use the content library: getContent('food').keys()
		"""
		url = "https://habitica.com/api/v3/user/feed/" + pet + "/" + food
		return(postUrl(url, self.credentials))

	def getAnonymizedUserData(self):
		"""
		User - Get anonymized user data
		
		Returns the user's data without: Authentication information NewMessages/Invitations/Inbox Profile Purchased 
		information Contributor information Special items Webhooks Notifications
		
		"""
		url = "https://habitica.com/api/v3/user/anonymized"
		return(getUrl(url, self.credentials))

	def getAuthenticatedProfile(self, userFields = None):
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
		
		
		userFields: A list of comma separated user fields to be returned instead of the entire document. 
			Notifications are always returned.
			Example usage: "achievements,items.mounts"
		"""
		if userFields == None:
			url = "https://habitica.com/api/v3/user"
			return(getUrl(url, self.credentials))
		else:
			url = "https://habitica.com/api/v3/user?userFields=" + userFields
			return(getUrl(url, self.credentials))

	def getGearAvailableForPurchase(self):
		"""
		User - Get the gear items available for purchase for the authenticated user
		
		"""
		url = "https://habitica.com/api/v3/user/inventory/buy"
		return(getUrl(url, self.credentials))

	def getInAppRewards(self):
		"""
		User - Get the in app items appearing in the user's reward column
		
		"""
		url = "https://habitica.com/api/v3/user/in-app-rewards"
		return(getUrl(url, self.credentials))

	def hatch(self, egg, hatchingPotion):
		"""
		User - Hatch a pet
		
		egg: the string for the egg you want to hatch 
			To see all egg UUID strings, use the content library: getContent('eggs').keys()
		hatchingPotion: the string for the hatching potion you want to use 
			To see all hatching potion UUID strings, use the content library: getContent('hatchingPotions').keys()
		"""
		url = "https://habitica.com/api/v3/user/hatch/" + egg + "/" + hatchingPotion
		return(postUrl(url, self.credentials))

	def login(self, username, password):
		"""
		User - Login
		Login a user with email / username and password
		
		username: Username or email of the user
		password: The user's password
		"""
		url = "https://habitica.com/api/v3/user/auth/local/login"
		payload = {"username": username, "password": password}
		return(postUrl(url, self.credentials, payload))

	def sleep(self):
		"""
		Make the user start / stop sleeping (resting in the Inn)
		
		"""
		url = "https://habitica.com/api/v3/user/sleep"
		return(postUrl(url, self.credentials))

	def markPMsRead(self):
		"""
		Marks Private Messages as read
		
		"""
		url = "https://habitica.com/api/v3/user/mark-pms-read"
		return(postUrl(url, self.credentials))

	def movePinnedItem(self, typ, path, position):
		"""
		Move a pinned item in the rewards column to a new position after being sorted
		
		type (shortened to typ because reserved words): No idea. It's missing from the docs.
		path: The unique item path used for pinning (string)
		position: Where to move the task (number) 
			0 = top of the list. 
			-1 = bottom of the list. (-1 means push to bottom). 
			First position is 0

		Returns an array of the new pinned items in order
		"""
		url = "https://habitica.com/api/v3/user/move-pinned-item/" + typ + "/" + path + "/move/to/" + position
		return(postUrl(url, self.credentials))

	def openMysteryBox(self):
		"""
		Open the Mystery Item box
		
		credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}	
		"""
		url = "https://habitica.com/api/v3/user/open-mystery-item"
		return(postUrl(url, self.credentials))

	def buyGemItem(self, itemType, key):
		"""
		Purchase Gem or Gem-purchasable item
		
		itemType: Type of item to purchase.
			Allowed values: "gems", "eggs", "hatchingPotions", "premiumHatchingPotions", ",", ","
		key: Item's key (use "gem" for purchasing gems)
		"""
		url = "https://habitica.com/api/v3/user/purchase/" + itemType + "/" + key
		return(postUrl(url, self.credentials))

	def buyHourglassItem(self, itemType, key):
		"""
		Purchase Hourglass-purchasable item
		
		itemType: Type of item to purchase.
			Allowed values: "pets", "mounts"
		key: Ex: {Phoenix-Base}. The key for the mount/pet
		"""
		url = "https://habitica.com/api/v3/user/purchase-hourglass/" + itemType + "/" + key
		return(postUrl(url, self.credentials))

	def readCard(self, cardType):
		"""
		Read a card
		
		cardType: Type of card to read (e.g. - birthday, greeting, nye, thankyou, valentine)
		"""
		url = "https://habitica.com/api/v3/user/read-card/" + cardType
		return(postUrl(url, self.credentials))

	def register(self, username, email, password, confirmPassword):
		"""
		Register a new user with email, login name, and password or attach local auth to a social user
		
		username: Login name of the new user. Must be 1-36 characters, containing only a-z, 0-9, hyphens (-), or underscores (_).
		email: Email address of the new user
		password: Password for the new user
		confirmPassword: Password confirmation
		"""
		url = "https://habitica.com/api/v4/user/auth/local/register"
		payload = {"username": username, "email": email, "password": password, "confirmPassword": confirmPassword}
		return(postUrl(url, self.credentials, payload))

	def releaseMounts(self):
		"""
		Release mounts
		
		"""
		url = "https://habitica.com/api/v3/user/release-mounts"
		return(postUrl(url, self.credentials))

	def releasePetsAndMounts(self):
		"""
		Release pets and mounts and grants Triad Bingo
		
		"""
		url = "https://habitica.com/api/v3/user/release-both"
		return(postUrl(url, self.credentials))

	def reroll(self):
		"""
		Reroll a user using the Fortify Potion

		Note: User must either have enough gems or be >= lv 100

		"""
		url = "https://habitica.com/api/v3/user/reroll"
		return(postUrl(url, self.credentials))

	def resetPasswordSetNew(self, newPassword, confirmPassword):
		"""
		Reset Password Set New one

		Set a new password for a user that reset theirs. Not meant for public usage.

		newPassword: The new password
		confirmPassword: Password confirmation
		"""
		url = "https://habitica.com/api/v3/user/auth/reset-password-set-new-one"
		payload ={"newPassword": newPassword, "confirmPassword": confirmPassword}
		return(postUrl(url, self.credentials, payload))

	def resetPassword(self, email):
		"""
		Reset Password Set New one

		Send the user an email to let them reset their password

		email: The email address of the user
		"""
		url = "https://habitica.com/api/v3/user/auth/reset-password"
		payload ={"email": email}
		return(postUrl(url, self.credentials, payload))

	def resetUser(self):
		"""
		I really don't know what this one does, and I'm afraid to test it. The docs aren't helpful. 

		"""
		url = "https://habitica.com/api/v4/user/reset"
		return(postUrl(url, self.credentials))

	def revive(self):
		"""
		Revive the user from death

		"""
		url = "https://habitica.com/api/v3/user/revive"
		return(postUrl(url, self.credentials))

	def sellItem(self, itemType, key):
		"""
		Sell a gold-sellable item owned by the user

		itemType: The type of item to sell.
			Allowed values: "eggs", "hatchingPotions", "food"
		key: The key of the item
		"""
		url = "https://habitica.com/api/v3/user/sell/" + itemType + "/" + key
		return(postUrl(url, self.credentials))

	def setDayStart(self, dayStart = 0):
		"""
		Set preferences.dayStart for user

		dayStart: The hour number 0-23 for day to begin. If body is not included, will default to 0.
			Default value: 0
		"""
		url = "https://habitica.com/api/v3/user/custom-day-start"
		payload = {"dayStart": dayStart}
		return(postUrl(url, self.credentials, payload))

	def togglePinnedItem(self, key):
		"""
		Toggle an item to be pinned

		key: The key of the item
		"""
		url = "https://habitica.com/user/toggle-pinned-item/" + key
		return(getUrl(url, self.credentials))

	def buyItem(self, path):
		"""
		Unlock item or set of items by purchase

		path: Full path to unlock. See "content" API call for list of items.
		"""
		url = "https://habitica.com/api/v3/user/unlock?path=" + path
		return(postUrl(url, self.credentials))

	def updateEmail(self, newEmail, password):
		"""
		Change the user email address

		newEmail: The new email address
		password: The user password
		"""
		url = "https://habitica.com/api/v3/user/auth/update-email"
		payload = {"newEmail": newEmail, "password": password}
		return(putUrl(url, self.credentials, payload))

	def updateUser(self, payload):
		"""
		Some of the user items can be updated, such as preferences, flags and stats. ^

		Example payload: 
			{
			    "achievements.habitBirthdays": 2,
			    "profile.name": "MadPink",
			    "stats.hp": 53,
			    "flags.warnedLowHealth": false,
			    "preferences.allocationMode": "flat",
			    "preferences.hair.bangs": 3
			}
		"""
		url = "https://habitica.com/api/v3/user"
		return(putUrl(url, self.credentials, payload))

	def updateUsername(self, username):
		"""
		Update the username of a local user

		username: The new username
		"""
		url = "https://habitica.com/api/v3/user/auth/update-username"
		payload = {"username": username}
		return(putUrl(url, self.credentials, payload))

	def orbOfRebirth(self):
		"""
		Use Orb of Rebirth on user

		"""
		url = "https://habitica.com/api/v3/user/rebirth"
		return(postUrl(url, self.credentials))