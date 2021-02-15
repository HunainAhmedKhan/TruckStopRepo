# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentControll(http.Controller):
    @http.route('/shipment/account_info', auth='public', website=True)
    def shipment_json(self, **kw):

        login = kw.get('login')
        company_details = request.env['shipment.shipper'].sudo().search([('login', '=', login),("account_status", '=', "active")], limit=1)
        print(company_details)
        if company_details:

            # company_details.token = token
            # if company_details.password == password:

                account_info_data = company_details.account_info
                account_list = []
                parent_account_list = []
                account = 0
                for i in account_info_data:
                    # if account < 3:
                    #     account = account + 1
                        account_list.append({
                            'id': i.id,
                            'address': i.add_addresses,
                            'address_title': i.address_title,
                            'street_address': i.street_address,
                            'city': i.city,
                        })
                parent_account_list.append(account_list)

                # Now concatinate all the lists into one single list
                list1 = parent_account_list

                data = json.dumps(list1)
                print(data)
                return data

        else:
            data = ["Login doesn't exist or password is incorrect"]
            return json.dumps(data)


        # else:
        #     data = {"response": "No record found or login,token Password is incorrect"}
        #     return json.dumps(data)

