"""Task class and API functions

This module contains class definitions for Habitica tasks. Each function
makes a call to Habitica's V3 API and the custom classes handle Habitica's
JSON objects pythonically.

See https://habitica.com/apidoc/ for Habitica's API documentation.

Todo:
	Move task.createChecklist() to children classes that use it.
	Remove credentials from task attributes.
	Test task.deleteTask().
	Test task.scoreChecklist() and move to related children.
	Test task.scoreTask() and move to related children.
	Test task.updateChecklist() and move to related children.
	Test task.updateTask().
	createGroupTask() payload should be a task object.
"""
from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl

class task:
	"""Parent class for habit, daily, todo, reward, and completed todo.

	This class uses polymorphism to handle habits, dailys, todos, rewards,
	and completed todos. All of these child objects inherit the attributes of
	this class as well as their own.

	Note:
		End users should create task lists through User objects. Create a User
		and call user.initTasks(). This will automatically populate the User
		object's habits, dailys, todos, rewards, and completdTodos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task's id. Optional if [data] is supplied. Either
			[data] or [taskId] must be given.
		data (JSON): Optional JSON object containing the data for this
			task. If this option is not taken, the data will be found with
			an extra API call. Either [data] or [taskId] must be given.
			default: None

	Attributes (inherited for all task types):
		data (JSON): Response object containing the data for this task.
		group (dict): Data relevant to paid group plans.
			keys: 'approval', 'assignedUsers', 'sharedCompletion'
		tags (list): A list of tag ids. To get a dictionary of tagIds and
			tagNames, use the tag module: getTags(credentials).
		text (str): The text of the task.
		challenge (dict): Data related to this task's challenge (if any).
			keys: taskId, id, shortName, broken
		userId (str): The user id of the task's related user.
		value (float): The task value for todos, dailys, and habits. Gold cost
			for rewards. See here for more info on task value:
			https://habitica.fandom.com/wiki/Task_Value
		id (str): The task id.
		priority (float): The difficulty of the task. 0.1: Trivial. 1: Easy.
			1.5: Medium. 2: Hard.
		notes (str): The notes section of this task.
		updatedAt (str): Timestamp when the task was last modified.
		_id (str): The task id.
		type (str): One of: habit, daily, todo, reward, completedTodo.
		reminders (list): A list of dictionaries of reminders.
		 	keys: id, time.
		createdAt (str): Timestamp when the task was created.
		credentials (dict): Credentials of the user who this task belongs to.
			TODO: Remove this

		Todo:
			Remove credentials from attributes.
	"""
	def __init__(self, credentials, taskId=None, data=None):
		if data == None:
			data = getTask(credentials, taskId)['data']
		self.data = data
		self.group = data['group']
		self.tags = data['tags']
		self.text = data['text']
		self.challenge = data['challenge']
		self.userId = [data['userId'] if 'userId' in data.keys() else None]
		self.value = data['value']
		self.id = data['id']
		self.priority = data['priority']
		self.notes = data['notes']
		self.updatedAt = data['updatedAt']
		self._id = data['_id']
		self.type = data['type']
		self.reminders = data['reminders']
		self.createdAt = data['createdAt']
		self.credentials = credentials

	def addTag(self, tagId):
		"""Add a tag to a task.

		Args:
			tagId (str): The tag id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/tags/" + tagId
		payload = {"taskId": self.id, "tagId": tagId}
		response = postUrl(url, self.credentials, payload)
		self.tags.append(tagId)
		return(response)

	def createChecklist(self, text):
		"""Add an item to the task's checklist.

		Args:
			text (str): The text of the checklist item.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Move to children classes that use this.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist"
		payload = {"text": text}
		response = postUrl(url, self.credentials, payload)
		self.checklist.append(text)
		return(response)

	def deleteChecklist(self, itemId):
		"""Delete a checklist item from a task.

		Args:
			itemId (str): The checklist item id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		response = deleteUrl(url, self.credentials)
		self.checklist.remove(itemId)
		return(response)

	def removeTag(self, tagId):
		"""Delete a tag from a task.

		Args:
			tagId (str): The tag id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/tags/" + tagId
		response = deleteUrl(url, self.credentials)
		self.tags.remove(tagId)
		return(response)

	def deleteTask(self):
		"""Delete a task given its id.

		Args:
			No arguments.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test this.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id
		return(deleteUrl(url, self.credentials))

	def scoreChecklist(self, itemId):
		"""Score a checklist item.

		Args:
			itemId (str): The checklist item id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
			Move to children classes that use this.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId + "/score"
		return(postUrl(url, self.credentials))

	def scoreTask(self, direction):
		"""Score a task.

		Args:
			direction (str): The direction for scoring the task.
				Allowed values: "up", "down".

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
			Move to children classes that use this.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/score/" + direction
		return(postUrl(url, self.credentials))

	def updateChecklist(self, itemId, text):
		"""Update a checklist item.

		Args:
			itemId (str): The checklist item id.
			text (str): The text that will replace the current checkitem text.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
			Move to children classes that use this.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		payload = {"text": text}
		return(putUrl(url, self.credentials, payload))

	def updateTask(self, text = None, attribute = None, collapseChecklist = None, notes = None,
				date = None, priority = None, reminders = None, frequency = None, repeat = True,
				everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
		"""Update a task.

		Args:
			text (str): Optional. The text to be displayed for the task.
			attribute (str): Optional. User's attribute to use.
				Options are: "str", "int", "per", "con".
			collapseChecklist (bool): Optional. Determines if a checklist will
				be displayed.
				Default value: false
			notes (str): Optional. Extra notes.
			date (str): Optional. Due date to be shown in task list. Only valid
				for type "todo."
			priority (float): Optional. Difficulty, options are 0.1, 1, 1.5, 2;
				eqivalent of Trivial, Easy, Medium, Hard.
				Default value: 1
			reminders (str[]): Optional. Array of reminders, each an object
				that must include a UUID, startDate and time.
				For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3",
				"startDate":"1/16/17","time":"1/16/17" }
			frequency (str): Optional. Value "weekly" enables "On days of the
				week", value "daily" enables "EveryX Days". Only valid for type
				"daily".
				Default value: "weekly"
				Allowed values: "weekly", "daily"
			repeat (str): Optional. List of objects for days of the week. Days
				that are true will be repeated upon. Only valid for type
				"daily". Any days not specified will be marked as true.
				Days are: su, m, t, w, th, f, s. Value of frequency must be
				"weekly". For example, to skip repeats on Mon & Fri:
				"repeat":{"f":false,"m":false}
				Default value: true
			everyX (int): Optional. The number of days until this daily task is
				available again. Value of frequency must be "daily".
				Default value: 1
			streak (int): Optional. Number of days that the task has
				consecutively been checked off. Only valid for type "daily".
				Default value: 0
			startDate (str): Optional. Date when the task will first become
				available. Only valid for type "daily"
			up (bool): Optional. If true, enables the "+" under
				"Directions/Action" for "Good habits." Only valid for type
				"habit."
				Default value: true
			down (bool): Optional. If true, enables the "-" under
				"Directions/Action" for "Bad habits." Only valid for type
				"habit."
				Default value: true
			value (float): Optional. The cost in gold of the reward. Only valid
				for type "reward."
				Default value: 0

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id
		payload = {}
		if text != None:
			payload["text"] = text
			self.text = text
		if attribute != None:
			payload["attribute"] = attribute
			self.attribute = attribute
		if collapseChecklist != None:
			payload["collapseChecklist"] = collapseChecklist
			self.collapseChecklist = collapseChecklist
		if notes != None:
			payload["notes"] = notes
			self.notes = notes
		if date != None:
			payload["date"] = date
			self.date = date
		if priority != None:
			payload["priority"] = priority
			self.priority = priority
		if reminders != None:
			payload["reminders"] = reminders
		if frequency != None:
			payload["frequency"] = frequency
			self.frequency = frequency
		if repeat != True:
			payload["repeat"] = repeat
			self.repeat = repeat
		if everyX != 1:
			payload["everyX"] = everyX
			self.everyX = everyX
		if streak != 0:
			payload["streak"] = streak
			self.streak = streak
		if startDate != None:
			payload["startDate"] = startDate
			self.startDate = startDate
		if up != True:
			payload["up"] = up
			self.up = up
		if down != True:
			payload["down"] = down
			self.down = down
		if value != 0:
			payload["value"] = value
			self.value = value
		return(putUrl(url, self.credentials, payload))

class habit(task):
	"""Habitica habit class. Inherits attributes and functions from Task.

	Note:
		End users should create task lists through User objects. Create a User
		and call user.initTasks(). This will automatically populate the User
		object's habits, dailys, todos, rewards, and completdTodos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task's id. Optional if [data] is supplied. Either
			[data] or [taskId] must be given.
		data (JSON): Optional JSON object containing the data for this
			task. If this option is not taken, the data will be found with
			an extra API call. Either [data] or [taskId] must be given.
			default: None

	Attributes:
		Inherited:
			data (JSON): Response object containing the data for this task.
			group (dict): Data relevant to paid group plans.
				keys: 'approval', 'assignedUsers', 'sharedCompletion'
			tags (list): A list of tag ids. To get a dictionary of tagIds and
				tagNames, use the tag module: getTags(credentials).
			text (str): The text of the task.
			challenge (dict): Data related to this task's challenge (if any).
				keys: taskId, id, shortName, broken
			userId (str): The user id of the task's related user.
			value (float): The task value for todos, dailys, and habits. Gold
				cost for rewards. See here for more info on task value:
				https://habitica.fandom.com/wiki/Task_Value
			id (str): The task id.
			priority (float): The difficulty of the task. 0.1: Trivial. 1: Easy.
				1.5: Medium. 2: Hard.
			notes (str): The notes section of this task.
			updatedAt (str): Timestamp when the task was last modified.
			_id (str): The task id.
			type (str): One of: habit, daily, todo, reward, completedTodo.
			reminders (list): A list of dictionaries of reminders.
			 	keys: id, time.
			createdAt (str): Timestamp when the task was created.
			credentials (dict): Credentials of the user this task belongs to.
				TODO: Remove this
		Standalone:
			frequency (str): "weekly" or "daily".
			history (dict[]): History of the habit.
				keys: 'date', 'value', 'scoredUp', 'scoredDown'
			counterUp (int): The number of times this daily has been scored up
				this "Reset Streak" period.
			up (bool): True if scoring this habit upward is enabled.
			counterDown (int): The number of times this daily has been scored
				down this "Reset Streak" period.
			down (bool): True if scoring this habit downward is enabled.
	"""
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.frequency = data['frequency']
		self.history = data['history']
		self.counterUp = data['counterUp']
		self.down = data['down']
		self.counterDown = data['counterDown']
		self.up = data['up']

	def scoreTask(self, direction):
		"""Score a task.

		Args:
			direction (str): The direction for scoring the task.
			Allowed values: "up", "down"

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/score/" + direction
		return(postUrl(url, self.credentials))

class daily(task):
	"""Habitica daily class. Inherits attributes and functions from Task.

	Note:
		End users should create task lists through User objects. Create a User
		and call user.initTasks(). This will automatically populate the User
		object's habits, dailys, todos, rewards, and completdTodos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task's id. Optional if [data] is supplied. Either
			[data] or [taskId] must be given.
		data (JSON): Optional JSON object containing the data for this
			task. If this option is not taken, the data will be found with
			an extra API call. Either [data] or [taskId] must be given.
			default: None

	Attributes:
		Inherited:
			data (JSON): Response object containing the data for this task.
			group (dict): Data relevant to paid group plans.
				keys: 'approval', 'assignedUsers', 'sharedCompletion'
			tags (list): A list of tag ids. To get a dictionary of tagIds and
				tagNames, use the tag module: getTags(credentials).
			text (str): The text of the task.
			challenge (dict): Data related to this task's challenge (if any).
				keys: taskId, id, shortName, broken
			userId (str): The user id of the task's related user.
			value (float): The task value for todos, dailys, and habits. Gold
				cost for rewards. See here for more info on task value:
				https://habitica.fandom.com/wiki/Task_Value
			id (str): The task id.
			priority (float): The difficulty of the task. 0.1: Trivial. 1: Easy.
				1.5: Medium. 2: Hard.
			notes (str): The notes section of this task.
			updatedAt (str): Timestamp when the task was last modified.
			_id (str): The task id.
			type (str): One of: habit, daily, todo, reward, completedTodo.
			reminders (list): A list of dictionaries of reminders.
			 	keys: id, time.
			createdAt (str): Timestamp when the task was created.
			credentials (dict): Credentials of the user this task belongs to.
				TODO: Remove this
		Standalone:
			attribute (str): Which stat to use. Not fully implemented in-game.
				Allowed values: str, int, con, per
			checklist (dict[]): The daily's checklist.
				keys: completed (bool), text (str), id (str)
			collapseChecklist (bool): Determines if a checklist will be
				displayed.
			completed (bool): Whether this daily has been checked off.
			startDate (str): The date this daily comes into effect.
				ex: 2018-02-19T05:00:00.000Z
			isDue (bool): True if this daily is due today.
			frequency (str): How often this daily repeats.
				Allowd values: daily, weekly, monthly, yearly
			daysOfMonth (int[]): The calendar day of each month this daily
				repeats on. Empty array if frequency is not "monthly".
			weeksOfMonth (int[]): The calendar week of each month this daily
				repeats on. Empty array if frequency is not "monthly".
			repeat (dict): Weekdays to repeat on.
				keys: m, t, w, th, f, s, su. All values are bool.
			nextDue (str[]): The next 6 datetimes the daily will be due.
			yesterDaily (bool): Whether this was marked as complete or not due
				yesterday. In-game flag for Record Yesterday's Activity feature.
			everyX (int): The number of days/weeks/etc. this daily repeats.
	"""
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.attribute = data['attribute']
		self.checklist = data['checklist']
		self.collapseChecklist = data['collapseChecklist']
		self.completed = data['completed']
		self.startDate = data['startDate']
		self.isDue = data['isDue']
		self.frequency = data['frequency']
		self.daysOfMonth = data['daysOfMonth']
		self.repeat = data['repeat']
		self.nextDue = data['nextDue']
		self.weeksOfMonth = data['weeksOfMonth']
		self.yesterDaily = data['yesterDaily']
		self.everyX = data['everyX']

	def createChecklist(self, text):
		"""Add an item to the task's checklist.

		Args:
			text (str): The text of the checklist item.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist"
		payload = {"text": text}
		response = postUrl(url, self.credentials, payload)
		self.checklist.append(text)
		return(response)

	def deleteChecklist(self, itemId):
		"""Delete a checklist item from a task.

		Args:
			itemId (str): The checklist item id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		response = deleteUrl(url, self.credentials)
		self.checklist.remove(itemId)
		return(response)

	def scoreChecklist(self, itemId):
		"""Score a checklist item

		Args:
			itemId (str): The checklist item id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId + "/score"
		return(postUrl(url, self.credentials))

	def updateChecklist(self, itemId, text):
		"""Unassign a user from a paid group task.

		Args:
			itemId (str): The checklist item id.
			text (str): The text that will replace the current checkitem text.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		payload = {"text": text}
		return(putUrl(url, self.credentials, payload))

class todo(task):
	"""Habitica todo class. Inherits attributes and functions from Task.

	Note:
		End users should create task lists through User objects. Create a User
		and call user.initTasks(). This will automatically populate the User
		object's habits, dailys, todos, rewards, and completdTodos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task's id. Optional if [data] is supplied. Either
			[data] or [taskId] must be given.
		data (JSON): Optional JSON object containing the data for this
			task. If this option is not taken, the data will be found with
			an extra API call. Either [data] or [taskId] must be given.
			default: None

	Attributes:
		Inherited:
			data (JSON): Response object containing the data for this task.
			group (dict): Data relevant to paid group plans.
				keys: 'approval', 'assignedUsers', 'sharedCompletion'
			tags (list): A list of tag ids. To get a dictionary of tagIds and
				tagNames, use the tag module: getTags(credentials).
			text (str): The text of the task.
			challenge (dict): Data related to this task's challenge (if any).
				keys: taskId, id, shortName, broken
			userId (str): The user id of the task's related user.
			value (float): The task value for todos, dailys, and habits. Gold
				cost for rewards. See here for more info on task value:
				https://habitica.fandom.com/wiki/Task_Value
			id (str): The task id.
			priority (float): The difficulty of the task. 0.1: Trivial. 1: Easy.
				1.5: Medium. 2: Hard.
			notes (str): The notes section of this task.
			updatedAt (str): Timestamp when the task was last modified.
			_id (str): The task id.
			type (str): One of: habit, daily, todo, reward, completedTodo.
			reminders (list): A list of dictionaries of reminders.
			 	keys: id, time.
			createdAt (str): Timestamp when the task was created.
			credentials (dict): Credentials of the user this task belongs to.
				TODO: Remove this
		Standalone:
			checklist (dict[]): The todo's checklist.
				keys: completed (bool), text (str), id (str)
			collapseChecklist (bool): Determines if a checklist will be
				displayed.
			completed (bool): Whether this daily has been checked off.
	"""
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.checklist = data['checklist']
		self.collapseChecklist = data['collapseChecklist']
		self.completed = data['completed']

	def createChecklist(self, text):
		"""Add an item to the task's checklist.

		text: The text of the checklist item
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist"
		payload = {"text": text}
		response = postUrl(url, self.credentials, payload)
		self.checklist.append(text)
		return(response)

	def deleteChecklist(self, itemId):
		"""
		Task - Delete a checklist item from a task

		Args:
			itemId (str): The checklist item id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		response = deleteUrl(url, self.credentials)
		self.checklist.remove(itemId)
		return(response)

	def scoreChecklist(self, itemId):
		"""Score a checklist item

		Args:
			itemId (str): The checklist item id.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId + "/score"
		return(postUrl(url, self.credentials))

	def updateChecklist(self, itemId, text):
		"""Update a checklist item

		Args:
			itemId (str): The checklist item id.
			text (str): The text that will replace the current checkitem text.

		Returns:
			A JSON response object.
			Keys: userV, notifications, data, appVersion, success.

		Todo:
			Test.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		payload = {"text": text}
		return(putUrl(url, self.credentials, payload))

class reward(task):
	"""Habitica reward class. Inherits attributes and functions from Task.

	Note:
		End users should create task lists through User objects. Create a User
		and call user.initTasks(). This will automatically populate the User
		object's habits, dailys, todos, rewards, and completdTodos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task's id. Optional if [data] is supplied. Either
			[data] or [taskId] must be given.
		data (JSON): Optional JSON object containing the data for this
			task. If this option is not taken, the data will be found with
			an extra API call. Either [data] or [taskId] must be given.
			default: None

	Attributes:
		Inherited:
			data (JSON): Response object containing the data for this task.
			group (dict): Data relevant to paid group plans.
				keys: 'approval', 'assignedUsers', 'sharedCompletion'
			tags (list): A list of tag ids. To get a dictionary of tagIds and
				tagNames, use the tag module: getTags(credentials).
			text (str): The text of the task.
			challenge (dict): Data related to this task's challenge (if any).
				keys: taskId, id, shortName, broken
			userId (str): The user id of the task's related user.
			value (float): The task value for todos, dailys, and habits. Gold
				cost for rewards. See here for more info on task value:
				https://habitica.fandom.com/wiki/Task_Value
			id (str): The task id.
			priority (float): The difficulty of the task. 0.1: Trivial. 1: Easy.
				1.5: Medium. 2: Hard.
			notes (str): The notes section of this task.
			updatedAt (str): Timestamp when the task was last modified.
			_id (str): The task id.
			type (str): One of: habit, daily, todo, reward, completedTodo.
			reminders (list): A list of dictionaries of reminders.
			 	keys: id, time.
			createdAt (str): Timestamp when the task was created.
			credentials (dict): Credentials of the user this task belongs to.
				TODO: Remove this
		Standalone:
			No standalone attributes.
	"""
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)

