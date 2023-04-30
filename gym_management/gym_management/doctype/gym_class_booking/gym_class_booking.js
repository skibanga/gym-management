// Copyright (c) 2023, sydney and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Class Booking", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Gym Class Booking","gym_class", function(frm) {
    if (frm.doc.gym_class != null) {
		frappe.db.get_value('Gym Class', frm.doc.gym_class, ['description','trainer', 'capacity', 'members_enrolled'])
		.then(function(data){
			// console.log(data.message.status);
			frm.set_value('trainer', data.message.trainer);
			frm.set_value('description', data.message.description);
			frm.set_value('capacity', data.message.capacity);
			frm.set_value('members_enrolled', data.message.members_enrolled);
		});
		
	}
});
