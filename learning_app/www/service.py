import frappe

def get_context(context):
    context.title = "Service Request "
    context.no_cache = True

    context.sr = frappe.get_list(
        "Service Request",
        fields=["name", "subject", "customer_name", "status"],
        order_by="creation desc",
        page_length=20,
    )