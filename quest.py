"""Quest API functions.

This module contains functions to interact with Habitica quests. Each function
makes a call to Habitica's V3 API.

This module contains no class definitions. To retrieve a quest object from
Habitica's servers, use the content module: getContent('quests')[questKey]

To see all the current questKeys, again use the content module:
getContent('quests').keys()

questKeys as of Dec. 23, 2019:
'dilatory', 'stressbeast', 'burnout', 'evilsanta', 'evilsanta2',
'gryphon', 'hedgehog', 'ghost_stag', 'vice1', 'vice2', 'vice3',
'egg', 'rat', 'octopus', 'dilatory_derby', 'atom1', 'atom2',
'atom3', 'harpy', 'rooster', 'spider', 'moonstone1', 'moonstone2',
'moonstone3', 'goldenknight1', 'goldenknight2', 'goldenknight3',
'basilist', 'owl', 'penguin', 'trex', 'trex_undead', 'rock',
'bunny', 'slime', 'sheep', 'kraken', 'whale', 'dilatoryDistress1',
'dilatoryDistress2', 'dilatoryDistress3', 'cheetah', 'horse',
'frog', 'snake', 'unicorn', 'sabretooth', 'monkey', 'snail',
'bewilder', 'falcon', 'treeling', 'axolotl', 'turtle', 'armadillo',
'cow', 'beetle', 'taskwoodsTerror1', 'taskwoodsTerror2',
'taskwoodsTerror3', 'ferret', 'dustbunnies', 'moon1', 'moon2',
'moon3', 'sloth', 'triceratops', 'stoikalmCalamity1',
'stoikalmCalamity2', 'stoikalmCalamity3', 'guineapig', 'peacock',
'butterfly', 'mayhemMistiflying1', 'mayhemMistiflying2',
'mayhemMistiflying3', 'nudibranch', 'hippo', 'lostMasterclasser1',
'lostMasterclasser2', 'lostMasterclasser3', 'lostMasterclasser4',
'yarn', 'pterodactyl', 'badger', 'dysheartener', 'squirrel',
'seaserpent', 'kangaroo', 'alligator', 'velociraptor', 'bronze',
'dolphin', 'silver', 'robot', 'amber'

See https://habitica.com/apidoc/ for Habitica's API documentation.
"""

from Habotica.urlFunctions import postUrl

def abortQuest(credentials, groupId = 'party'):
	"""Abort a quest. Must be a group leader or quest leader.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/abort'
	return(postUrl(url, credentials))

def acceptQuest(credentials, groupId = 'party'):
	"""Accept a quest.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/accept'
	return(postUrl(url, credentials))

def cancelQuest(credentials, groupId = 'party'):
	"""Cancel a quest. Must be a group leader or quest leader.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/cancel'
	return(postUrl(url, credentials))

def forceStartQuest(credentials, groupId = 'party'):
	"""Force a quest to start. Must be a group leader or quest leader.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/force-start'
	return(postUrl(url, credentials))

def inviteToQuest(credentials, questKey, groupId = 'party'):
	"""Invite users to a quest.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.
		questKey (str): The shorthand name of the quest.
			ex: 'atom1' is the questKey of "Attack of the Mundane, part 1."
			To see all current quest keys, use the content module:
			getContent('quests').keys()
			Keys as of Dec. 23, 2019:
			'dilatory', 'stressbeast', 'burnout', 'evilsanta', 'evilsanta2',
			'gryphon', 'hedgehog', 'ghost_stag', 'vice1', 'vice2', 'vice3',
			'egg', 'rat', 'octopus', 'dilatory_derby', 'atom1', 'atom2',
			'atom3', 'harpy', 'rooster', 'spider', 'moonstone1', 'moonstone2',
			'moonstone3', 'goldenknight1', 'goldenknight2', 'goldenknight3',
			'basilist', 'owl', 'penguin', 'trex', 'trex_undead', 'rock',
			'bunny', 'slime', 'sheep', 'kraken', 'whale', 'dilatoryDistress1',
			'dilatoryDistress2', 'dilatoryDistress3', 'cheetah', 'horse',
			'frog', 'snake', 'unicorn', 'sabretooth', 'monkey', 'snail',
			'bewilder', 'falcon', 'treeling', 'axolotl', 'turtle', 'armadillo',
			'cow', 'beetle', 'taskwoodsTerror1', 'taskwoodsTerror2',
			'taskwoodsTerror3', 'ferret', 'dustbunnies', 'moon1', 'moon2',
			'moon3', 'sloth', 'triceratops', 'stoikalmCalamity1',
			'stoikalmCalamity2', 'stoikalmCalamity3', 'guineapig', 'peacock',
			'butterfly', 'mayhemMistiflying1', 'mayhemMistiflying2',
			'mayhemMistiflying3', 'nudibranch', 'hippo', 'lostMasterclasser1',
			'lostMasterclasser2', 'lostMasterclasser3', 'lostMasterclasser4',
			'yarn', 'pterodactyl', 'badger', 'dysheartener', 'squirrel',
			'seaserpent', 'kangaroo', 'alligator', 'velociraptor', 'bronze',
			'dolphin', 'silver', 'robot', 'amber'

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/invite/' + questKey
	return(postUrl(url, credentials))

def leaveQuest(credentials, groupId = 'party'):
	"""Leave a quest.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/leave'
	return(postUrl(url, credentials))


def rejectQuest(credentials, groupId = 'party'):
	"""Reject a quest.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The group's id. 'party' is also allowed.
			Default: 'party'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/reject'
	return(postUrl(url, credentials))
