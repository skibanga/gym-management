# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymTrainer(Document):
	def before_save(self):
		if not frappe.db.exists("Gym Trainer", {"first_name": self.first_name,"email": self.email}):
			self.create_new_user()

	def create_new_user(self):
		
		if not frappe.db.exists("User", {"first_name": self.first_name,"email": self.email}):
			user = frappe.get_doc({
				"doctype": "User",
				"first_name": self.first_name,
				"last_name": self.last_name,
				"email": self.email,
				# "send_welcome_email": 1,
				"username": self.email,
				"user_type": "Website User",
				}).insert(ignore_permissions=True)
			if user:
				role = frappe.get_doc({
					"doctype": "Has Role",
					"parent": user.name,
					"parenttype": "User",
					"parentfield": "roles",
					"role": "Gym Trainer"
					}).insert()
				if role:
					frappe.msgprint("Gym Trainer is created Successfully")
		else:
			pass
