# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from datetime import date
from frappe.model.document import Document

class GymClassBooking(Document):
	def before_save(self):
		
		today_date = date.today()
		
		# checking user membership well as activeness
		check_membership(frappe.session.user, today_date)
		self.check()
		self.booked_by = frappe.session.user
        
	def check(self):
		if not frappe.db.exists("Gym Class Booking",{"member": frappe.session.user,},):
			doc = frappe.get_doc("Gym Class", self.gym_class)
			if doc.capacity == 0:
				frappe.throw('Class is full')
			
			if doc.members_enrolled  == doc.capacity:
				frappe.throw('There are no available slots')
			
			members_enrolled = int(doc.members_enrolled) + 1
			frappe.db.set_value('Gym Class', self.gym_class, 'members_enrolled', members_enrolled)
		else:
			frappe.throw('You Cant Book A class twice')

	def on_trash(self):
		doc = frappe.get_doc("Gym Class", self.gym_class)
		members_enrolled = int(doc.members_enrolled) - 1
		frappe.db.set_value('Gym Class', self.gym_class, 'members_enrolled', members_enrolled)
		


def check_membership(email, today_date):
	exists = frappe.db.sql(
		f"""
		SELECT
		   gm.name,
		   gms.to_date 
		FROM   
		  `tabGym Member` gm
		INNER JOIN 
		  `tabGym Membership` gms
			ON  gm.name = gms.gym_member
		WHERE gm.email = '{email}'
		AND  gms.to_date > '{today_date}'
		""",as_dict=True
	)
	if not exists:
		frappe.throw('Your not an active member in our Gym. Please contact the admin to give you Membership')