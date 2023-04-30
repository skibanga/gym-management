# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date

class GymLockerBooking(Document):
	def before_save(self):

		today_date = date.today()
		email = frappe.session.user

		# checking user membership well as activeness
		self.booked_by = check_membership(email, today_date)

		# checking the has been boocked
		exists = frappe.db.exists(
		"Gym Locker Booking",
			{
			"locker": self.locker,
			},
		)
		if exists:
		    frappe.throw(f'{self.locker} is already boooked')    

def check_membership(email, today_date):
	exists = frappe.db.sql(
		f"""
		SELECT
		   gm.name,
		   gms.to_date,
		   gm.email 
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
		
	return exists[0].email


@frappe.whitelist()		
def get_locker(locker):
	return frappe.db.get_doc("Gym Locker",locker)
