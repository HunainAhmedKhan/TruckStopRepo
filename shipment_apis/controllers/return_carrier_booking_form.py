# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class carrierBooking(http.Controller):

    @http.route('/carrier/Return/CarrierList', auth='public', website=True)
    def carrier_booking_form(self, **kw):
        carrier = kw.get('carrier_id')
        print(carrier)
        booking_status = kw.get('booking_status')
        carrier_id = int(carrier)
        print(booking_status)

        if carrier_id:
           if  booking_status =="pending":
                print("pending")
                booking_details = request.env['shipment.shipment_booking'].sudo().search([('carrier_id','=',carrier_id),('booking_status','=','pending')])
                print(booking_details)
                if booking_details:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        booking_data = {
                            'id':carrier.id,
                            'login': carrier.login,
                            'load_type': carrier.load_type.name,
                            'Origin_city': carrier.origin_city,
                            'Destination_city': carrier.destination_city,
                            'Delivery_Option': carrier.delivery_option.name,
                            'Cargo_Type': carrier.cargo_type.name,
                            'Cargo_amount': carrier.cargo_amount,
                            "Cargo_Product_type": carrier.cargo_product_type,
                            'Cargo_Packing_List': carrier.cargo_packing_list,
                            'carrier_id': carrier.carrier_id.id,
                            'shipper_id': carrier.shipper_id.id,
                            'shipper_company': carrier.shipper_id.company_name,
                            'booking_status':carrier.booking_status,
                            'shipper_name': carrier.shipper_id.login,
                            'carrier_company': carrier.carrier_id.company_name,
                            'shipper_token': carrier.shipper_id.token,
                            'carrier_token': carrier.carrier_id.token,
                            'address': carrier.address,
                            'grand_total': carrier.grand_total,
                            'estimated_date': carrier.estimated_date.strftime('%Y-%m-%d'),
                            'rate_per_ton': carrier.rate_per_ton,
                            'rate_per_kg': carrier.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
                else:
                    data = {"response": "Record does not exits or not found"}
                    return json.dumps(data)

           if booking_status == "in_progress":
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'in_progress')])
                print(booking_details)
                if booking_details:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        print(carrier.id)
                        booking_data = {
                            'id': carrier.id,
                            'login': carrier.login,
                            'load_type': carrier.load_type.name,
                            'Origin_city': carrier.origin_city,
                            'Destination_city': carrier.destination_city,
                            'Delivery_Option': carrier.delivery_option.name,
                            'Cargo_Type': carrier.cargo_type.name,
                            'Cargo_amount': carrier.cargo_amount,
                            "Cargo_Product_type": carrier.cargo_product_type,
                            'Cargo_Packing_List': carrier.cargo_packing_list,
                            'carrier_id': carrier.carrier_id.id,
                            'shipper_id': carrier.shipper_id.id,
                            'shipper_company': carrier.shipper_id.company_name,
                            'booking_status': carrier.booking_status,
                            'shipper_name': carrier.shipper_id.login,
                            'carrier_company': carrier.carrier_id.company_name,
                            'shipper_token': carrier.shipper_id.token,
                            'carrier_token': carrier.carrier_id.token,
                            'address': carrier.address,
                            'estimated_date': carrier.estimated_date.strftime('%Y-%m-%d'),
                            'grand_total': carrier.grand_total,
                            'rate_per_ton': carrier.rate_per_ton,
                            'rate_per_kg': carrier.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
                else:
                    data = {"response": "Record does not exits or not found"}
                    return json.dumps(data)
           if booking_status == "complete":
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'complete')])
                print(booking_details)
                if booking_details:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        print(carrier.id)
                        booking_data = {
                            'id': carrier.id,
                            'login': carrier.login,
                            'load_type': carrier.load_type.name,
                            'Origin_city': carrier.origin_city,
                            'Destination_city': carrier.destination_city,
                            'Delivery_Option': carrier.delivery_option.name,
                            'Cargo_Type': carrier.cargo_type.name,
                            'Cargo_amount': carrier.cargo_amount,
                            "Cargo_Product_type": carrier.cargo_product_type,
                            'Cargo_Packing_List': carrier.cargo_packing_list,
                            'carrier_id': carrier.carrier_id.id,
                            'shipper_id': carrier.shipper_id.id,
                            'shipper_company': carrier.shipper_id.company_name,
                            'booking_status': carrier.booking_status,
                            'shipper_name': carrier.shipper_id.login,
                            'carrier_company': carrier.carrier_id.company_name,
                            'shipper_token': carrier.shipper_id.token,
                            'carrier_token': carrier.carrier_id.token,
                            'address': carrier.address,
                            'estimated_date': carrier.estimated_date.strftime('%Y-%m-%d'),
                            'grand_total': carrier.grand_total,
                            'rate_per_ton': carrier.rate_per_ton,
                            'rate_per_kg': carrier.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
                else:
                    data = {"response": "Record does not exits or not found"}
                    return json.dumps(data)
           if booking_status == "previous":
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'previous')])
                print(booking_details)
                if booking_details:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        print(carrier.id)
                        booking_data = {
                            'id': carrier.id,
                            'login': carrier.login,
                            'load_type': carrier.load_type.name,
                            'Origin_city': carrier.origin_city,
                            'Destination_city': carrier.destination_city,
                            'Delivery_Option': carrier.delivery_option.name,
                            'Cargo_Type': carrier.cargo_type,
                            'Cargo_amount': carrier.cargo_amount,
                            "Cargo_Product_type": carrier.cargo_product_type,
                            'Cargo_Packing_List': carrier.cargo_packing_list,
                            'carrier_id': carrier.carrier_id.id,
                            'shipper_id': carrier.shipper_id.id,
                            'shipper_company': carrier.shipper_id.company_name,
                            'booking_status': carrier.booking_status,
                            'shipper_name': carrier.shipper_id.login,
                            'carrier_company': carrier.carrier_id.company_name,
                            'shipper_token': carrier.shipper_id.token,
                            'carrier_token': carrier.carrier_id.token,
                            'address': carrier.address,
                            'estimated_date': carrier.estimated_date.strftime('%Y-%m-%d'),
                            'grand_total': carrier.grand_total,
                            'rate_per_ton': carrier.rate_per_ton,
                            'rate_per_kg': carrier.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
                else:
                    data = {"response": "Record does not exits or not found"}
                    return json.dumps(data)

           if booking_status == "accept":
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'accept')])
                print(booking_details)
                if booking_details:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        print(carrier.id)
                        booking_data = {
                            'id': carrier.id,
                            'login': carrier.login,
                            'load_type': carrier.load_type.name,
                            'Origin_city': carrier.origin_city,
                            'Destination_city': carrier.destination_city,
                            'Delivery_Option': carrier.delivery_option.name,
                            'Cargo_Type': carrier.cargo_type,
                            'Cargo_amount': carrier.cargo_amount,
                            "Cargo_Product_type": carrier.cargo_product_type,
                            'Cargo_Packing_List': carrier.cargo_packing_list,
                            'carrier_id': carrier.carrier_id.id,
                            'shipper_id': carrier.shipper_id.id,
                            'shipper_company': carrier.shipper_id.company_name,
                            'booking_status': carrier.booking_status,
                            'shipper_name': carrier.shipper_id.login,
                            'carrier_company': carrier.carrier_id.company_name,
                            'shipper_token': carrier.shipper_id.token,
                            'carrier_token': carrier.carrier_id.token,
                            'address': carrier.address,
                            'estimated_date': carrier.estimated_date.strftime('%Y-%m-%d'),
                            'grand_total': carrier.grand_total,
                            'rate_per_ton': carrier.rate_per_ton,
                            'rate_per_kg': carrier.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
                else:
                    data = {"response": "Record does not exits or not found"}
                    return json.dumps(data)
           if booking_status == "reject":
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'reject')])
                print(booking_details)
                if booking_details:
                    parent_booking_list = []
                    booking_list = []
                    for carrier in booking_details:
                        print(carrier.id)
                        booking_data = {
                            'id': carrier.id,
                            'login': carrier.login,
                            'load_type': carrier.load_type.name,
                            'Origin_city': carrier.origin_city,
                            'Destination_city': carrier.destination_city,
                            'Delivery_Option': carrier.delivery_option.name,
                            'Cargo_Type': carrier.cargo_type,
                            'Cargo_amount': carrier.cargo_amount,
                            "Cargo_Product_type": carrier.cargo_product_type,
                            'Cargo_Packing_List': carrier.cargo_packing_list,
                            'carrier_id': carrier.carrier_id.id,
                            'shipper_id': carrier.shipper_id.id,
                            'shipper_company': carrier.shipper_id.company_name,
                            'booking_status': carrier.booking_status,
                            'shipper_name': carrier.shipper_id.login,
                            'carrier_company': carrier.carrier_id.company_name,
                            'shipper_token': carrier.shipper_id.token,
                            'carrier_token': carrier.carrier_id.token,
                            'address': carrier.address,
                            'estimated_date': carrier.estimated_date.strftime('%Y-%m-%d'),
                            'grand_total': carrier.grand_total,
                            'rate_per_ton': carrier.rate_per_ton,
                            'rate_per_kg': carrier.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                    parent_booking_list.append(booking_list)
                    data = json.dumps(booking_list)
                    return data
                else:
                    data = {"response": "Record does not exits or not found"}
                    return json.dumps(data)



        else:
            data = {"response": "Record does not exist or not found"}
            return json.dumps(data)
