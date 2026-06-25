# Copyright (c) 2026,   and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils import today

class Fine(Document):

    def after_insert(self):
        create_journal_entry(self)


def create_journal_entry(fine):

    je = frappe.get_doc({
    "doctype": "Journal Entry",
    "voucher_type": "Journal Entry",
    "company": "Anomaly",
    "posting_date": today(),
    "accounts": [
        {
            "account": "Library Fine Receivable - A",
            "debit_in_account_currency": fine.fine_amount
        },
        {
            "account": "Library Fine Income - A",
            "credit_in_account_currency": fine.fine_amount
        }
    ]
})

    je.insert()
    je.submit()
