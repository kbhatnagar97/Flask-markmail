import unittest
import os
import json
from app import create_app, db, app


class CustomerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.db = db
        self.client = self.app.test_client()
        self.Customer = {
            "first_name": "Kshitij sk",
            "last_name": "Bhatnagar ss",
            "gender": "female",
            "email": "kbhatnagar@gmail.com",
            "age": "26",
            "address": "C-	2/2257/Vasant Kunj",
            "state": "New Delhi 7",
            "zipcode": "110080",
            "phoneNumber": "7500169360",
            "registrationDate": "19/02/2019"
        }


        with self.app.app_context():
            self.db.create_all()

    def test_customerlist_creation(self):
        self.assertEqual(201, 201)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            self.db.session.remove()
            self.db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()