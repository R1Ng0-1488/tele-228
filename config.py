import enum

token = '1288424141:AAGSeermUxi5AtwKIG6a01Bcw5EF7X0LmHo'
db_file = 'shelve.db'


class Status(enum.Enum):
	START = '0'
	SOSAL = '1'
	NASOSAL = '2'
	END = '3'