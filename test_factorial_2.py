#!/usr/bin/env python
#coding: utf-8

# In[2]:

#unit test

import unittest
from factorial_c import factorial

class Test(unittest.TestCase):
	
	def test_for_number(self):
		self.assertEqual(24, factorial(4))
		self.assertEqual(120, factorial(5))
		self.assertEqual(720, factorial(6))

	def test_if_zero(self):
		self.assertEqual(1, factorial(0))

	def test_is_invalid (self):
		with self.assertRaises(ValueError):
			factorial(-4)
		with self.assertRaises(ValueError):
			factorial(2.5)

if __name__ == "__main__":
	unittest.main()
