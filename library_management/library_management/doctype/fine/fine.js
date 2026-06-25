// Copyright (c) 2026,   and contributors
// For license information, please see license.txt
frappe.ui.form.on("Fine", {
    refresh(frm) {
        if(frm.doc.fine_status=="Pending") {
            frm.add_custom_button("Waive Fine", ()=>{
                frm.set_value("fine_status","Waived");
                frm.save();
            });
        }
    }
});