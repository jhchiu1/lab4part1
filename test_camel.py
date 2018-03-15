import unittest
from unittest.mock import patch
import camel

class TestCamelCase(unittest.TestCase):

	def test_camel_case(self):
		self.assertEqual('helloWorld', camel.camel_case('Hello World'))

	def test_camel_case1(self):
		self.assertEqual('', camel.camel_case(''))

	def test_camel_case_spaces(self):
		self.assertEqual('helloWorld', camel.camel_case('	Hello   World   '))
		
	def test_numbers(self):
        	self.assertEqual('123', camel.camel_case('123'))

	def test_symbols(self):
    		self.assertEqual('@@#^^', camel.camel_case('@@# ^ ^'))

if __name__ == '__main__':
    unittest.main()
