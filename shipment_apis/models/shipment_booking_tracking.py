# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipperList(http.Controller):

    @http.route('/shipment/booking/tracking', auth='public', website=True)
    def shipper_Booking_form_list(self, **kw):
        shipper = kw.get('shippment_id')
        if shipper:
            shipper_id = int(shipper)
            if shipper_id:
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('id', '=', shipper_id),('shipper_id.account_status', '=', 'active')])
                print(booking_details)
                if booking_details:
                    if booking_details.booking_status == "in_progress":
                            parent_booking_list = []
                            booking_list = []
                            for shipper in booking_details:
                                    booking_data = {
                                        'id': shipper.id,
                                        'login': shipper.login,
                                        'booking_status': shipper.booking_status,
                                        'carrier_id': shipper.carrier_id.id,
                                        'carrier_login': shipper.carrier_id.login,
                                        'shipper_id': shipper.shipper_id.id,
                                        'shipper_login': shipper.shipper_id.login,
                                        'pick_up_longitude': shipper.pick_up_longitude,
                                        'pick_up_latitude': shipper.pick_up_latitude,
                                        'drop_off_longitude': shipper.drop_off_longitude,
                                        'drop_off_latitude': shipper.drop_off_latitude,
                                        'current_longitude': shipper.current_longitude,
                                        'current_latitude': shipper.current_latitude,

                                    }
                                    booking_list.append(booking_data)
                                    parent_booking_list.append(booking_list)
                            data = json.dumps(booking_list)
                            return data
                    else:
                            data = {"response":"Shipment is not in progress"}
                            return json.dumps(data)
                else:
                    data = {"response":"Shipment ID doesn't exist"}
                    return json.dumps(data)
        else:
            data = {"response": "Enter Shipment ID"}
            return json.dumps(data)
