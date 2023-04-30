# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymSubscriptionPlan(Document):
	pass

# @frappe.whitelist()
def my_method(plan):
	subscription_plan_fee = frappe.db.get_value('Gym Subscription Plan', plan, 'fee')
	return subscription_plan_fee
