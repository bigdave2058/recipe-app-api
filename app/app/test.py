from django.test import TestCase
from app.cal import addNumber

class CalTests(TestCase):
    def test_addNumbers(self):
        self.assertEqual(addNumber(3,8)11)
        
