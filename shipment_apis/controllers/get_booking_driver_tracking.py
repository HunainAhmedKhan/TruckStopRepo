# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentBooking(http.Controller):

    @http.route('/shipment/booking/driver/tracking', auth='public', website=True)
    def shipment_booking_form(self, **kw):
        shipment = kw.get('shipment_id')
        shipment_id = int(shipment)
        print(shipment_id)
        if shipment_id:
            # booking_details = request.env['shipment.shipment_booking'].sudo().search(
            #     [('id', '=', shipment_id), ('shipper_id.account_status', '=', 'active')], limit=1)
            booking_details = request.env['shipment.shipment_booking'].sudo().search([('id','=',shipment_id),('shipper_id.account_status', '=', 'active')],limit=1)
            if not booking_details.id:
                data = {"response": "Shipment ID doesnt exist or not active"}
                return json.dumps(data)
            print(booking_details)
            booking_list = []
            parent_booking_list=[]
            if booking_details:
                booking_data = {
                    'id': booking_details.id,
                    'driver_current_longitude': booking_details.driver_id.current_longitude,
                    'driver_current_latitude': booking_details.driver_id.current_latitude,
                    'driver_pick_up_latitude': booking_details.driver_id.pick_up_latitude,
                    'driver_pick_up_longitude': booking_details.driver_id.pick_up_longitude,
                    'driver_drop_off_longitude': booking_details.driver_id.drop_off_longitude,
                    'driver_drop_off_latitude': booking_details.driver_id.drop_off_latitude,
                   'driver_assigned': booking_details.driver_id.driver_name,
                    'driver_id': booking_details.driver_id.id,
                    'driver_status': booking_details.driver_status,
                }
                booking_list.append(booking_data)
                parent_booking_list.append(booking_list)
                data = json.dumps(booking_list)
                print(data)
                return data
        else:
            data = {"response": "Shipment ID doesnt exist or driver is not assigned"}
            return json.dumps(data)