class completedTodo(task):
	"""Completed todo class. Inherits attributes and functions from Task.

	Note:
		End users should create task lists through User objects. Create a User
		and call user.initTasks(). This will automatically populate the User
		object's habits, dailys, todos, rewards, and completdTodos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task's id. Optional if [data] is supplied. Either
			[data] or [taskId] must be given.
		data (JSON): Optional JSON object containing the data for this
			task. If this option is not taken, the data will be found with
			an extra API call. Either [data] or [taskId] must be given.
			default: None

	Attributes:
		Inherited:
			data (JSON): Response object containing the data for this task.
			group (dict): Data relevant to paid group plans.
				keys: 'approval', 'assignedUsers', 'sharedCompletion'
			tags (list): A list of tag ids. To get a dictionary of tagIds and
				tagNames, use the tag module: getTags(credentials).
			text (str): The text of the task.
			challenge (dict): Data related to this task's challenge (if any).
				keys: taskId, id, shortName, broken
			userId (str): The user id of the task's related user.
			value (float): The task value for todos, dailys, and habits. Gold
				cost for rewards. See here for more info on task value:
				https://habitica.fandom.com/wiki/Task_Value
			id (str): The task id.
			priority (float): The difficulty of the task. 0.1: Trivial. 1: Easy.
				1.5: Medium. 2: Hard.
			notes (str): The notes section of this task.
			updatedAt (str): Timestamp when the task was last modified.
			_id (str): The task id.
			type (str): One of: habit, daily, todo, reward, completedTodo.
			reminders (list): A list of dictionaries of reminders.
			 	keys: id, time.
			createdAt (str): Timestamp when the task was created.
			credentials (dict): Credentials of the user this task belongs to.
				TODO: Remove this
		Standalone:
			checklist (dict[]): The todo's checklist.
				keys: completed (bool), text (str), id (str)
			collapseChecklist (bool): Determines if a checklist will be
				displayed.
			completed (bool): Whether this daily has been checked off.
			dateCompleted (str): Timestamp when the todo was completed.
	"""
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.checklist = data['checklist']
		self.collapseChecklist = data['collapseChecklist']
		self.completed = data['completed']
		self.dateCompleted = data['dateCompleted']

