#!/usr/bin/python3

'''Reviews module'''

from models.baseModel import BaseModel

class Review(BaseModel):
	'''Review Class
		Attributes:
			placeID = place ID
			userID = user id
			text = review description
	'''
	placeID = ""
	userID = ""
	test = ""