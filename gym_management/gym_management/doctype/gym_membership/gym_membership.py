# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMembership(Document):
    # check before submitting this document
    def before_save(self):
        exists = frappe.db.exists(
            'Gym Membership',
            {
                'gym_member': self.gym_member,
                # check if the membership's end date is later than this membership's start date
                'to_date': ('>', self.from_date),
            },
        )
        if exists:
            frappe.throw('There is an active membership for this member')

