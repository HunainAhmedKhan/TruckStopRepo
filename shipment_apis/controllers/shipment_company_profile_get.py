# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentControll(http.Controller):

    @http.route('/shipment/company_profile', auth='public', website=True)
    def shipment_user_company_profile(self, **kw):
        login = kw.get('login')
        company_details = request.env['shipment.shipper'].sudo().search([('login', '=', login),("account_status", '=', "active")], limit=1)
        if company_details:
                company_list = []
                parent_company_list = []
                details = {
                    'id': company_details.id,
                    'Company_Name': company_details.company_name,
                    'NTN_No': company_details.NTN_No,
                    'Company_NTN': company_details.company_NTN,
                    'Company_Industry': company_details.company_industry.name,
                    'Company_Address_City': company_details.company_address_city,
                    'Company_Street_Address': company_details.company_Address_street_address,
                    'login': company_details.login,
                    'password': company_details.password,
                    'confirmpass': company_details.confirmpass,
                    'phone': company_details.phone,
                    'token': company_details.token,
                    'get_image_base64': company_details.url,
                }
                company_list.append(details)
                parent_company_list.append(company_list)

                # Now concatinate all the lists into one single list
                list1 = parent_company_list

                data = json.dumps(list1)
                print(data)
                return data

        else:
            data = ["User doesn't exist"]
            return json.dumps(data)


        # else:
        #     data = {"response": "No record found or login,token Password is incorrect"}
        #     return json.dumps(data)

