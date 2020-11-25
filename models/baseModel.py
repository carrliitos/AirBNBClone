#!/usr/bin/python3

'''Module Base Model, the parent class'''

from datetime import datetime
from uuid import uuid4
import models

class BaseModel():
	'''Class base for all project'''
	def __init__(self, *args, **kwargs):
		'''Initialize class with UUID and
		createdAt:
			datetime - assign with the current datetime when an instance is
			created
		updatedAt:
			datetime - assign with the current datetime when an instance is 
			created and it will be updated every time you change your object'''
		if len(kwargs) is 0:
			self.id = str(uuid4())
			self.createdAt = datetime.now()
			self.updatedAt = datetime.now()
			models.storage.new(self)
		else:
			for key, val in kwargs.items():
				if "createdAt" == key:
					self.createdAt = datetime.strptime(kwargs["createdAt"],
														"%Y-%m-%dT%H:%M:%S.%f")
				elif "updatedAt" == key:
					self.updatedAt = datetime.strptime(kwargs["updatedAt"],
														"%Y-%m-%dT%H:%M:%S.%f")
				elif not key == "__class__":
					setattr(self, key, val)

	def __str__(self):
		'''Returns a string'''
		return ("[{}] ({}) {}".format(self.__class__.__name__, 
									self.id, self.__dict__))

	def save(self):
		'''Save a file'''
		self.updatedAt = datetime.now()
		models.storage.save()

	def toDict(self):
		'''Create a dictionary with argument'''
		nDict = dict(self.__dict__)
		nDict["__class__"] = self.__class__.__name__
		nDict["createdAt"] = self.createdAt.isoformat()
		nDict["updatedAt"] = self.updatedAt.isoformat()
		return nDict