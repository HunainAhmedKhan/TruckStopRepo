# -*- coding: utf-8 -*-
import base64

from odoo import http
from odoo.http import request
from base64 import decodestring

import json

class City(http.Controller):

    @http.route('/driver_images', auth='public', website=True)
    def driver_images(self, **kw):
        login = kw.get('login')
        city = request.env['driver.info'].sudo().search([('login','=',login)],limit=1)
        data = []
        for i in city:
                dic= {'get_image_url': i.url}
                data.append(dic)
        return json.dumps(data)

    @http.route('/driver_info', auth='public', website=True)
    def get_city(self, **kw):
        city =request.env['driver.info'].sudo().search([])
        print(city)
        data= []
        for i in city:
            if i.driver_name:
                data.append(i.driver_name)

        return json.dumps(data)

    @http.route('/get_driver_record', auth='public', website=True)
    def get_driver_record(self, **kw):
        login = kw.get('login')
        driver_login = kw.get('driver_login')

        if login:
            driver = request.env['driver.info'].sudo().search([('carrier.login','=',login)])
        if driver_login:
            driver = request.env['driver.info'].sudo().search([('login', '=', driver_login)])
        data = []
        for i in driver:
            drivers = {
                'driver_name': i.driver_name,
                'driver_login': i.login,
                'driver_address': i.driver_address,
                'driver_lisence': i.driver_lisence,
                'driver_no': i.driver_no,
                'get_image_base64': i.url,
                'pick_up_latitude': i.pick_up_latitude,
                'pick_up_longitude': i.pick_up_longitude,
                'drop_off_longitude': i.drop_off_longitude,
                'drop_off_latitude': i.drop_off_latitude,
                'current_longitude': i.current_longitude,
                'current_latitude': i.current_latitude,
            }
            data.append(drivers)
        return json.dumps(data)

    @http.route('/driver/booking/form', auth='public', website=True)
    def driver_booking_form(self, **kw):
        driver_id = kw.get('login')
        password = kw.get('password')
        token = kw.get('token')
        driver_status = kw.get('driver_status')
        if driver_id:
            if driver_status == "pending":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id),('driver_status', '=', 'pending')])
            elif driver_status == "in_progress":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'in_progress')])
            elif driver_status == "truck_assigned":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'truck_assigned')])
            elif driver_status == "truck_dispatched":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'truck_dispatched')])
            elif driver_status == "loading":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'loading')])
            elif driver_status == "in_transit":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'in_transit')])
            elif driver_status == "unloading":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'unloading')])
            elif driver_status == "loading":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'loading')])

            elif driver_status == "completed":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id), ('driver_status', '=', 'completed')])

            elif driver_status == "invoice_cleared":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                [('driver_id.login', '=', driver_id), ('driver_status', '=', 'invoice_cleared')])

            else:
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('driver_id.login', '=', driver_id)])

        # if not booking_details:
        #     args = {'success': False, 'message': 'User Doesnt Exist'}
        #     return args
            if booking_details.driver_id.password == password:
                # print(booking_details)
                # if booking_details and driver_status:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        print(carrier.id)
                        booking_data = {

                            'id': carrier.id,
                            'booking_status': carrier.booking_status,
                            'driver_status': carrier.driver_status,
                            'invoice_no': carrier.invoice_no,
                            'pickup_time': carrier.pick_up_time.name,
                            'pickup_date': carrier.pick_up_date.strftime('%Y-%m-%d'),
                            'cargo_weight': carrier.cargo_weight,
                            'pickup_address': carrier.address,
                            'company_no': carrier.carrier_id.phone,
                            'drop_off_time': carrier.drop_off_time.name,
                            'contact_person_no': carrier.recipient_contact_number,
                            'contact_person': carrier.recipient_contact_person_name,
                            'drop_off_address': carrier.drop_off_address,
                            'shipper_company': carrier.shipper_id.company_name,
                            'driver_assigned': carrier.driver_id.driver_name,
                            'driver_name': carrier.driver_id.driver_name,
                            'driver_login': carrier.driver_id.login,
                            'driver_address': carrier.driver_id.driver_address,
                            'driver_lisence': carrier.driver_id.driver_lisence,
                            'driver_no': carrier.driver_id.driver_no,
                            'carrier_company': carrier.carrier_id.company_name,
                            'carrier_phone': carrier.carrier_id.phone,
                            'origin_city': carrier.origin_city,
                            'destination_city': carrier.destination_city,
                            'cargo_weight_type':carrier.cargo_weight_type,
                            'truck_type': carrier.load_type.name,
                             'pick_up_latitude': carrier.pick_up_latitude,
                            'pick_up_longitude': carrier.pick_up_longitude,
                            'drop_off_longitude': carrier.drop_off_longitude,
                            'drop_off_latitude': carrier.drop_off_latitude,
                            'current_longitude': carrier.current_longitude,
                            'current_latitude': carrier.current_latitude,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
            else:
                args = {'success': False, 'message': 'Wrong password or login'}
                data = json.dumps(args)
                return data
        else:
            args = {'success': False, 'message': 'No Driver Login'}
            data = json.dumps(args)
            return data




    @http.route('/get_driver_login', auth='public', website=True)
    def get_driver_login(self, **kw):
        login = kw.get('login')
        password = kw.get('password')
        token = kw.get('token')
        print(kw.get('password'))
        driver = request.env['driver.info'].sudo().search([('login','=',login)],limit=1)
        data = []
        if driver.password==password:
            if token:
                driver.write({'token': kw.get('token')})
            for i in driver:
                drivers = {
                    'driver_name': i.driver_name,
                    'driver_login': i.login,
                    'driver_address': i.driver_address,
                    'driver_lisence': i.driver_lisence,
                    'driver_no': i.driver_no,
                    'carrier': i.carrier.id,
                    'pick_up_latitude': i.pick_up_latitude,
                    'pick_up_longitude': i.pick_up_longitude,
                    'drop_off_longitude': i.drop_off_longitude,
                    'drop_off_latitude': i.drop_off_latitude,
                    'carrier_name': i.carrier.company_name,
                    'current_longitude': i.current_longitude,
                    'current_latitude': i.current_latitude,

                }
                data.append(drivers)
            return json.dumps(data)
        else:
           return "Password incorrect"
