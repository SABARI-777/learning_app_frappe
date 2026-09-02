# Copyright (c) 2026, sab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServiceRequest(Document):
    
	def validate(self):
		self.subject = "TECH"
		self.customer_name = "Sample TECH"

		self.append("items",{
			"item_code":"ITM-00002",
			"qty": 2,
			"rate": 500
		})

		for row in self.items:
			row.qty = 3
			row.amount = row.qty * row.rate

