#!/usr/bin/env python
# coding: utf-8

# In[1]:


# factorial.py
# Program to compute the factorial of a number

def factorial(number):
	"""This function calculates the factorial of any number"""
	if number < 0 :
		raise ValueError('You cannot use a negtive number')
	elif type(number) != int :
		raise ValueError('The factorial of 0 is 1')
	elif number == 1 :
		return 1 # returns the factorial of 1
	elif number == 0 :
		return 1 # returns the factorial of 0
	else:
		return number * factorial(number-1) # calculates factorial
if __name__ == "__main__":

	factorial(5)
