# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentControll(http.Controller):
    @http.route('/shipment/login', auth='public', website=True)
    def shipment_json(self, **kw):

        login = kw.get('login')
        password = kw.get('password')
        token = kw.get('token')

        if login[0] == " ":
            # login[0].replace("+")
            login=f"+{login[1:]}"
        if login[0:2] == '00' or '0':
            if login[0:2] == '00':
                login = f"+92{login[4:]}"
                print('Login start',login)
            if login[0:1] == '0':
                login = f"+92{login[1:]}"
                print('Login Again',login)

        company_list =[]
        company_details = request.env['shipment.shipper'].sudo().search(['|', ('login', '=', login), ('phone', '=', login),("account_status", '=', "active")], limit=1)
        print(company_details)
        if company_details and company_details.password == password:
                if not company_details.token == token:
                    company_details.token = token
                details = {
                    'id': company_details.id,
                    'company_name': company_details.company_name,
                    'login': company_details.login,
                    'password': company_details.password,
                    'token': company_details.token,
                }
                company_list.append(details)
                if not company_details.token == token:
                    company_details.token = token

                # Now concatinate all the lists into one single list
                list1 = company_list

                data = json.dumps(list1)
                print(data)
                return data

        else:
            data = ["Login doesn't exist or password is incorrect"]
            return json.dumps(data)


        # else:
        #     data = {"response": "No record found or login,token Password is incorrect"}
        #     return json.dumps(data)