def getTaskList(credentials, taskType):
	"""Get a list of task objects.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskType (str): one of habits, dailys, todos, rewards, completedTodos

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	data = getTasks(credentials, taskType)['data']
	if taskType == 'habits':
		return([habit(credentials, data=i) for i in data])
	if taskType == 'dailys':
		return([daily(credentials, data=i) for i in data])
	if taskType == 'todos':
		return([todo(credentials, data=i) for i in data])
	if taskType == 'rewards':
		return([reward(credentials, data=i) for i in data])
	if taskType == 'completedTodos':
		return([completedTodo(credentials, data=i) for i in data])


def addTag(credentials, taskId, tagId):
	"""Add a tag to a task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		tagId (str): The tag id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/tags/" + tagId
	payload = {"taskId": taskId, "tagId": tagId}
	return(postUrl(url, credentials, payload))

def createChecklist(credentials, taskId, text):
	"""Add an item to the task's checklist.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		text (str): The text of the checklist item.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist"
	payload = {"text": text}
	return(postUrl(url, credentials, payload))

def approveTask(credentials, taskId, userId):
	"""Approves a user assigned to a group task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		userId (str): The id of the user that will be approved.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/approve/" + userId
	return(postUrl(url, credentials))

def assignTask(credentials, taskId, assignedUserId):
	"""Assigns a user to a group task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		assignedUserId (str): The id of the user that will be assigned to the
			task.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/assign/" + assignedUserId
	return(postUrl(url, credentials))

def createChallengeTask(credentials, challengeId, text, taskType, alias = None,
		attribute = None, collapseChecklist = False, notes = None, date = None,
		priority = 1, reminders = None, frequency = "weekly", repeat = True,
		everyX = 1, streak = 0, startDate = None, up = True, down = True,
		value = 0):
	"""Create a new task belonging to a challenge.

	Can be passed an object to create a single task or an array of objects to
	create multiple tasks.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		text (str): The text to be displayed for the task.
		taskType (str): One of: "habit", "daily", "todo", "reward".
		alias (str): Optional. Alias to assign to task.
		attribute (str): Optional. User's attribute (stat) to use.
			Allowed values: "str", "int", "per", "con"
		collapseChecklist (bool): Optional. Determines if the checklist will be
			displayed.
			Default value: false
		notes (str): Optional. Extra notes.
		date (str): Optional. Due date to be shown in task list. Only valid
			for type "todo."
		priority (float): Optional. Difficulty, options are 0.1, 1, 1.5, 2;
			eqivalent of Trivial, Easy, Medium, Hard.
			Default value: 1
			Allowed values: "0.1", "1", "1.5", "2"
		reminders (str[]): Optional. Array of reminders, each an object that
			must include: a UUID, startDate and time.
			For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3",
			"startDate":"1/16/17","time":"1/16/17" }
		frequency (str): Optional. Value "weekly" enables "On days of the week",
			value "daily" enables "EveryX Days". Only valid for type "daily".
			Default value: weekly
			Allowed values: "weekly", "daily"
		repeat (dict): Optional. List of objects for days of the week. Days
			that are true will be repeated upon. Only valid for type "daily".
			Any days not specified will be marked as true. Days are: su, m, t,
			w, th, f, s. Value of frequency must be "weekly". For example, to
			skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
			Default value: true
		everyX (float): Optional. Value of frequency must be "daily". The
			number of days until this daily is available again.
			Default value: 1
		streak (int): Optional. Number of days that the task has consecutively
			been checked off. Only valid for type "daily"
			Default value: 0
		startDate (str): Optional. Date when the task will first become
			available. Only valid for type "daily".
		up (bool): Optional. Only valid for type "habit." If true, enables the
			"+" under "Directions/Action" for "Good habits."
			Default value: true
		down (bool): Optional. Only valid for type "habit." If true, enables
			the "-" under "Directions/Action" for "Bad habits."
			Default value: true
		value (float): Optional. Only valid for type "reward." The cost in gold
			of the reward.
			Default value: 0

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
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
	return(postUrl(url, credentials, payload))

