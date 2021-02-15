# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class ShipmentBooking(http.Controller):

    @http.route('/shipment/carrier/info', auth='public', website=True)
    def shipment_booking_form(self, **kw):
        login = kw.get('login')
        password = kw.get('password')
        token = kw.get('token')
        print(login)
        carrier_info_details = request.env['carrier.carrier'].sudo().search(
            ['|', ('login', '=', login), ('phone', '=', login)], limit=1)
        print(carrier_info_details)
        if carrier_info_details:
            if password == carrier_info_details.password and carrier_info_details.state=='active':
                carrier_info_details.token=token
                #many2one data in city operated field
                City_Operated = carrier_info_details.city_operated
                city_list = []
                parent_city_list = []
                for i in City_Operated:
                    city_list.append({
                        # 'Name': i.add_addresses,
                        'id': i.id,
                        'City Operated': i.truck_stop_person,
                        'Number': i.truck_stop_perosn_no,
                        'Address': i.truck_stop,
                    })
                parent_city_list.append(city_list)

                Truck_Fleet_Data = carrier_info_details.truck_fleet
                truck_fleet_list = []
                parent_truck_fleet_list = []
                for i in Truck_Fleet_Data:
                    truck_fleet_list.append({
                        # 'Type': i,
                        'id': i.id,
                        'truck_type': i.name,
                        'Registration_No': i.truck_reg_no,
                        'Loading Capacity': i.truck_load,
                        'Truck_Chassi': i.truck_chassi,
                        'Truck City': i.truck_city,
                        'City_Operated': i.truck_operated,
                        'Truck_Size': i.truck_size,
                    })

                parent_truck_fleet_list.append(truck_fleet_list)


                Contact_Person_Data = carrier_info_details.contact_person
                contact_person_list = []
                parent_contact_person_list = []
                for i in Contact_Person_Data:
                    contact_person_list.append({
                        'id': i.id,
                        'Contact_No':i.contact_no_1,
                        'Contact_Person':i.contact_person_1,
                        'Designation': i.designation_1,
                    })

                parent_contact_person_list.append(contact_person_list)

                Bank_Info_Data = carrier_info_details.bank_accounts
                bank_info_list = []
                parent_bank_info_list = []
                for i in Bank_Info_Data:
                    bank_info_list.append({
                        'id': i.id,
                        'Bank_Name': i.bank_info,
                        'Beneficiary_Name': i.beneficiary_name,
                        'Account_Type': i.account_type,
                        'Account_No': i.account_no,
                        'Swift_Code': i.swift_code,
                        'Bank_Address': i.bank_address,

                    })
                print(bank_info_list)
                parent_bank_info_list.append(bank_info_list)
                # Driver_data = carrier_info_details.driver_data
                # driver_data_list = []
                # parent_driver_data_list = []

                # for i in Driver_data:
                #     driver_data_list.append({
                #         'id': i.id,
                #         'Driver_Name': i.driver_name,
                #         'Driver_Phone_Number': i.driver_no,
                #         'Driver_Lisence': i.driver_lisence,
                #     })
                # parent_driver_data_list.append(driver_data_list)

                Lane = carrier_info_details.lane
                lane_data = []
                parent_lane_data=[]

                for i in Lane:
                    lane_data.append({
                        'id': i.id,
                        'Origin_City': i.origin_city,
                        'destination_City': i.destination_city,
                        'price_per_lane': i.price_per_lane,
                        'days_required': i.days_required,
                        'price_per_ton': i.price_per_ton,
                        'provisional_tax': i.provisional_tax,
                    })
                    print("lane data", lane_data)
                parent_lane_data.append(lane_data)


                carrier_info_list = []
                parent_carrier_info_list = []

                carrier_info_data = {
                    'id': carrier_info_details.id,
                    'Company_Name': carrier_info_details.company_name,
                    'Company_NTN': carrier_info_details.company_NTN,
                    'phone': carrier_info_details.phone,
                    'NTN_No': carrier_info_details.NTN_No,
                    'token': carrier_info_details.token,

                    'Company_Head_Office_adrs': carrier_info_details.company_head_office_adrs,
                    'login': carrier_info_details.login,
                    'password': carrier_info_details.password,
                    'confirm pass': carrier_info_details.confirmpass,
                    'Rate': carrier_info_details.rate_type,
                    'Type': carrier_info_details.truckk.name,
                    'Delivery_Time': carrier_info_details.delivery_time,
                    'image_url': carrier_info_details.url,
                    'carrier_sales_tax_no': carrier_info_details.sales_tax_no,
                    'Rate_Truck': carrier_info_details.rate_truck,
                    # 'Effective_Date':(not return in json)

                }

                carrier_info_list.append(carrier_info_data)
                parent_carrier_info_list.append(carrier_info_list)

                list = parent_carrier_info_list + parent_city_list + parent_truck_fleet_list+ parent_contact_person_list + parent_bank_info_list + parent_lane_data
                print(list)
                data = json.dumps(list)
                return data
            else:
                args = {'success': False, 'message': 'Password is Incorrect'}
                return json.dumps(args)
        else:
            args = {'success': False, 'message': 'User Doesnt Exist'}
            return json.dumps(args)