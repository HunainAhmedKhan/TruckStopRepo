# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentControll(http.Controller):
    @http.route('/shipment', type="http", auth="public", website=True)
    def shipment_search_details(self, **kw):
        return http.request.render('shipment.shipment_search', {
        })

    @http.route('/shipment/search', auth='public', website=True)
    def shipment_json(self, **kw):

        login = kw.get('login')
        password = kw.get('password')
        token = kw.get('token')
        company_details = request.env['shipment.shipper'].sudo().search(['|', ('login', '=', login), ('phone', '=', login),("account_status", '=', "active")], limit=1)
        print(company_details)
        if company_details and company_details.password == password:

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
                print(parent_account_list)

                # This is for contact one2many field
                contacts_data = company_details.contacts
                contact_list = []
                parent_contact_list = []
                count = 0
                for i in contacts_data:

                    # if count < 3:
                    #     count = count + 1
                        contact_list.append({
                            'id': i.id,
                            'person_name': i.person_name,
                            'designation_person': i.designation_person,
                            'mobile_no': i.mobile_no,
                            'email_address': i.email_address
                        })

                parent_contact_list.append(contact_list)
                # This is for person info one2many field
                account = company_details.contact_person_info
                person_list = []
                parent_person_list = []
                person = 0
                for i in account:

                    # if person < 3:
                    #     person = person + 1
                        person_list.append({
                            'id': i.id,
                            'person_name': i.person_name,
                            'person_designation': i.person_desig,
                            'person_number': i.person_number,
                            'person_email': i.person_mail
                        })
                parent_person_list.append(person_list)

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
                    'get_image_base64': company_details.get_image_base64,
                }
                company_list.append(details)
                parent_company_list.append(company_list)
                all_parent = []
                parent_person_list + parent_contact_list + parent_account_list

                # Now concatinate all the lists into one single list
                list1 = parent_company_list + parent_person_list + parent_contact_list + parent_account_list

                data = json.dumps(list1)
                print(data)
                return data

        else:
            data = ["Login doesn't exist or password is incorrect"]
            return json.dumps(data)


        # else:
        #     data = {"response": "No record found or login,token Password is incorrect"}
        #     return json.dumps(data)

