#!/usr/bin/python3

from os.path import basename
from models.baseModel import BaseModel
from models import storage
import unittest
import datetime
import json
import os

# Global variable
base = BaseModel()

class TestBaseModel(unittest.TestCase):
	'''BaseModel test
	Args:
		unittest (base class)
	'''
	def test_doc(self):
		'''Tests documentation'''
		self.assertIsNotNone(("models.baseModel").__doc__)
		self.assertIsNotNone(base.__doc__)
		self.assertIsNotNone(base.__init__.__doc__)
		self.assertIsNotNone(base.save.__doc__)
		self.assertIsNotNone(base.toDict.__doc__)
		self.assertIsNotNone(base.__str__.__doc__)

	def test_attr(self):
		'''Create new attributes test'''
		base.name = "Benzon"
		base.number = 52000

		self.assertEqual(base.name, "Benzon")
		self.assertEqual(type(base.id), str)
		self.assertAlmostEqual(base.number, 52000)
		self.assertEqual(type(base.createdAt), datetime.datetime)
		self.assertEqual(type(base.updatedAt), datetime.datetime)

	def test_update(self):
		'''test for proper updates'''
		a = str(base.updatedAt)
		b = str(base.createdAt)
		base.name = "Salazar"
		base.save()

		self.assertNotEqual(str(base.updatedAt), a)
		self.assertEqual(str(base.createdAt), b)

	def test_dict(self):
		'''Tests dictionary'''
		base2 = base.toDict()

		self.assertEqual(base2["updatedAt"], base.updatedAt.isoformat())
		self.assertEqual(base2["__class__"], "BaseModel")
		self.assertNotIn("__class__", base.__dict__)

	def test_save(self):
		'''Tests the save method'''
		base.save()
		with open("fileStorage.json", mode="r", encoding="UTF-8") as f:
			d = json.load(f)
		for item in d:
			if base.id in item:
				d = d[item]

		self.assertDictEqual(d, base.toDict())

	def test_save2(self):
		'''Test save using method provided by peer in BOG'''
		base2 = datetime.datetime.now().replace(microsecond=0)
		base.save()

		self.assertEqual(base.updatedAt.replace(microsecond=0), base2)

	def test_new_model(self):
		'''Tests creation of new model with dictionary'''
		base3 = base.toDict()
		base2 = BaseModel(**base3)

		self.assertFalse(base is base2)
		self.assertDictEqual(base.toDict(), base2.toDict())

	def test_exec_permission(self):
		'''Test for execution permissions'''
		self.assertFalse(os.access("models/baseModel.py", os.X_OK))
		self.assertFalse(os.access("models/baseModel.py", os.R_OK))
		self.assertFalse(os.access("models/baseModel.py", os.W_OK))

	def test_is_an_instance(self):
		'''Tests for an instance'''
		BaseModelInstance = BaseModel()

		self.assertIsInstance(BaseModelInstance, BaseModel)

	def test_different_id(self):
		'''Test if each instance that is created has a unique id'''
		instance1 = BaseModel()
		instance2 = BaseModel()

		self.assertNotEqual(instance1, instance2)