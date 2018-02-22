import unittest
import sys
from .wcUser import wcUser


class BusinessTestCase(unittest.TestCase):
    def setUp(self):
        self.user = wcUser()

    def test_business_initialy_empty(self):
        self.assertEqual(self.user.business, {})

    def test_create_business_sucsscessfully(self):
        initial_room_count = len(self.user.business)
        saloon = self.user.create_business('Saloon')
        self.assertTrue(saloon)
        new_room_count = len(self.user.business)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_business(self):
        self.user.business = {}
        try:
            pass
        except Exception as e:
            raise self.assertEqual(self.user.create_business('recreation', 'hotels'),{'recreation': ['hotel']})

    def test_create_business_when_list_already_exists(self):
        self.user.business = {'recreation': ['hotel']}
        try:
            pass
        except Exception as e:
            raise self.assertEqual(self.user.create_business('recreation', 'hotel'),'Business already created!', msg='Business already created!')

    def test_update_business(self):
        self.user.business = {'recreation': ['hotel']}
        self.assertEqual(self.user.update_business(
            'recreation', 'beach_resort'), {'beach_resort': ['hotel']})

    def test_updating_non_existing_business(self):
        self.user.business = {'recreation': ['hotel']}
        try:
            pass
        except Exception as e:
            raise self.assertEqual(self.user.update_business('re-creation','hotel'),'Business review does not exist ', msg='Business review does not exist')

    def test_update_business_description(self):
        self.user.business = {'recreation': ['hotel']}
        self.assertEqual(self.user.update_business_description(
            'recreation', 'hotel', 'hotel_and_resturant'), {'recreation': ['hotel_and_resturant']})

    def test_updating_non_existing_business_description(self):
        self.user.business = {'recreation': ['hotel']}
        try:
            pass
        except Exception as e:
            raise self.assertEqual(self.user.update_business_description('recreation', 'hotl', 'hotels'),
                         'Business description not in system', msg='Business description not in system')

    def test_read_business_description(self):
        self.user.business = {'recreation': ['hotel', '5-star']}
        self.assertEqual(self.user.read_business('recreation'), ['hotel', '5-star'])

    def test_delete_business(self):
        self.user.business = {'recreation': ['hotel', '5-star'], 'fin_tech': ['consultation', 'software_development']}
        self.assertEqual(self.user.delete_business(
            'recreation'), {'fin_tech': ['consultation', 'software_development']})

    def test_delete_business_description(self):
        self.user.business = {'recreation': ['hotel', '5-star'], 'fin_tech': ['consultation', 'software_development']}
        self.assertEqual(self.user.delete_business_description('recreation', 'hotel'), {
                         'recreation': ['5-star'], 'fin_tech': ['consultation', 'software_development']})
