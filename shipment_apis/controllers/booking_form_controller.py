# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentBooking(http.Controller):

    @http.route('/shipment/booking/form', auth='public', website=True)
    def shipment_booking_form(self, **kw):
        shipment = kw.get('shipment_id')
        shipment_id = int(shipment)
        if shipment_id:
            booking_details = request.env['shipment.shipment_booking'].sudo().search([('id','=',shipment_id),('shipper_id.account_status', '=', 'active')],limit=1)
            if not booking_details.id:
                data = {"response": "Shipment ID doesnt exist or not active"}
                return json.dumps(data)
            booking_list = []
            parent_booking_list=[]
            if booking_details.cargo_weight_type == 'kg':
                booking_data = {
                    'id':booking_details.id,
                    'load_type': booking_details.load_type.name,
                    'origin_city': booking_details.origin_city,
                    'destination_city': booking_details.destination_city,
                    'delivery_Option': booking_details.delivery_option.name,
                    'cargo_Type': booking_details.cargo_type.name,
                    'cargo_amount': booking_details.cargo_amount,
                    "cargo_Product_type": booking_details.cargo_product_type,
                    'cargo_Packing_List': booking_details.cargo_packing_list,
                    'carrier_id': booking_details.carrier_id.id,
                    'carrier_company': booking_details.carrier_id.company_name,
                    'carrier_address': booking_details.carrier_id.company_head_office_adrs,
                    'carrier_ntn': booking_details.carrier_id.company_NTN,
                    'carrier_login': booking_details.carrier_id.login,
                    'carrier_ntn_no': booking_details.carrier_id.NTN_No,
                    'carrier_sales_tax_no': booking_details.carrier_id.sales_tax_no,
                    'shipper_id': booking_details.shipper_id.id,
                    'shipper_company': booking_details.shipper_id.company_name,
                    'shipper_ntn_no': booking_details.shipper_id.NTN_No,
                    'shipper_ntn': booking_details.shipper_id.company_NTN,
                    'shipper_address': booking_details.shipper_id.company_Address_street_address,
                    'shipper_login': booking_details.shipper_id.login,
                    'pickup_address':booking_details.address,
                    'booking_status': booking_details.booking_status,
                    'description_of_goods': booking_details.description_of_goods,
                    'cargo_weight': booking_details.cargo_weight,
                    'cargo_weight_type': booking_details.cargo_weight_type,
                    'cargo_packing_units': booking_details.cargo_packing_units,
                    'pick_up_date': booking_details.pick_up_date.strftime('%Y-%m-%d'),
                    'pick_up_time': booking_details.pick_up_time.name,
                    'drop_off_time': booking_details.drop_off_time.name,
                    'recipient_company_name': booking_details.recipient_company_name,
                    'recipient_contact_person_name': booking_details.recipient_contact_person_name,
                    'recipient_contact_number': booking_details.recipient_contact_number,
                    'recipient_contact_email': booking_details.recipient_contact_email,
                    'drop_off_address': booking_details.drop_off_address,
                    'invoice_total': booking_details.invoice_total,
                    'grand_total': booking_details.grand_total,
                    'ntn_No ': booking_details.NTN_No,
                    'due_date': booking_details.due_date.strftime('%Y-%m-%d'),
                    'invoice_status ': booking_details.invoice_status,
                    'registration_no': booking_details. registration_no,
                    'sales_tax': booking_details.sales_tax,
                    'invoice_no': booking_details.invoice_no,
                    'pick_up_latitude': booking_details.pick_up_latitude,
                    'pick_up_longitude': booking_details.pick_up_longitude,
                    'drop_off_longitude': booking_details.drop_off_longitude,
                    'drop_off_latitude': booking_details.drop_off_latitude,
                    'current_longitude': booking_details.drop_off_latitude,
                    'current_latitude': booking_details.drop_off_latitude,
                    'driver_assigned': booking_details.driver_id.driver_name,
                    'driver_status': booking_details.driver_status,
                    'rate_type': booking_details.rate_per_kg,
                    'estimated_date': booking_details.estimated_date.strftime('%Y-%m-%d'),
                    'actual_delivery_date': booking_details.actual_delivery_date.strftime('%Y-%m-%d'),
                }

                booking_list.append(booking_data)
                parent_booking_list.append(booking_list)
                data = json.dumps(booking_list)
                print(data)
                return data
            if booking_details.cargo_weight_type == 'ton':
                booking_data = {
                    # 'id': booking_details.id,
                    # 'load_type': booking_details.load_type.name,
                    # 'Origin_city': booking_details.origin_city,
                    # 'Destination_city': booking_details.destination_city,
                    # 'Delivery_Option': booking_details.delivery_option,
                    # 'Cargo_Type': booking_details.cargo_type.name,
                    # 'Cargo_amount': booking_details.cargo_amount,
                    # "Cargo_Product_type": booking_details.cargo_product_type,
                    # 'Cargo_Packing_List': booking_details.cargo_packing_list,
                    # 'carrier_id': booking_details.carrier_id.id,
                    # 'carrier_company': booking_details.carrier_id.company_name,
                    # 'carrier_address': booking_details.carrier_id.company_head_office_adrs,
                    # 'carrier_ntn': booking_details.carrier_id.company_NTN,
                    # 'carrier_login': booking_details.carrier_id.login,
                    # 'carrier_ntn_no': booking_details.carrier_id.NTN_No,
                    # 'shipper_id': booking_details.shipper_id.id,
                    # 'shipper_company': booking_details.shipper_id.company_name,
                    # 'shipper_ntn_no': booking_details.shipper_id.NTN_No,
                    # 'shipper_ntn': booking_details.shipper_id.company_NTN,
                    # 'shipper_address': booking_details.shipper_id.company_Address_street_address,
                    # 'shipper_login': booking_details.shipper_id.login,
                    # 'pickup_address': booking_details.address,
                    # 'booking_status': booking_details.booking_status,
                    # 'description_of_goods': booking_details.description_of_goods,
                    # 'cargo_weight': booking_details.cargo_weight,
                    # 'cargo_weight_type': booking_details.cargo_weight_type,
                    # 'cargo_packing_units': booking_details.cargo_packing_units,
                    # 'pick_up_date': booking_details.pick_up_date.strftime('%Y-%m-%d'),
                    # 'pick_up_time': booking_details.pick_up_time,
                    # 'drop_off_time': booking_details.drop_off_time,
                    # 'recipient_company_name': booking_details.recipient_company_name,
                    # 'recipient_contact_person_name': booking_details.recipient_contact_person_name,
                    # 'recipient_contact_number': booking_details.recipient_contact_number,
                    # 'recipient_contact_email': booking_details.recipient_contact_email,
                    # 'drop_off_address': booking_details.drop_off_address,
                    # 'invoice_total': booking_details.invoice_total,
                    # 'grand_total': booking_details.grand_total,
                    # 'NTN_No ': booking_details.NTN_No,
                    # 'due_date': booking_details.due_date.strftime('%Y-%m-%d'),
                    # 'invoice_status ': booking_details.invoice_status,
                    # 'registration_no': booking_details.registration_no,
                    # 'sales_tax': booking_details.sales_tax,
                    # 'invoice_no': booking_details.invoice_no,
                    # 'pick_up_latitude': booking_details.pick_up_latitude,
                    # 'pick_up_longitude': booking_details.pick_up_longitude,
                    # 'drop_off_longitude': booking_details.drop_off_longitude,
                    # 'drop_off_latitude': booking_details.drop_off_latitude,
                    # 'current_longitude': booking_details.drop_off_latitude,
                    # 'current_latitude': booking_details.drop_off_latitude,
                    # 'driver_assigned': booking_details.driver_id.driver_name,
                    # 'driver_status': booking_details.driver_status,
                    # 'rate_type': booking_details.rate_per_ton,
                    # 'estimated_date': booking_details.estimated_date.strftime('%Y-%m-%d'),
                    # 'actual_delivery_date': booking_details.actual_delivery_date.strftime('%Y-%m-%d'),
                    'id': booking_details.id,
                    'load_type': booking_details.load_type.name,
                    'origin_city': booking_details.origin_city,
                    'destination_city': booking_details.destination_city,
                    'delivery_Option': booking_details.delivery_option.name,
                    'cargo_Type': booking_details.cargo_type.name,
                    'cargo_amount': booking_details.cargo_amount,
                    "cargo_Product_type": booking_details.cargo_product_type,
                    'cargo_Packing_List': booking_details.cargo_packing_list,
                    'carrier_id': booking_details.carrier_id.id,
                    'carrier_company': booking_details.carrier_id.company_name,
                    'carrier_address': booking_details.carrier_id.company_head_office_adrs,
                    'carrier_ntn': booking_details.carrier_id.company_NTN,
                    'carrier_login': booking_details.carrier_id.login,
                    'carrier_ntn_no': booking_details.carrier_id.NTN_No,
                    'shipper_id': booking_details.shipper_id.id,
                    'shipper_company': booking_details.shipper_id.company_name,
                    'shipper_ntn_no': booking_details.shipper_id.NTN_No,
                    'shipper_ntn': booking_details.shipper_id.company_NTN,
                    'shipper_address': booking_details.shipper_id.company_Address_street_address,
                    'shipper_login': booking_details.shipper_id.login,
                    'pickup_address': booking_details.address,
                    'booking_status': booking_details.booking_status,
                    'description_of_goods': booking_details.description_of_goods,
                    'cargo_weight': booking_details.cargo_weight,
                    'cargo_weight_type': booking_details.cargo_weight_type,
                    'cargo_packing_units': booking_details.cargo_packing_units,
                    'pick_up_date': booking_details.pick_up_date.strftime('%Y-%m-%d'),
                    'pick_up_time': booking_details.pick_up_time.name,
                    'drop_off_time': booking_details.drop_off_time.name,
                    'recipient_company_name': booking_details.recipient_company_name,
                    'recipient_contact_person_name': booking_details.recipient_contact_person_name,
                    'recipient_contact_number': booking_details.recipient_contact_number,
                    'recipient_contact_email': booking_details.recipient_contact_email,
                    'drop_off_address': booking_details.drop_off_address,
                    'invoice_total': booking_details.invoice_total,
                    'grand_total': booking_details.grand_total,
                    'ntn_No ': booking_details.NTN_No,
                    'due_date': booking_details.due_date.strftime('%Y-%m-%d'),
                    'invoice_status ': booking_details.invoice_status,
                    'registration_no': booking_details.registration_no,
                    'sales_tax': booking_details.sales_tax,
                    'invoice_no': booking_details.invoice_no,
                    'pick_up_latitude': booking_details.pick_up_latitude,
                    'pick_up_longitude': booking_details.pick_up_longitude,
                    'drop_off_longitude': booking_details.drop_off_longitude,
                    'drop_off_latitude': booking_details.drop_off_latitude,
                    'current_longitude': booking_details.drop_off_latitude,
                    'current_latitude': booking_details.drop_off_latitude,
                    'driver_assigned': booking_details.driver_id.driver_name,
                    'driver_status': booking_details.driver_status,
                    'rate_type': booking_details.rate_per_ton,
                    'carrier_sales_tax_no': booking_details.carrier_id.sales_tax_no,
                    'estimated_date': booking_details.estimated_date.strftime('%Y-%m-%d'),
                    'actual_delivery_date': booking_details.actual_delivery_date.strftime('%Y-%m-%d'),
                }
                booking_list.append(booking_data)
                parent_booking_list.append(booking_list)
                data = json.dumps(booking_list)
                print(data)
                return data
        else:

            data = {"response": "Shipment ID doesnt exist"}
            return json.dumps(data)

