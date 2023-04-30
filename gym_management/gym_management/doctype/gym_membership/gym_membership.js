// Copyright (c) 2023, sydney and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Membership", {
// 	before_save(frm) {
//         let from_date = frm.doc.from_date;
//         let to_date = frm.doc.to_date;
//         if (to_date < from_date) {
//             frappe.msgprint("Ending date should not be less than start Date");
//             frm.set_value("to_date", "");
//         }
// 	},
// });

frappe.ui.form.on("Gym Membership","to_date", function(frm) {
    let from_date = frm.doc.from_date;
        let to_date = frm.doc.to_date;
        if (to_date < from_date) {
            frappe.msgprint("To date should not be less than start Date");
            frm.set_value("to_date", "");
        }
});

frappe.ui.form.on("Gym Membership", "from_date", function(frm) {
    let now = new Date();
	let day = now.getDate();
    let month = now.getMonth() + 1;
    let year = now.getFullYear();
    let from_date = frm.doc.from_date;
    if (from_date < now.toISOString().substring(0, 10)) {
		frappe.msgprint({
			title: __('Warning'),
			indicator: 'red',
			message: __("From date can not be less than Today's date")
		});
		frm.set_value("from_date", "");
    }
});