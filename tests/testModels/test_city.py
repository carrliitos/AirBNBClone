#!/usr/bin/python3

"""Test City"""

from models.city import City
from models import storage
import unittest
import datetime
import time
import os
import json

base = City()

class Test_City(object):
	"""docstring for Test_City class"""
	def test_attr(self):
		base.name = "Salazar"
		base.number = 52000

		self.assertAlmostEqual(base.name, "Salazar")