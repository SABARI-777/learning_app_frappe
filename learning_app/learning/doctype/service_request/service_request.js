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

        refresh(frm){

                if (!frm.is_new()){

                frm.add_custom_button(("Start"), async () => {
                await frm.set_value("status", "In Progress");
                await frm.save();
                },);

                frm.add_custom_button(("PUT queue"),async() =>{
                       
                        frappe.call({
                                method:"learning_app.tasks.start_process",
                        });

                        frappe.realtime.on("service_request_done", (data) => {
                        frappe.msgprint({
                        message: data.message,
                        indicator: "green"
                       });
                });
                })

                // const dialog = new frappe.ui.Dialog({
                // title: __("New Contact"),
                // fields: [
                // { fieldname: "first_name", label: __("First Name"), fieldtype: "Data", reqd: 1
                // }
                // ],
                // primary_action_label: __("Continue"),
                // primary_action(values) {
                // dialog.hide();
                // frappe.route_options = { first_name: values.first_name };
                // frappe.new_doc("Contact");
                // }
                // });
                // dialog.show();
                }   
                
                frm.add_custom_button(("ADD"), async () => {
                const dialog = new frappe.ui.Dialog({
                        title:"CREATE NEW SERVICE REQUEST ",
                        fields:[{fieldname:"subject",label:"SUBJECT",fieldtype:"Data",reqd:1}],
                        primary_action_label:"Create",
                        async primary_action(values){
                              const res =  frappe.call({
                                        method:"learning_app.api.create_service_request.create_service_request",
                                        type:"POST",
                                        args:{"subject":values.subject},
                                        freeze:true,
                                        freeze_message: ("Creating request..."),
                                        callback: function (r) {
                                        console.log(r.message);
                                        frappe.msgprint({
                                                title: ("Created"),
                                                message: `Service Request ${r.message} was created.`,
                                                indicator: "green"
                                        });
                                       }
                                });
                                dialog.hide();
                               
                        }
                });
                dialog.show();
        });
        }
        
});
