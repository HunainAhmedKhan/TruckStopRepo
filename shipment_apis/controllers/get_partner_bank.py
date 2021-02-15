# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class City(http.Controller):
   

    @http.route('/res_partner_bank', auth='public', website=True)
    def get_city(self, **kw):
        city =request.env['res.bank'].sudo().search([])
        print(city)
        data= []
        for i in city:

                data.append(i.name)

        return json.dumps(data)


