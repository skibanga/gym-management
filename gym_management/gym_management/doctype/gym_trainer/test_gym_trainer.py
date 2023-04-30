# Copyright (c) 2023, sydney and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymTrainer(FrappeTestCase):
	def test_create_gym_trainer(self):
            doc = frappe.get_doc({
				"doctype": "Gym Trainer",
				"first_name":"test ",
				"last_name": "trainer",
				"email": "testtrainer@gmail.com",
				"age": "23",
				"sex": "Male",
				"phone_number": "123456",
				"address": "dsm"
			}).insert()
            self.assertTrue(
			frappe.db.exists(
				"Gym Trainer", {"first_name": "test", "email": "testtrainer@gmail.com"}
			)
		   )

