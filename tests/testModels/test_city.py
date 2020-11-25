#!/usr/bin/python3

"""Test City"""
from models.city import City
from models import storage
import unittest
import datetime
import time
import os
import json

# Global variable
base = City()

class Test_City(unittest.TestCase):
	"""docstring for Test_City class"""
	def test_attr(self):
		base.name = "Salazar"
		base.number = 52000

		self.assertAlmostEqual(base.name, "Salazar")
		self.assertAlmostEqual(base.number, 52000)
		self.assertEqual(type(base.id), str)
		self.assertEqual(type(base.createdAt), datetime.datetime)
		self.assertEqual(type(base.updatedAt), datetime.datetime)

	def test_type(self):
		"""Tests type class"""
		self.assertAlmostEqual(type(base), City)

	def test_updated_at(self):
		"""Tests updatedAt"""
		create = str(base.createdAt)
		start = str(base.updatedAt)
		base.name = "Salazar"
		base.save()

		self.assertNotEqual(str(base.updatedAt), start)
		self.assertEqual(str(base.createdAt), create)

	def test_toDict(self):
		"""Tests dictionary"""
		base2 = base.toDict()

		self.assertEqual(base2["updatedAt"], base.updatedAt.isoformat())