import frappe
from frappe.rate_limiter import rate_limit

@frappe.whitelist(allow_guest=True, methods=["GET"])
@rate_limit(key="limited_greeting", limit=5, seconds=60)
def limited_greeting():
    return {"message": "Hello, Rate Limited World!"}
