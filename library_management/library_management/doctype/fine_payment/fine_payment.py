import frappe
from frappe.model.document import Document
from frappe.utils import today

class FinePayment(Document):

    def on_submit(self):

        je = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Journal Entry",
            "company": "Anomaly",
            "posting_date": today(),
            "accounts": [
                {
                    "account": "Cash - A",
                    "debit_in_account_currency": self.amount
                },
                {
                    "account": "Library Fine Receivable - A",
                    "credit_in_account_currency": self.amount
                }
            ]
        })

        je.insert()
        je.submit()

        fine = frappe.get_doc("Fine", self.fine)
        fine.fine_status = "Paid"
        fine.save()