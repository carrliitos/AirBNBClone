#!/usr/bin/python3

'''Place Module'''

from models.baseModel import BaseModel

class Place(BaseModel):
	'''Class for Place
		Attributes:
			cityID = city id
			userID = user ID
			name = name input
			description = description
			numberRooms = number of rooms
			numberBathrooms = number of bathrooms
			maxGuest = maximum guests
			priceByNight = price for staying a night
			latitude = latitude
			longitude = longitude
			amenityIDs = list of amenity IDs
	'''
	cityID = ""
	userID = ""
	name = ""
	description = ""
	numberRooms = 0
	numberBathrooms = 0
	priceByNight = 0
	maxGuest = 0
	latitude = 0
	longitude = 0
	amenityIDs = []