def getTasks(credentials, taskType = None):
	"""Get a user's tasks.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskType (str): One of: "habit", "daily", "todo", "reward".

	Returns:
		A JSON response object. The returned object's structure depends on the
		type of task. Keys are listed below:
		todos keys: attribute, checklist, group, collapseChecklist, tags, text,
			challenge, userId, value, id, priority, completed, notes, updatedAt,
			_id, type, reminders, createdAt
		dailys keys: streak, startDate, isDue, attribute, userId, frequency,
			updatedAt, id, createdAt, daysOfMonth, group, collapseChecklist,
			priority, text, type, repeat, tags, checklist, completed, nextDue,
			weeksOfMonth, yesterDaily, challenge, reminders, everyX, value, _id,
			notes, history
		habits keys: attribute, counterUp, group, tags, down, text, challenge,
			counterDown, userId, up, value, id, priority, frequency, notes,
			updatedAt, _id, type, reminders, createdAt, history
		rewards keys: attribute, group, tags, text, challenge, userId, value,
			id, priority, notes, updatedAt, _id, type, reminders, createdAt
		completedTodos keys: attribute, dateCompleted, checklist, group,
			collapseChecklist, tags, text, challenge, userId, value, id,
			priority, completed, notes, updatedAt, _id, type, reminders,
			createdAt

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/user"
	else:
		url = "https://habitica.com/api/v3/tasks/user?type=" + taskType
	return(getUrl(url, credentials))

def createGroupTask(credentials, groupId, data):
	"""Create a new task belonging to a group.

	Can be passed an object to create a single task or an array of objects to
	create multiple tasks.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The id of the group the new task(s) will belong to.
		data (dict): The data of the task to create. I don't have a way to test
			this, so I have no idea what to use here.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.

	Todo:
		I guess the payload needs to be a task object. I have no way to test
		this. I think __dict__ of a task object would work.
	"""
	url = "https://habitica.com/api/v3/tasks/group/" + groupId
	payload = data
	return(postUrl(url, credentials, payload))

def createTask(credentials, text, taskType, tags = None, alias = None,
		attribute = None, collapseChecklist = False, notes = None, date = None,
		priority = 1, reminders = None, frequency = "weekly", repeat = True,
		everyX = 1, streak = 0, startDate = None, up = True, down = True,
		value = 0):
	"""Create a new task belonging to the user.

	Can be passed an object to create a single task or an array of objects to
	create multiple tasks. TODO: Support this feature.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		text (str): The text to be displayed for the task.
		taskType (str): Task type.
			Allowed values: "habit", "daily", "todo", "reward"
		tags (str[]): Optional. Array of UUIDs of tags.
		alias (str): Optional. Alias to assign to task.
		attribute (str): Optional. User's attribute to use.
			Allowed values: "str", "int", "per", "con"
		collapseChecklist (bool): Optional. Determines if a checklist will be
			displayed.
			Default value: false
		notes (str): Optional. Extra notes.
		date (str): Optional. Due date to be shown in task list. Only valid for
			type "todo."
		priority (float): Optional. Difficulty, options are 0.1, 1, 1.5, 2;
			eqivalent of Trivial, Easy, Medium, Hard.
			Default value: 1
			Allowed values: "0.1", "1", "1.5", "2"
		reminders (str[]): Optional. Array of reminders, each an object that
		 	must include: a UUID, startDate and time.
			Example: {"id":"ed427623-9a69-4aac-9852-13deb9c190c3",
				"startDate":"1/16/17","time":"1/16/17" }
		frequency (str): Optional. Value "weekly" enables "On days of the week",
			value "daily" enables "EveryX Days". Only valid for type "daily".
			Default value: weekly
			Allowed values: "weekly", "daily"
		repeat (dict[]): Optional. List of objects for days of the week, Days
			that are true will be repeated upon. Only valid for type "daily".
			Any days not specified will be marked as true. Days are: su, m, t,
			w, th, f, s. Value of frequency must be "weekly". For example, to
			skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
			Default value: true
		everyX (int): Optional. The number of days until this daily task is
			available again. Value of frequency must be "daily".
			Default value: 1
		streak (int): Optional. Number of days that the task has consecutively
			been checked off. Only valid for type "daily".
			Default value: 0
		startDate (str): Optional. Date when the task will first become
			available. Only valid for type "daily".
		up (bool): Optional. Only valid for type "habit." If true, enables the
			"+" under "Directions/Action" for "Good habits."
			Default value: true
		down (bool): Optional. Only valid for type "habit." If true, enables
			the "-" under "Directions/Action" for "Bad habits."
			Default value: true
		value (float): Optional. Only valid for type "reward." The cost in gold
			of the reward.
			Default value: 0

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.

	Todo:
		Test the optional arguments.
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
	return(postUrl(url, credentials, payload))

