// Copyright (c) 2023, sydney and contributors
// For license information, please see license.txt


frappe.ui.form.on("Gym Locker Booking", {
	refresh(frm) {
		
		
	},
});

frappe.ui.form.on("Gym Locker Booking","locker", function(frm) {
    if (frm.doc.locker != null) {
		frappe.db.get_value('Gym Locker', frm.doc.locker, ['status', 'slots'])
		.then(function(data){
			console.log(data.message.status);
			frm.set_value('number_of_slot', data.message.slots);
			frm.set_value('locker_status', data.message.status);
		});
		
	}
});

frappe.ui.form.on("Gym Locker Booking","to_date", function(frm) {
    let from_date = frm.doc.from_date;
        let to_date = frm.doc.to_date;
        if (to_date < from_date) {
            frappe.msgprint("To date should not be less than start Date");
            frm.set_value("to_date", "");
        }
});

frappe.ui.form.on("Gym Locker Booking", "from_date", function(frm) {
    let now = new Date();
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