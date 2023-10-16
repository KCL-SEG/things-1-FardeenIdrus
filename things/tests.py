from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError
from django.db.models import Max

# Create your tests here.
class UserModelTestCase(TestCase):
    
    def setUp(self):
         self.user= User.objects.create_user(
           'thing',
            name = 'first_thing',
            description = 'description...',
            quantity = 10,
        )
    
    def test_valid_user(self):
        self.assert_user_is_valid()
            
    def test_name(self):
        self.user.name = ''
        self.assert_user_is_invalid()
            
            
    def assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('test should be valid')
            
    def test_name_can_be_30_characthers_long(self):
       author = User.objects.get(id=1)
       max_length =  User._meta.get_field('name').max_length 
       self.assertEqual(max_length,30)
        
    
    def test_description(self):
       author = User.objects.get(id=1)
       max_length =  User._meta.get_field('description').max_length
       self.assertEqual(max_length,120)
       
    def assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
    
        
            
        
            