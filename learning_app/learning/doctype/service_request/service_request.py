# Copyright (c) 2026, sab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServiceRequest(Document):

	def before_insert(self):
		if not self.description:
			frappe.throw("ENTER DESC !!!!")

	# def before_save(self):

    
	def validate(self):

		flag = False
		for child in self.items:
			if not child.rate:
				flag= True
		if flag:
			frappe.throw("ENTER RATE PLEASE !!")

		self.subject = "TECH"
		self.customer_name = "Sample TECH"

		self.append("items",{
			"item_code":"ITM-00002",
			"qty": 2,
			"rate": 500
		})
		total = 0
		for row in self.items:
			row.qty = 3
			row.amount = row.qty * row.rate
			total+=row.amount
		self.total_amount = total

 		
	def after_insert(self):
		frappe.msgprint("DOC SAVED SUCCESSFULLY !!!")