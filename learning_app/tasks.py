import frappe

def daily_maintenance():
    frappe.logger("learning_app.scheduler").info("Daily maintenance completed")




@frappe.whitelist()
def process_service_request():
    frappe.logger("learning_app.background_job").info("background_job LOG") 

    frappe.publish_realtime(
        "service_request_done",
        {"message": "Service Request processing completed"}
    )

@frappe.whitelist()
def start_process():
    frappe.enqueue(
        "learning_app.tasks.process_service_request",
        queue="default",
        job_name="service requests",
    )

    return "Process started"