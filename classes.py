from habotica import getAllTasks
from habotica import getTasks
import inspect

# Create a user. Contains login credentials of user_id and api_key.
class user:
	def __init__(self, user_id, api_key):
		self.credentials = {'x-api-user': user_id, 'x-api-key': api_key}

# Create a task object from a JSON string containing a task's data
class task:
	def __init__(self, inStr):
		keyDict = inStr.keys()
		for key in keyDict:
			exec("self." + key + "= inStr['" + key + "']")

class habit(task):
	pass

class daily(task):
	pass

class todo(task):
	pass

class reward(task):
	pass
