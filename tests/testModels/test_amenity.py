#!/usr/bin/python3

'''Test class for Amenity'''

from models.amenity import Amenity
import unittest
import datetime
import time
import os
import json
# from models import storage

class Test_Amenity(unittest.TestCase):
	def testattr(self):
		'''Tests attributes'''
		base = Amenity()
		base.name = "Salazar"
		base.number = 52000

		self.assertAlmostEqual(base.name, "Salazar")
		self.assertAlmostEqual(base.number, 52000)
		self.assertEqual(type(base.id), str)
		self.assertEqual(type(base.createdAt), datetime.datetime)
		self.assertEqual(type(base.updatedAt), datetime.datetime)