def deleteChecklist(credentials, taskId, itemId):
	"""Delete a checklist item from a task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		itemId (str): The checklist item id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId
	return(deleteUrl(url, credentials))

def removeTag(credentials, taskId, tagId):
	"""Delete a tag from a task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		tagId (str): The tag id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/tags/" + tagId
	return(deleteUrl(url, credentials))

def deleteTask(credentials, taskId):
	"""Delete a task given its id.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	return(deleteUrl(url, credentials))

def clearCompletedTodos(credentials):
	"""Delete user's completed todos.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/clearCompletedTodos"
	return(postUrl(url, credentials))

def getChallengeTasks(credentials, challengeId, taskType = None):
	"""Get a challenge's tasks.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The id of the associated challenge.
		taskType (str) Optional. Filter returned object to one type of task.
			Allowed values: "habits", "dailys", "todos", "rewards".

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/challenge/" + challengeId
	else:
		url = "https://habitica.com/api/v3/tasks/challenge/" + challengeId + "?type=" + taskType
	return(getUrl(url, credentials))

def getGroupApprovals(credentials, groupId):
	"""Get a group's approvals.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The id of the group from which to retrieve the approvals.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/approvals/group/" + groupId
	return(getUrl(url, credentials))

def getGroupTasks(credentials, groupId, taskType = None):
	"""Get a group's tasks.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The id of the group from which to retrieve the approvals.
		taskType (str) Optional. Filter returned object to one type of task.
			Allowed values: "habits", "dailys", "todos", "rewards".

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/group/" + groupId
	else:
		url = "https://habitica.com/api/v3/tasks/group/" + groupId + "?type=" + taskType
	return(getUrl(url, credentials))

def getTask(credentials, taskId):
	"""Get a task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	return(getUrl(url, credentials))

