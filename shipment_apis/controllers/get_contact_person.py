from odoo import http
from odoo.http import request
import json

class ContactPerson(http.Controller):



    @http.route('/shipment/contact/person', auth='public', website=True)
    def get_contact_pesron(self, **kw):
            login = kw.get('login')
            get_login =request.env['shipment.shipper'].sudo().search([('login', '=',login)],limit=1)
            print("Some value",get_login)
            if get_login:
                 print('WORKING ',get_login)
                 contact = []
                 print("Working ",get_login.contacts)
                 for i in get_login.contact_person_info:
                     list ={
                         'id'         : i.id,
                         'person_name': i.person_name,
                         'person_designation': i.person_desig,
                         'person_number': i.person_number,
                         'person_mail': i.person_mail
                     }
                     contact.append(list)
                     print(contact)
                 data = json.dumps(contact)
                 return data

            if not get_login:
              return "User doesnt exist"
                     # return {'success': False, 'message': "User not found"}





