from django.test import TestCase
from .models import User
# Create your tests here.
class UserTest(TestCase):

    def setUpTestData():
        # set up fake user using all attributes
        User.objects.create(name='John Doe')

    def test_user_name(self):
        # Get user object to test
        user = User.objects.get(id=1)
        # Get name metadata to query
        field_label = user._meta.get_field('name').verbose_name
        # Compare value to expected result 
        self.assertEqual(user.name, 'John Doe')

    def test_user_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)
