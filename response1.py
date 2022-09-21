# Copyright (c) 2022, SANJAY and contributors
# For license information, please see license.txt

import json
import frappe
import requests
from frappe.model.document import Document

class Response1(Document):
	def validate(self):
		if(self.link):
			r = requests.get(self.link.strip())
			self.log = (r._content).decode()
			if (self.log):
				a = json.loads(self.log)
				
				for i in a:
						i = frappe.get_doc({
							"doctype": "Response Fields",
							"postid": i['postId'],
							"id": i['id'],
							"name1": i['name'],
							"email": i['email'],
						}).insert()
				print(a)
				# b = (a['response'])
				# print(b)
				# res= json.loads(b)
				# ls= (a['data'])
				# print(ls)
					
			log_request(self.link.strip(), res=self.log)

 
def log_request(url, res):
		request_log = frappe.get_doc(
			{
				"doctype": "Webhook Request Log",
				"user": frappe.session.user if frappe.session.user else None,
				"url": url,
				"response": res
			}
		)

		request_log.save(ignore_permissions=True);	

		