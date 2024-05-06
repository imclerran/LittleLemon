from django.test import TestCase
from Restaurant.models import MenuItem

class TestMenuItem(TestCase):
    def test_string_representation(self):
        item = MenuItem(title='Cheese Pizza', price=10.99, inventory=5)
        self.assertEqual(str(item), 'Cheese Pizza : $10.99')