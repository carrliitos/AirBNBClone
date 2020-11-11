#!/usr/bin/python3

'''User module'''

from models.baseModel import BaseModel

class User(BaseModel):
	'''User class'''
	email = ""
	password = ""
	firstName = ""
	lastName = ""