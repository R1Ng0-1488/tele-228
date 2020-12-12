import enum

token = ''
db_file = 'shelve.db'


class Status(enum.Enum):
	START = '0'
	SOSAL = '1'
	NASOSAL = '2'
	END = '3'