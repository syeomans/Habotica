"""Content API function

This module contains a single function to retrieve content from Habitica. The
function makes a call to Habitica's V3 API and returns the JSON response object
as a python dictionary.

See https://habitica.com/apidoc/ for Habitica's API documentation.
"""
from Habotica.urlFunctions import getUrl

def getContent(contentType=None, language=None):
	"""Get all contents or specified contents on Habitica.

	Args:
		language (str): Language code used for the items' strings. If the
			authenticated user makes the request, the content will return with
			the user's configured language.
			Default value: en
			Allowed values: "bg", "cs", "da", "de", "en", "en@pirate", "en_GB",
				"es", "es_419", "fr", "he", "hu", "id", "it", "ja", "nl", "pl",
				"pt", "pt_BR", "ro", "ru", "sk", "sr", "sv", "uk", "zh", "zh_TW"
		contentType (str): Various data about the content of Habitica. The
			content route contains many keys, but the data listed under
			"Attributes" are the recomended data to use.

	Attributes:
		mystery: The mystery sets awarded to paying subscribers.
		gear: The gear that can be equipped.
			tree: Detailed information about the gear, organized by type.
			flat: The full key of each equipment.
		spells: The skills organized by class. Includes cards and visual buffs.
		potion: Data about the health potion.
		armoire: Data about the armoire.
		classes: The available classes.
		eggs: All available eggs.
		timeTravelStable: The animals available in the Time Traveler's
			stable, separated into pets and mounts.
		hatchingPotions: All the hatching potions.
		petInfo: All the pets with extra info.
		mountInfo: All the mounts with extra info.
		food: All the food.
		userCanOwnQuestCategories: The types of quests that a user can own.
		quests: Data about the quests.
		appearances: Data about the apperance properties.
			hair: Data about available hair options.
			shirt: Data about available shirt options.
			size: Data about available body size options.
			skin: Data about available skin options.
			chair: Data about available chair options.
			background: Data about available background options.
		backgrounds: Data about the background sets.
		subscriptionBlocks: Data about the various subscirption blocks.

	A list of all content types (as of December 21, 2019):
		achievements, questSeriesAchievements, animalColorAchievements, quests,
		questsByLevel, userCanOwnQuestCategories, itemList, gear, spells,
		subscriptionBlocks, audioThemes, mystery, officialPinnedItems, bundles,
		potion, armoire, classes, gearTypes, cardTypes, special, dropEggs,
		questEggs, eggs, timeTravelStable, dropHatchingPotions,
		premiumHatchingPotions, wackyHatchingPotions, hatchingPotions, pets,
		premiumPets, questPets, specialPets, wackyPets, petInfo, mounts,
		questMounts, premiumMounts, specialMounts, mountInfo, food, appearances,
		backgrounds, backgroundsFlat, userDefaults, tasksByCategory,
		userDefaultsMobile, faq, loginIncentives

	Returns:
		A dictionary of the specified content objects or a dictionary of all
		content objects if contentType is not specified.
	"""
	# Get language. Add to URL as query parameter if specified.
	if language == None:
		url = 'https://habitica.com/api/v3/content'
	else:
		url = 'https://habitica.com/api/v3/content?language=' + language

	# Return only specified content. If none specified, return all content.
	if contentType == None:
		return(getUrl(url)['data'])
	else:
		return(getUrl(url)['data'][contentType])
