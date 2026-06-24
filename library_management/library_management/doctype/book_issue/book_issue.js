frappe.ui.form.on("Book Issue", {
    refresh(frm) {

        if(frm.doc.docstatus==1 &&
           frm.doc.status=="Issued") {

            frm.add_custom_button(
                "Return Book",
                ()=>{
                    frappe.call({
                        method:
                        "library_management.api.return_book",
                        args:{
                            issue:frm.doc.name
                        },
                        callback:function(){
                            frm.reload_doc();
                        }
                    })
                }
            )
        }
    }
});