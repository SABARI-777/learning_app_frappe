import frappe
def validate_desc(doc,method=None):
	if not doc.description:
		frappe.throw("ENTER DESCRIPTION !!!!")
