// Copyright (c) 2026, sab and contributors
// For license information, please see license.txt

frappe.ui.form.on("Service Request", {
	validate(frm) {
        const  row = frm.add_child("items");
        row.item_code = "ITM-00002";
        row.qty = 5;
        row.rate = 600
        row.amount = row.rate * row.qty;
        frm.refresh_field("items");
	},
});