def needsWork(credentials, taskId, userId):
	"""Group task needs more work.

	Mark an assigned group task as needeing more work before it can be approved.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		userId (str): The id of the assigned user.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/needs-work/" + userId
	return(postUrl(url, credentials))

def moveGroupTask(credentials, groupId, taskId, position):
	"""Move a group task to a specified position.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		groupId (str): The id of the group from which to retrieve the approvals.
		taskId (str): The task id or alias.
		position (int): Where to move the task (-1 means push to bottom). First
			position is 0.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/group/" + groupId + "/tasks/" + taskId + "/move/to/" + str(position)
	return(postUrl(url, credentials))

def moveTask(credentials, taskId, position):
	"""Move a task to a new position.

	Note:
		Completed To-Dos are not sortable, do not appear
		in user.tasksOrder.todos, and are ordered by date of completion.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		position (int): Where to move the task (-1 means push to bottom). First
			position is 0.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/move/to/" + str(position)
	return(postUrl(url, credentials))

def scoreChecklist(credentials, taskId, itemId):
	"""Score a checklist item.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		itemId (str): The checklist item id.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId + "/score"
	return(postUrl(url, credentials))

def scoreTask(credentials, taskId, direction):
	"""Score a task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		direction (str): The direction for scoring the task.
			Allowed values: "up", "down".

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/score/" + direction
	return(postUrl(url, credentials))

def unassignTask(credentials, taskId, assignedUserId):
	"""Unassign a user from a group task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		assignedUserId (str): The id of the user that will be unassigned from
			the task.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/unassign/" + assignedUserId
	return(postUrl(url, credentials))

