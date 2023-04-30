# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from datetime import date
from frappe.model.document import Document

class GymSubscription(Document):
	def before_save(self):

		today_date = date.today()
		email = frappe.session.user
		check_membership(email, today_date)
		check_subscription(email)



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

def check_subscription(user):
	if frappe.db.exists("Gym Subscription", {"gym_member": user,}):
	    frappe.throw("You already have an active subscription")	

@frappe.whitelist()
def get_subscription_plan_fee(plan, doctype):
	fee = frappe.db.get_value(doctype, plan, 'fee')
	return fee				