import frappe
@frappe.whitelist(methods=["POST"])
def create_service_request(subject: str) -> str:
	if not subject.strip():
		frappe.throw("Subject is required.")

	doc = frappe.new_doc("Service Request")
	doc.subject = subject.strip()
	doc.customer_name = frappe.session.user
	doc.description = "Dialog Descritpion"
	doc.insert()
	return doc.name