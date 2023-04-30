# import frappe

# def get_context(context):
#     context.about_us_settings = frappe.get_doc('Gym Workout Plan')
#     return context


import frappe

def get_context(context):
	context.doc = frappe.get_cached_doc("Gym Workout Plan")

	return context
