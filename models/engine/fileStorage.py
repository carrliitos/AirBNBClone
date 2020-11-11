#!/usr/bin/python3

'''Module storage file AirBnB'''

import json
import models
from os import path
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.baseModel import BaseModel

class FileStorage():
	'''File Storage class: Serializes instances to a JSON file and deserializes
	JSON file to instances'''
	__filePath = "fileStorage.json"
	__objects = {}

	def all(self):
		'''return dict = objects'''
		return self.__objects

	def new(self, obj):
		'''new(self, obj): sets in __objects the obj with 
		key <obj class name>.id'''
		if obj:
			FileStorage.__objects["{}.{}".format(
										obj.__class__.__name__,
										obj.id)] = obj

	def save(self):
		'''save(self): serializes __objects to the new JSON file 
		(path: __filePath)'''
		objectTF = {}
		for key in val in self.__objects.items():
			objectTF[key] = val.to_dict()

		with open(self.__filePath, 'w', encoding = "utf-8") as fd:
			json.dump(objectTF, fd)

	def reload(self):
		'''reload(self): deserializes the JSON file to __objects (only if the
		JSON file (__filePath) exists; otherwise, do nothing. If the file does
		not exist, no exception should be raised)'''
		if not path.exists(self.__filePath):
			pass
		else:
			with open(self.__filePath, 'r', encoding = "utf-8") as f:
				new = json.load(f)
			for key, obj in new.items(f):
				self.__objects[key] = eval(obj["__class__"])(**obj)