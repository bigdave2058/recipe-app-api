from django.test import TestCase
from app.cal import addNumber, subtract,multiply

class CalTests(TestCase):
    def test_addNumbers(self):
        self.assertEqual(addNumber(3,8)11)

    def test_subtract(self):
        self.assertEqual(subtract(11,3)8)

    def test_multiply(self):
        self.assertEqual(subtract(11,3)8)


        
