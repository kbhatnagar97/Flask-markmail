from app import app
import unittest
import json

class MyTestCases(unittest.TestCase):
    def test_customer_insert(self):
        data= json.dumps({
            	"first_name" : "Kshitij sk",
                "last_name" : "Bhatnagar ss",
                "gender" : "female",
                "email" : "kbhatnagar@gmail.com",
                "age" : "26",
                "address" : "C-	2/2257/Vasant Kunj" ,
                "state" : "New Delhi 7",
                "zipcode" : "110080",
                "phoneNumber" : "7500169360",
                "registrationDate" : "19/02/2019"
        })

        my_test = app.test_client(self)
        response = my_test.post('/user', data=data,content_type="application/json")
        status_code = response.status_code
        self.assertEqual(status_code,200)

if __name__ == '__main__':
    unittest.main()