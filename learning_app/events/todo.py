import frappe

def validate_desc(doc,method=None):
	if not doc.description:
		frappe.throw("ENTER DESCRIPTION !!!!")

@frappe.whitelist()
def data_access():
	row1 = frappe.get_list("ToTo",fields=["name","description"],order_by="creation desc",page_length=5)
	print(row1)
	row = frappe.get_all("ToTo",fields=["name","owner"])
	row2 = []
	for r in row:
		user_value = frappe.db.get_value("User",r.owner,"email")
		row2.append(user_value)
		print(row2)
		
	TOTO = frappe.qb.DocType("ToTo")
	USER = frappe.qb.DocType("User")
	row3 = frappe.qb.from_(TOTO).left_join(USER).on(TOTO.owner ==USER.name).select(TOTO.name,TOTO.description,USER.name,USER.email).run(as_dict = True)
	print(row3)
	toto_doc = frappe.get_doc("ToTo","TOTO-00009")
	toto_doc.description = "FRAPPE "
	toto_doc.save()
	frappe.db.commit()

	return{
		"row1":row1,
		"row2":row2,
        "row3":row3,
		"date":frappe.utils.now(),
    }


# for row in doc:
#     print(row.description)
#     val = frappe.get_value("ToTo",row)
#     print(val)
#     frappe.set_value("ToTo",row,"description","HELLO FRAPPPEE!!!!!")
#     print(row.description)


#    toto = frappe.qb.DocType("ToTo")
#    rows = frappe.qb.from_(toto).select(toto.name,toto.description).run(as_dict=True)
#    print(rows)


# export FRAPPE_TOKEN='63bbb627de80821:a908d3690fe2c76'

# curl -X POST 'http://learning.localhost:8000/api/resource/ToTo' \
# -H "Authorization: token ${FRAPPE_TOKEN}" \
# -H 'Content-Type: application/json' \
# --data '{"description":"Created through REST"}'


# export FRAPPE_TOKEN='63bbb627de80821:a908d3690fe2c76'
# curl --get 'http://learning.localhost:8000/api/resource/ToTo' \
# -H "Authorization: token ${FRAPPE_TOKEN}" \
# --data-urlencode 'fields=["name","description"]'

# this is for rate limit 
# curl --get 'http://learning.localhost:8000/api/method/learning_app.api.greeting.limited_greeting'