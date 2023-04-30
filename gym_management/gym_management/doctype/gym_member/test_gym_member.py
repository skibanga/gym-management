# Copyright (c) 2023, sydney and Contributors
# See license.txt

import frappe
# from frappe.tests.utils import FrappeTestCase
import unittest

# class TestGymMember(FrappeTestCase):

class TestGymMember(unittest.TestCase):
    def test_create_gym_member(self):
            doc = frappe.get_doc({
				"doctype": "Gym Member",
				"first_name":"test ",
				"last_name": "user",
				"email": "testuser@gmail.com",
				"age": "23",
				"sex": "Male",
				"phone_number": "123456",
				"address": "dsm"
			}).insert()
            self.assertTrue(
			frappe.db.exists(
				"Gym Member", {"first_name": "test", "email": "testuser@gmail.com"}
			)
		   )



	

	

