#!/usr/bin/python3

"""Test City"""
from models.city import City
from models import storage
import unittest
import datetime
import time
import os
import json

class Test_City(unittest.TestCase):
	'''Test_City class'''
	def test_doc(self):
		'''Tests docstring'''
		self.assertIsNotNone(("models.baseModel".__doc__))
		self.assertIsNotNone(City.__doc__)
		self.assertIsNotNone(City.__init__.__doc__)

	def test_attr(self):
		'''Tests attributes'''
		base = City()
		base.name = "Salazar"
		base.number = 52000

		self.assertAlmostEqual(base.name, "Salazar")
		self.assertAlmostEqual(base.number, 52000)
		self.assertEqual(type(base.id), str)
		self.assertEqual(type(base.createdAt), datetime.datetime)
		self.assertEqual(type(base.updatedAt), datetime.datetime)

	def test_type(self):
		'''Test type class'''
		base = City()
		self.assertAlmostEqual(type(base), City)

	def test_updatedAt(self):
		'''Test updated at'''
		base = City()
		create = str(base.createdAt)
		start = str(base.updatedAt)
		base.name = "Salazar"
		base.save()

		self.assertNotEqual(str(base.updatedAt), start)
		self.assertEqual(str(base.createdAt), create)

	def test_to_dict(self):
		'''Tests dict'''
		base = City()
		base2 = base.toDict()

		self.assertEqual(base2["updatedAt"], base.updatedAt.isoformat())
		self.assertEqual(base2["__class__"], "City")
		self.assertNotIn("__class__", base.__dict__)

	def test_save(self):
		'''Tests save'''
		base = City()
		base.save()
		with open("fileStorage.json", mode="r", encoding="UTF-8") as f:
			d = json.load(f)
		for item in d:
			if base.id in item:
				d = d[item]

		self.assertDictEqual(d, base.toDict())

	def test_new_model_dict(self):
		'''Tests new model with dictionary'''
		base = City()
		dict1 = base.toDict()
		base2 = City(**dict1)

		self.assertFalse(base is base2)
		self.assertDictEqual(base.toDict(), base2.toDict())

	def test_instance(self):
		'''Tests instance'''
		instanceTest = City()

		self.assertIsInstance(instanceTest, City)

	def test_permissions(self):
		'''Tests permissions'''
		self.assertFalse(os.access("models/City.py", os.X_OK))
		self.assertFalse(os.access("models/City.py", os.R_OK))
		self.assertFalse(os.access("models/City.py", os.W_OK))
		self.assertFalse(os.access("models/City.py", os.F_OK))

	def test_ids_maker(self):
		'''Tests to generate the ID'''
		option1 = City()
		option2 = City()

		self.assertNotEqual(option1, option2)