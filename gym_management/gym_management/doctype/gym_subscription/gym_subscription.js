// Copyright (c) 2023, sydney and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Subscription", {
    plan: function (frm) {
        frappe.call({
            method: 'gym_management.gym_management.doctype.gym_subscription.gym_subscription.get_subscription_plan_fee',
            args: {
                'doctype': 'Gym Subscription Plan',
                'plan': frm.doc.plan,
            },
            callback: function(r) {
                console.log(r.message);
                
                if (frm.doc.plan == 'Daily') {
                    frm.set_value('fee', r.message);
                } else if (frm.doc.plan == 'Weekly') {
                    var fee = r.message * 7;
                    frm.set_value('fee', fee);
                } else if (frm.doc.plan == 'Monthly') {
                    var fee = r.message * 30;
                    frm.set_value('fee', fee);
                } else{
                    var fee = r.message * 360;
                    frm.set_value('fee', fee);
                }
            }
        });
    },
    type: function (frm) {
        frappe.call({
            method: 'gym_management.gym_management.doctype.gym_subscription.gym_subscription.get_subscription_plan_fee',
            args: {
                'doctype': 'Gym Subscription Plan',
                'plan': frm.doc.plan,
            },
            callback: function(r) {
                console.log(r.message);
                
                if (frm.doc.type === 'Daily') {
                    frm.set_value('fee', r.message);
                } else if (frm.doc.type === 'Weekly') {
                    var fee = r.message * 7;
                    frm.set_value('fee', fee);
                } else if (frm.doc.type === 'Monthly') {
                    var fee = r.message * 30;
                    frm.set_value('fee', fee);
                } else{
                    var fee = r.message * 360;
                    frm.set_value('fee', fee);
                }
            }
        });
    },
    onload(frm) {
        frm.set_value('gym_member', frappe.user.name);
	},
});




