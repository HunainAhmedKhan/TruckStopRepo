# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class Notification(http.Controller):

    @http.route('/notification', auth='public', website=True)
    def notifications(self, **kw):
        search = request.env['activity'].sudo().search([])
        notifications = []
        for i in search:
            data= {
            "notification_no": i.notification_no,
            "name": i.name,
            "push_notification": i.name,
            "sms_notification": i.name,
        }
            notifications.append(data)
        data = notifications
        return json.dumps(data)

