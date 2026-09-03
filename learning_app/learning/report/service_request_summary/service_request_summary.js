frappe.query_reports["Service Request Summary"] = {
    filters: [
        {
            fieldname: "status",
            label: __("Status"),
            fieldtype: "Select",
            options: "\nOpen\nIn Progress\nClosed"
        }
    ]
};