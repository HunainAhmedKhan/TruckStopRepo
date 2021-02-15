# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class City(http.Controller):
  


    @http.route('/payment_type', auth='public', website=True)
    def get_city(self, **kw):
        city =request.env['payment.type'].sudo().search([])
        print(city)
        data= []
        for i in city:
            if i.name:
             data.append(i.name)
        return json.dumps(data)


