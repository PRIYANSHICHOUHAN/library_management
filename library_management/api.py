import frappe
from frappe.utils import today, date_diff

@frappe.whitelist()
def return_book(issue):

    doc = frappe.get_doc(
        "Book Issue",
        issue
    )

    # Update Issue Status
    doc.status = "Returned"
    doc.save()

    # Increase Available Copies
    book = frappe.get_doc(
        "Book",
        doc.book
    )

    book.available_copies += 1
    book.save()

    # Calculate Overdue Days
    overdue_days = date_diff(
        today(),
        doc.due_date
    )

    if overdue_days > 0:

        settings = frappe.get_single(
            "Library Settings"
        )

        amount = (
            overdue_days *
            settings.fine_per_day
        )

        fine = frappe.get_doc({
            "doctype": "Fine",
            "member": doc.member,
            "book_issue": doc.name,
            "fine_amount": amount,
            "days_overdue": overdue_days,
            "fine_status": "Pending"
        })

        fine.insert()

        # Send Email Notification
        try:
            member = frappe.get_doc(
                "Library Member",
                doc.member
            )

            if member.email:

                frappe.sendmail(
                    recipients=[member.email],
                    subject="Library Overdue Fine Notification",
                    message=f"""
                    Dear {member.full_name},

                    Your book has been returned late.

                    Overdue Days: {overdue_days}
                    Fine Amount: ₹{amount}

                    Please pay the fine at the library desk.

                    Regards,
                    Library Team
                    """
                )

        except Exception:
            frappe.log_error(
                frappe.get_traceback(),
                "Library Email Notification Failed"
            )

    frappe.db.commit()

    return {
        "status": "success",
        "message": "Book Returned Successfully"
    }