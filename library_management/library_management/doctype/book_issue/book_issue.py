from frappe.model.document import Document
from frappe.utils import add_days

class BookIssue(Document):

    def validate(self):

        if not self.issue_date:
            self.issue_date = frappe.utils.today()

        self.due_date = add_days(self.issue_date,14)

        book = frappe.get_doc("Book",self.book)

        if book.available_copies <= 0:
            frappe.throw("No copies available")
            
def on_submit(self):

    book = frappe.get_doc("Book",self.book)

    book.available_copies -= 1

    book.save()