def unlinkTask(credentials, taskId, keep):
	"""Unlink a challenge task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		keep (str): Optional. Specifies if the task should be kept or removed.
			Allowed values: 'keep', 'remove'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/unlink-one/" + taskId + "?keep=" + keep
	return(postUrl(url, credentials))

def unlinkTasks(credentials, challengeId, keep=None):
	"""Unlink a challenge task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		challengeId (str): The challenge id.
		keep (str): Optional. Specifies if the task should be kept or removed.
			Allowed values: 'keep', 'remove'.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	if keep == None:
		url = "https://habitica.com/api/v3/tasks/unlink-all/" + challengeId
	else:
		url = "https://habitica.com/api/v3/tasks/unlink-all/" + challengeId + "?keep=" + keep
	return(postUrl(url, credentials))

def updateChecklist(credentials, taskId, itemId, text):
	"""Update a checklist item.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		itemId (str): The checklist item id.
		text (str): The text that will replace the current checkitem text.

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId
	payload = {"text": text}
	return(putUrl(url, credentials, payload))

def updateTask(credentials, taskId, text = None, attribute = None,
		collapseChecklist = False, notes = None, date = None, priority = 1,
		reminders = None, frequency = "weekly", repeat = True, everyX = 1,
		streak = 0, startDate = None, up = True, down = True, value = 0):
	"""Update a task.

	Args:
		credentials (dict): Formatted dictionary of user id and api key. If a
			user object has already been created, use user.credentials.
			format: {'x-api-user': "user_id_here", 'x-api-key': "api_key_here"}
		taskId (str): The task id or alias.
		text (str): Optional. The text to be displayed for the task.
		attribute (str): Optional. User's attribute to use.
			Allowed values: "str", "int", "per", "con".
		collapseChecklist (bool): Optional. Determines if a checklist will be
			displayed.
			Default value: false
		notes (str): Optional. Extra notes.
		date (str): Optional. Due date to be shown in task list. Only valid for
			type "todo."
		priority (float): Optional. Difficulty, options are 0.1, 1, 1.5, 2;
			eqivalent of Trivial, Easy, Medium, Hard.
			Default value: 1
			Allowed values: "0.1", "1", "1.5", "2"
		reminders (str[]): Optional. Array of reminders, each an object that
			must include: a UUID, startDate and time.
			For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3",
				"startDate":"1/16/17","time":"1/16/17" }
		frequency (str): Optional. Value "weekly" enables "On days of the week",
			value "daily" enables "EveryX Days". Only valid for type "daily".
			Default value: weekly
			Allowed values: "weekly", "daily"
		repeat (str): Optional. List of objects for days of the week, Days that
			are true will be repeated upon. Only valid for type "daily". Any
			days not specified will be marked as true. Days are: su, m, t, w,
			th, f, s. Value of frequency must be "weekly". For example, to skip
			repeats on Mon & Fri: "repeat":{"f":false,"m":false}
			Default value: true
		everyX (int): Optional. Value of frequency must be "daily", the number
			of days until this daily task is available again.
			Default value: 1
		streak (int): Optional. Number of days that the task has consecutively
			been checked off. Only valid for type "daily".
			Default value: 0
		startDate (str): Optional. Date when the task will first become
			available. Only valid for type "daily".
		up (bool): Optional. Only valid for type "habit." If true, enables the
			"+" under "Directions/Action" for "Good habits."
			Default value: true
		down (bool): Optional. Only valid for type "habit." If true, enables the
			"-" under "Directions/Action" for "Bad habits."
			Default value: true
		value (float): Optional. Only valid for type "reward." The cost in gold
			of the reward.
			Default value: 0

	Returns:
		A JSON response object.
		Keys: userV, notifications, data, appVersion, success.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	payload = {}
	if text != None:
		payload["text"] = text
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
	return(putUrl(url, credentials, payload))
