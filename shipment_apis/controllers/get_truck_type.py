# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class City(http.Controller):
   


    @http.route('/truck_type', auth='public', website=True)
    def get_city(self, **kw):
        city =request.env['truck.type'].sudo().search([]).sorted('name')
        print(city)
        dic = {}
        data= []
        for i in city:
            if i.name:
                dic =(
                    {
                        'id' : i.id,
                        'truck_name': i.name,
                    }
                )
                data.append(dic)
                # data.append(i.name)
                # dic.update(data)

        return json.dumps(data)

    @http.route('/truck_type_name', auth='public', website=True)
    def get_name_city(self, **kw):
        city = request.env['truck.type'].sudo().search([]).sorted('name')
        print(city)
        dic = {}
        data = []
        for i in city:
            if i.name:
                data.append(i.name)
                # data.append(i.name)
                # dic.update(data)

        return json.dumps(data)

    @http.route('/get_carrier_truck', auth='public', website=True)
    def get_carrier_trucks(self, **kw):
        carrier = kw.get('carrier_id')
        carrier_id = int(carrier)
        city = request.env['carrier.carrier'].sudo().search([("id",'=',carrier_id)])
        dic = {}
        data = []
        for i in city.truck_fleet:
            if i.name:
                data.append(i.name)
        return json.dumps(data)


