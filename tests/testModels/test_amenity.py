#!/usr/bin/python3

'''Test class for Amenity'''

from models.amenity import Amenity
import unittest
import datetime
import time
import os
import json
from models import storage

class Test_Amenity(unittest.TestCase):
	def test_doc(self):
		'''Tests docstring'''
		self.assertIsNotNone(("models.base_model".__doc__))
		self.assertIsNotNone(Amenity.__doc__)
		self.assertIsNotNone(Amenity.__init__.__doc__)

	def test_attr(self):
		'''Tests attributes'''
		base = Amenity()
		base.name = "Salazar"
		base.number = 52000

		self.assertAlmostEqual(base.name, "Salazar")
		self.assertAlmostEqual(base.number, 52000)
		self.assertEqual(type(base.id), str)
		self.assertEqual(type(base.createdAt), datetime.datetime)
		self.assertEqual(type(base.updatedAt), datetime.datetime)

	def test_type(self):
		'''Test type class'''
		base = Amenity()
		self.assertAlmostEqual(type(base), Amenity)

	def test_updated_at(self):
		'''Test updatedAt'''
		base = Amenity()
		create = str(base.createdAt)
		start = str(base.updatedAt)
		base.name = "Salazar"
		base.save()

		self.assertNotEqual(str(base.updatedAt), start)
		self.assertEqual(str(base.createdAt), create)

	def test_to_dict(self):
		'''Tests dict'''
		base = Amenity()
		base2 = base.toDict()

		self.assertEqual(base2["updatedAt"], base.updatedAt.isoformat())
		self.assertEqual(base2["__class__"], "Amenity")
		self.assertNotIn("__class__", base.__dict__)

	def test_save(self):
		'''Tests save'''
		base = Amenity()
		base.save()
		with open("fileStorage.json", mode="r", encoding="UTF-8") as f:
			d = json.load(f)
		for item in d:
			if base.id in item:
				d = d[item]

		self.assertDictEqual(d, base.toDict())

	def test_new_model_dict(self):
		'''Tests new model with dictionary'''
		base = Amenity()
		dict1 = base.toDict()
		base2 = Amenity(**dict1)

		self.assertFalse(base is base2)
		self.assertDictEqual(base.toDict(), base2.toDict())

	def test_instance(self):
		'''Tests instance'''
		instanceTest = Amenity()

		self.assertIsInstance(instanceTest, Amenity)

	def test_permissions(self):
		'''Tests permissions'''
		self.assertFalse(os.access("models/amenity.py", os.X_OK))
		self.assertFalse(os.access("models/amenity.py", os.R_OK))
		self.assertFalse(os.access("models/amenity.py", os.W_OK))
		self.assertFalse(os.access("models/amenity.py", os.F_OK))

	def test_ids_maker(self):
		'''Tests to generate the ID'''
		option1 = Amenity()
		option2 = Amenity()

		self.assertNotEqual(option1, option2)