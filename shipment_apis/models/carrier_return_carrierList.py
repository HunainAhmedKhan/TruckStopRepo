# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipperList(http.Controller):

    @http.route('/shipper/Return/CarrierList', auth='public', website=True)
    def shipper_Booking_form_list(self, **kw):
        carrier = kw.get('carrier_id')
        carrier_id = int(carrier)
        booking_status = kw.get('booking_status')
        invoice_status = kw.get('invoice_status')
        if carrier_id:
            if booking_status == "pending":

                booking_details = request.env['shipment.shipment_booking'].sudo().search([('carrier_id', '=', carrier_id),('booking_status', '=', 'pending')])
            elif booking_status == "accept":

                booking_details = request.env['shipment.shipment_booking'].sudo().search([('carrier_id', '=', carrier_id),('booking_status', '=', 'accept')])
            elif booking_status == "reject":
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'reject')])
            elif booking_status == "complete":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'complete')])
            elif booking_status == "in_progress":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'in_progress')])
            elif booking_status == "previous":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('booking_status', '=', 'previous')])
            elif invoice_status:

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id), ('invoice_status', '=', invoice_status)])
                print((booking_details))
            else:
                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('carrier_id', '=', carrier_id)])

            print(booking_details)
            if booking_details:
                parent_booking_list = []
                booking_list = []
                for shipper in booking_details:

                    if shipper.cargo_weight_type =='kg':
                        booking_data = {
                            'id': shipper.id,
                            'login': shipper.login,
                            'load_type': shipper.load_type.name,
                            'Origin_city': shipper.origin_city,
                            'Destination_city': shipper.destination_city,
                            'Delivery_Option': shipper.delivery_option.name,
                            'Cargo_Type': shipper.cargo_type.name,
                            'Cargo_amount': shipper.cargo_amount,
                            "Cargo_Product_type": shipper.cargo_product_type,
                            'Cargo_Packing_List': shipper.cargo_packing_list,
                            'description_of_goods': shipper.description_of_goods,
                            'carrier_id': shipper.carrier_id.id,
                            'carrier_login': shipper.carrier_id.login,

                            'shipper_id': shipper.shipper_id.id,
                            'shipper_login': shipper.shipper_id.login,
                            'carrier_company': shipper.carrier_id.company_name,
                            'shipper_company': shipper.shipper_id.company_name,
                            'carrier_NTN_No': shipper.carrier_id.NTN_No,
                            'shipper_NTN': shipper.shipper_id.NTN_No,
                            'carrier_address': shipper.carrier_id.company_head_office_adrs,
                            'shipper_address': shipper.shipper_id.company_Address_street_address,

                            'booking_status': shipper.booking_status,
                            'shipper_token': shipper.shipper_id.token,
                            'carrier_token': shipper.carrier_id.token,
                            'invoice_no': shipper.invoice_no,

                            'due_date': shipper.due_date.strftime('%Y-%m-%d'),
                            'NTN_No': shipper.NTN_No,
                            'registration_no': shipper.registration_no,
                            'sales_tax': shipper.sales_tax,
                            'total_tax': shipper.grand_total-shipper.invoice_total,
                            'invoice': shipper.invoice_total,
                            'invoice_status': shipper.invoice_status,
                            'grand_total': shipper.grand_total,
                            'estimated_date': shipper.estimated_date.strftime('%Y-%m-%d'),
                            'pick_up_latitude': shipper.pick_up_latitude,
                            'pick_up_longitude': shipper.pick_up_longitude,
                            'drop_off_longitude': shipper.drop_off_longitude,
                            'drop_off_latitude': shipper.drop_off_latitude,
                            'current_longitude': shipper.current_longitude,
                            'current_latitude': shipper.current_latitude,
                            'driver_assigned': shipper.driver_id.driver_name,
                            'driver_login': shipper.driver_id.login,
                            'driver_current_longitude': shipper.driver_id.current_longitude,
                            'driver_current_latitude': shipper.driver_id.current_latitude,
                            'driver_carrier': shipper.driver_id.carrier.id,
                            'driver_status': shipper.driver_status,
                            # 'rate_per_ton': shipper.rate_per_ton,
                            'rate_type': shipper.rate_per_kg,
                            'cargo_weight': shipper.cargo_weight,
                            'cargo_weight_type':shipper.cargo_weight_type,
                            'cargo_packing_units': shipper.cargo_packing_units,

                            'pick_up_date': shipper.pick_up_date.strftime('%Y-%m-%d'),
                            'pick_up_time': shipper.pick_up_time.name,
                            'drop_off_address': shipper.drop_off_address,
                            'pick_up_address': shipper.address,
                            'driver_name': shipper.driver_id.driver_name,
                            'driver_phone': shipper.driver_id.driver_no,
                            'driver_lisence': shipper.driver_id.driver_lisence,
                            'carrier_sales_tax_no': shipper.carrier_id.sales_tax_no,
                            'packing_unit_list_file': shipper.url,
                            'actual_delivery_date': shipper.actual_delivery_date.strftime('%Y-%m-%d'),

                        }
                        booking_list.append(booking_data)
                    else:
                        booking_data = {
                            'id': shipper.id,
                            'login': shipper.login,
                            'load_type': shipper.load_type.name,
                            'Origin_city': shipper.origin_city,
                            'Destination_city': shipper.destination_city,
                            'Delivery_Option': shipper.delivery_option.name,
                            'Cargo_Type': shipper.cargo_type.name,
                            'Cargo_amount': shipper.cargo_amount,
                            "Cargo_Product_type": shipper.cargo_product_type,
                            'Cargo_Packing_List': shipper.cargo_packing_list,
                            'description_of_goods': shipper.description_of_goods,
                            'carrier_id': shipper.carrier_id.id,
                            'carrier_login': shipper.carrier_id.login,

                            'shipper_id': shipper.shipper_id.id,
                            'shipper_login': shipper.shipper_id.login,
                            'carrier_company': shipper.carrier_id.company_name,
                            'shipper_company': shipper.shipper_id.company_name,
                            'carrier_NTN_No': shipper.carrier_id.NTN_No,
                            'shipper_NTN': shipper.shipper_id.NTN_No,
                            'carrier_address': shipper.carrier_id.company_head_office_adrs,
                            'shipper_address': shipper.shipper_id.company_Address_street_address,

                            'booking_status': shipper.booking_status,
                            'shipper_token': shipper.shipper_id.token,
                            'carrier_token': shipper.carrier_id.token,
                            'invoice_no': shipper.invoice_no,

                            'due_date': shipper.due_date.strftime('%Y-%m-%d'),
                            'NTN_No': shipper.NTN_No,
                            'registration_no': shipper.registration_no,
                            'sales_tax': shipper.sales_tax,
                            'total_tax': shipper.grand_total - shipper.invoice_total,
                            'invoice': shipper.invoice_total,
                            'invoice_status': shipper.invoice_status,
                            'grand_total': shipper.grand_total,
                            'estimated_date': shipper.estimated_date.strftime('%Y-%m-%d'),
                            'pick_up_latitude': shipper.pick_up_latitude,
                            'pick_up_longitude': shipper.pick_up_longitude,
                            'drop_off_longitude': shipper.drop_off_longitude,
                            'drop_off_latitude': shipper.drop_off_latitude,
                            'current_longitude': shipper.current_longitude,
                            'current_latitude': shipper.current_latitude,
                            'driver_assigned': shipper.driver_id.driver_name,
                            'driver_login': shipper.driver_id.login,
                            'driver_current_longitude': shipper.driver_id.current_longitude,
                            'driver_current_latitude': shipper.driver_id.current_latitude,
                            'driver_carrier': shipper.driver_id.carrier.id,
                            'driver_status': shipper.driver_status,
                            'rate_type': shipper.rate_per_ton,
                            # 'rate_per_kg': shipper.rate_per_kg,
                            'cargo_weight': shipper.cargo_weight,
                            'cargo_weight_type': shipper.cargo_weight_type,
                            'cargo_packing_units': shipper.cargo_packing_units,

                            'pick_up_date': shipper.pick_up_date.strftime('%Y-%m-%d'),
                            'pick_up_time': shipper.pick_up_time.name,
                            'drop_off_address': shipper.drop_off_address,
                            'pick_up_address': shipper.address,
                            'driver_name': shipper.driver_id.driver_name,
                            'driver_phone': shipper.driver_id.driver_no,
                            'driver_lisence': shipper.driver_id.driver_lisence,

                            'carrier_sales_tax_no': shipper.carrier_id.sales_tax_no,
                            'packing_unit_list_file': shipper.url,
                            'actual_delivery_date': shipper.actual_delivery_date.strftime('%Y-%m-%d'),

                        }



                        booking_list.append(booking_data)
                parent_booking_list.append(booking_list)
                data = json.dumps(booking_list)
                return data
            else:
                data = {"response":"Record does not exist or not found"}
                return json.dumps(data)
        else:
            data = {"response":"Record does not exist or not found"}
            return json.dumps(data)