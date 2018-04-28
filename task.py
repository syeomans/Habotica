from urlFunctions import getUrl
from urlFunctions import postUrl
from urlFunctions import putUrl
from urlFunctions import deleteUrl

def addTag(creds, taskId, tagId):
	"""
	Task - Add a tag to a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	tagId: The tag id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/tags/" + tagId
	payload = {"taskId": taskId, "tagId": tagId}
	return(postUrl(url, creds, payload))

def createChecklist(creds, taskId, text):
	"""
	Task - Add an item to the task's checklist

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	text: The text of the checklist item
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist"
	payload = {"text": text}
	return(postUrl(url, creds, payload))

def approveTask(creds, taskId, userId):
	"""
	Task - Approves a user assigned to a group task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	userId: The id of the user that will be approved
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/approve/" + userId
	return(postUrl(url, creds))

def assignTask(creds, taskId, assignedUserId):
	"""
	Task - Assigns a user to a group task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	assignedUserId: The id of the user that will be assigned to the task
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/assign/" + assignedUserId
	return(postUrl(url, creds))

def createChallengeTask(creds, challengeId, text, taskType, alias = None, attribute = None, collapseChecklist = False, 
						notes = None, date = None, priority = 1, reminders = None, frequency = "weekly", 
						repeat = True, everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
	"""
	Task - Create a new task belonging to a challenge
	Can be passed an object to create a single task or an array of objects to create multiple tasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	text: String. The text to be displayed for the task
	taskType: String. Task type, options are: "habit", "daily", "todo", "reward".
		Allowed values: "habit", "daily", "todo", "reward"
	alias (optional): String. Alias to assign to task
	attribute (optional): String. User's attribute to use, options are: "str", "int", "per", "con"
		Allowed values: "str", "int", "per", "con"
	collapseChecklist (optional): Boolean. Determines if a checklist will be displayed
		Default value: false
	notes (optional): String. Extra notes
	date (optional): String. Due date to be shown in task list. Only valid for type "todo."
	priority (optional): Number. Difficulty, options are 0.1, 1, 1.5, 2; eqivalent of Trivial, Easy, Medium, Hard.
		Default value: 1
		Allowed values: "0.1", "1", "1.5", "2"
	reminders (optional): String[]. Array of reminders, each an object that must include: a UUID, startDate and time. 
		For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3","startDate":"1/16/17","time":"1/16/17" }
	frequency (optional): String. Value "weekly" enables "On days of the week", value "daily" enables "EveryX Days". 
		Only valid for type "daily".
		Default value: weekly
		Allowed values: "weekly", "daily"
	repeat (optional): String. List of objects for days of the week, Days that are true will be repeated upon. 
		Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s. 
		Value of frequency must be "weekly". For example, to skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
		Default value: true
	everyX (optional): Number. Value of frequency must be "daily", the number of days until this daily task is 
		available again.
		Default value: 1
	streak (optional): Number. Number of days that the task has consecutively been checked off. 
		Only valid for type "daily"
		Default value: 0
	startDate (optional): Date. Date when the task will first become available. Only valid for type "daily"
	up (optional): Boolean. Only valid for type "habit." If true, enables the "+" under "Directions/Action" for 
		"Good habits."
		Default value: true
	down (optional): Boolean. Only valid for type "habit." If true, enables the "-" under "Directions/Action" for 
		"Bad habits."
		Default value: true
	value (optional): Number. Only valid for type "reward." The cost in gold of the reward.
		Default value: 0
	"""
	url = "https://habitica.com/api/v3/tasks/challenge/" + challengeId
	payload = {"text": text, "type": taskType} 
	if alias != None:
		payload["alias"] = alias
	if attribute != None:
		payload["attribute"] = attribute
	if collapseChecklist != False:
		payload["collapseChecklist"] = collapseChecklist
	if notes != None:
		payload["notes"] = notes
	if date != None:
		payload["date"] = date
	if priority != 1:
		payload["priority"] = priority
	if reminders != None:
		payload["reminders"] = reminders
	if frequency != "weekly":
		payload["frequency"] = frequency
	if repeat != True:
		payload["repeat"] = repeat
	if everyX != 1:
		payload["everyX"] = everyX
	if streak != 0:
		payload["streak"] = streak
	if startDate != None:
		payload["startDate"] = startDate
	if up != True:
		payload["up"] = up
	if down != True:
		payload["down"] = down
	if value != 0:
		payload["value"] = value
	return(postUrl(url, creds, payload))

def getTasks(creds, taskType = None):
	"""
	Task - Get a user's tasks

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskType: one of ['habits', 'dailys', 'todos', 'rewards', 'completedTodos'] (optional)

	The returned dictionaries' structure depends on the type of task. Keys defined below:

	todos keys: attribute, checklist, group, collapseChecklist, tags, text, challenge, userId, value, 
		id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	dailys keys: streak, startDate, isDue, attribute, userId, frequency, updatedAt, id, createdAt, 
		daysOfMonth, group, collapseChecklist, priority, text, type, repeat, tags, checklist, completed, 
		nextDue, weeksOfMonth, yesterDaily, challenge, reminders, everyX, value, _id, notes, history
	habits keys: attribute, counterUp, group, tags, down, text, challenge, counterDown, userId, up, 
		value, id, priority, frequency, notes, updatedAt, _id, type, reminders, createdAt, history
	rewards keys: attribute, group, tags, text, challenge, userId, value, id, priority, notes, updatedAt, 
		_id, type, reminders, createdAt
	completedTodos keys: attribute, dateCompleted, checklist, group, collapseChecklist, tags, text, 
		challenge, userId, value, id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	"""
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/user"
	else:
		url = "https://habitica.com/api/v3/tasks/user?type=" + taskType
	return(getUrl(url, creds))

def createGroupTask(creds, groupId):
	"""
	Task - Create a new task belonging to a group
	Can be passed an object to create a single task or an array of objects to create multiple tasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group the new task(s) will belong to
	"""
	url = "https://habitica.com/api/v3/tasks/group/" + groupId
	payload = {"groupId": groupId}
	return(postUrl(url, creds, payload))

def createTask(creds, text, taskType, tags = None, alias = None, attribute = None, collapseChecklist = False, 
				notes = None, date = None, priority = 1, reminders = None, frequency = "weekly", repeat = True, 
				everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
	"""
	Task - Create a new task belonging to the user
	Can be passed an object to create a single task or an array of objects to create multiple tasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	text: String. The text to be displayed for the task
	taskType: String. Task type, options are: "habit", "daily", "todo", "reward".
		Allowed values: "habit", "daily", "todo", "reward"
	tags (optional): String[]. Array of UUIDs of tags
	alias (optional): String. Alias to assign to task
	attribute (optional): String. User's attribute to use, options are: "str", "int", "per", "con"
		Allowed values: "str", "int", "per", "con"
	collapseChecklist (optional): Boolean. Determines if a checklist will be displayed
		Default value: false
	notes (optional): String. Extra notes
	date (optional): String. Due date to be shown in task list. Only valid for type "todo."
	priority (optional): Number. Difficulty, options are 0.1, 1, 1.5, 2; eqivalent of Trivial, Easy, Medium, Hard.
		Default value: 1
		Allowed values: "0.1", "1", "1.5", "2"
	reminders (optional): String[]. Array of reminders, each an object that must include: a UUID, startDate and time. 
		For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3","startDate":"1/16/17","time":"1/16/17" }
	frequency (optional): String. Value "weekly" enables "On days of the week", value "daily" enables "EveryX Days". 
		Only valid for type "daily".
		Default value: weekly
		Allowed values: "weekly", "daily"
	repeat (optional): String. List of objects for days of the week, Days that are true will be repeated upon. 
		Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s. 
		Value of frequency must be "weekly". For example, to skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
		Default value: true
	everyX (optional): Number. Value of frequency must be "daily", the number of days until this daily task is 
		available again.
		Default value: 1
	streak (optional): Number. Number of days that the task has consecutively been checked off. 
		Only valid for type "daily"
		Default value: 0
	startDate (optional): Date. Date when the task will first become available. Only valid for type "daily"
	up (optional): Boolean. Only valid for type "habit." If true, enables the "+" under "Directions/Action" for 
		"Good habits."
		Default value: true
	down (optional): Boolean. Only valid for type "habit." If true, enables the "-" under "Directions/Action" for 
		"Bad habits."
		Default value: true
	value (optional): Number. Only valid for type "reward." The cost in gold of the reward.
		Default value: 0
	"""
	url = "https://habitica.com/api/v3/tasks/user"
	payload = {"text": text, "type": taskType} 
	if tags != None:
		payload["tags"] = tags
	if alias != None:
		payload["alias"] = alias
	if attribute != None:
		payload["attribute"] = attribute
	if collapseChecklist != False:
		payload["collapseChecklist"] = collapseChecklist
	if notes != None:
		payload["notes"] = notes
	if date != None:
		payload["date"] = date
	if priority != 1:
		payload["priority"] = priority
	if reminders != None:
		payload["reminders"] = reminders
	if frequency != "weekly":
		payload["frequency"] = frequency
	if repeat != True:
		payload["repeat"] = repeat
	if everyX != 1:
		payload["everyX"] = everyX
	if streak != 0:
		payload["streak"] = streak
	if startDate != None:
		payload["startDate"] = startDate
	if up != True:
		payload["up"] = up
	if down != True:
		payload["down"] = down
	if value != 0:
		payload["value"] = value
	return(postUrl(url, creds, payload))

def deleteChecklist(creds, taskId, itemId):
	"""
	Task - Delete a checklist item from a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	itemId: The checklist item _id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId
	return(deleteUrl(url, creds))

def removeTag(creds, taskId, tagId):
	"""
	Task - Delete a tag from a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	tagId: The tag id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/tags/" + tagId
	return(deleteUrl(url, creds))

def deleteTask(creds, taskId):
	"""
	Task - Delete a task given its id

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	return(deleteUrl(url, creds))