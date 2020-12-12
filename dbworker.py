import shelve
import config

def get_current_status(user_id):
	with shelve.open(config.db_file) as db:
		try:
			return db[str(user_id)]
		except KeyError:
			return config.Status.START.value

def set_status(user_id, value):
	with shelve.open(config.db_file) as db:
		try:
			db[str(user_id)] = value
			return True
		except:
			return False