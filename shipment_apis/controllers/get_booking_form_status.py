# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipperList(http.Controller):

    @http.route('/shipper/Return/Shipper', auth='public', website=True)
    def shipper_Booking_form_list(self, **kw):
        shipper = kw.get('shipper_id')
        shipper_id = int(shipper)
        booking_status = kw.get('booking_status')
        invoice_status = kw.get('invoice_status')
        if shipper_id:
            if booking_status == "pending":

                booking_details = request.env['shipment.shipment_booking'].sudo().search([('shipper_id', '=', shipper_id),('booking_status', '=', 'pending'),('shipper_id.account_status', '=', 'active')])
            elif booking_status == "accept":

                booking_details = request.env['shipment.shipment_booking'].sudo().search([('shipper_id', '=', shipper_id),('booking_status', '=', 'accept'),('shipper_id.account_status', '=', 'active')])
            elif booking_status == "reject":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('shipper_id', '=', shipper_id), ('booking_status', '=', 'reject'),('shipper_id.account_status', '=', 'active')])
            elif booking_status == "complete":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('shipper_id', '=', shipper_id), ('booking_status', '=', 'complete'),('shipper_id.account_status', '=', 'active')])
            elif booking_status == "in_progress":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('shipper_id', '=', shipper_id), ('booking_status', '=', 'in_progress'),('shipper_id.account_status', '=', 'active')])
            elif booking_status == "previous":

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('shipper_id', '=', shipper_id), ('booking_status', '=', 'previous'),('shipper_id.account_status', '=', 'active')])
            elif invoice_status:

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('shipper_id', '=', shipper_id), ('invoice_status', '=', invoice_status),('shipper_id.account_status', '=', 'active')])
                print((booking_details))

            else:

                booking_details = request.env['shipment.shipment_booking'].sudo().search(
                    [('shipper_id', '=', shipper_id),('shipper_id.account_status', '=', 'active')])



            print(booking_details)
            if booking_details:
                parent_booking_list = []
                booking_list = []
                for shipper in booking_details:
                    print(shipper.id)
                    if shipper.cargo_weight_type == 'kg':
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
                            'invoice': shipper.invoice,
                            'invoice_status': shipper.invoice_status,
                            'grand_total': shipper.grand_total,
                            'recipient_company_name': shipper.recipient_company_name,
                            'recipient_contact_person_name': shipper.recipient_contact_person_name,
                            'recipient_contact_number': shipper.recipient_contact_number,
                            'recipient_contact_email': shipper.recipient_contact_email,
                            'actual_delivery_date': shipper.actual_delivery_date.strftime('%Y-%m-%d'),
                            'pick_up_time': shipper.pick_up_time.name,
                            'pick_up_date': shipper.pick_up_date.strftime('%Y-%m-%d'),
                            'estimated_date': shipper.estimated_date.strftime('%Y-%m-%d'),
                            'drop_off_time': shipper.drop_off_time.name,
                            'driver_status': shipper.driver_status,
                            'driver_id': shipper.driver_id.id,
                            'driver_name': shipper.driver_id.driver_name,
                            'address': shipper.address,
                            'drop_off_address': shipper.drop_off_address,
                            'shipper_image_url': shipper.shipper_id.url,
                            'cargo_packing_units': shipper.cargo_packing_units,
                            'packing_unit_list_file': shipper.url,
                            'description_of_goods': shipper.description_of_goods,
                            'rate_type': shipper.rate_per_kg,
                        }
                        booking_list.append(booking_data)
                        parent_booking_list.append(booking_list)
                        data = json.dumps(booking_list)

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
                            'carrier_id': shipper.carrier_id.id,
                            'carrier_login': shipper.carrier_id.login,
                            'shipper_id': shipper.shipper_id.id,
                            'shipper_login': shipper.shipper_id.login,
                            'carrier_company': shipper.carrier_id.company_name,
                            'shipper_company': shipper.shipper_id.company_name,
                            'carrier_NTN_No': shipper.carrier_id.NTN_No,
                            'shipper_NTN': shipper.shipper_id.NTN_No,
                            'carrier_NTN': shipper.carrier_id.company_NTN,
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
                            'invoice': shipper.invoice,
                            'invoice_status': shipper.invoice_status,
                            'grand_total': shipper.grand_total,
                            'recipient_company_name': shipper.recipient_company_name,
                            'recipient_contact_person': shipper.recipient_contact_person_name,
                            'recipient_contact_number': shipper.recipient_contact_number,
                            'recipient_contact_email': shipper.recipient_contact_email,
                            'actual_delivery_date': shipper.actual_delivery_date.strftime('%Y-%m-%d'),
                            'pick_up_time': shipper.pick_up_time.name,
                            'drop_off_time': shipper.drop_off_time.name,
                            'driver_status': shipper.driver_status,
                            'driver_id': shipper.driver_id.driver_name,
                            'pick_up_date': shipper.pick_up_date.strftime('%Y-%m-%d'),
                            'estimated_date': shipper.estimated_date.strftime('%Y-%m-%d'),
                            'driver_name': shipper.driver_id.driver_name,
                            'address': shipper.address,
                            'drop_off_address': shipper.drop_off_address,
                            'shipper_image_url': shipper.shipper_id.url,
                            'rate_type': shipper.rate_per_ton,
                            'cargo_packing_units': shipper.cargo_packing_units,
                            'packing_unit_list_file': shipper.url,
                            'description_of_goods': shipper.description_of_goods,



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
