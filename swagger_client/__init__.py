# coding: utf-8

# flake8: noqa

"""
    Groupon Connect APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: 3pip@groupon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from mobidy_groupon_api.api.ingestion_feed_api import IngestionFeedApi
from mobidy_groupon_api.api.ingestion_feed_v2_api import IngestionFeedV2Api
from mobidy_groupon_api.api.transactional_partner_endpoints_api import TransactionalPartnerEndpointsApi
from mobidy_groupon_api.api.default_api import DefaultApi
# import ApiClient
from mobidy_groupon_api.api_client import ApiClient
from mobidy_groupon_api.configuration import Configuration
# import models into sdk package
from mobidy_groupon_api.models.all_ofgrouponv1reservations_reserved_units_bookings_items import AllOfgrouponv1reservationsReservedUnitsBookingsItems
from mobidy_groupon_api.models.all_ofgrouponv1reservationsreservation_idfulfillments_data_tax_details_items import AllOfgrouponv1reservationsreservationIdfulfillmentsDataTaxDetailsItems
from mobidy_groupon_api.models.all_ofgrouponv2reservationsreservation_idfulfillments_fulfillment_tax_details_items import AllOfgrouponv2reservationsreservationIdfulfillmentsFulfillmentTaxDetailsItems
from mobidy_groupon_api.models.all_ofinline_response20011_data_price_summary_base_price import AllOfinlineResponse20011DataPriceSummaryBasePrice
from mobidy_groupon_api.models.all_ofinline_response20011_data_price_summary_price import AllOfinlineResponse20011DataPriceSummaryPrice
from mobidy_groupon_api.models.all_ofinline_response20011_data_price_summary_value import AllOfinlineResponse20011DataPriceSummaryValue
from mobidy_groupon_api.models.all_ofinline_response20011_data_products_reserved_units_items import AllOfinlineResponse20011DataProductsReservedUnitsItems
from mobidy_groupon_api.models.all_ofinline_response20012_data_price_summary_price import AllOfinlineResponse20012DataPriceSummaryPrice
from mobidy_groupon_api.models.all_ofinline_response20012_data_products_reserved_units_items import AllOfinlineResponse20012DataProductsReservedUnitsItems
from mobidy_groupon_api.models.all_ofinline_response20015_offers_points_of_interest_items import AllOfinlineResponse20015OffersPointsOfInterestItems
from mobidy_groupon_api.models.all_ofinline_response20015_offers_products_items import AllOfinlineResponse20015OffersProductsItems
from mobidy_groupon_api.models.all_ofinline_response20015_offers_redemption_locations_items import AllOfinlineResponse20015OffersRedemptionLocationsItems
from mobidy_groupon_api.models.all_ofinline_response20019_merchants_attributes_items import AllOfinlineResponse20019MerchantsAttributesItems
from mobidy_groupon_api.models.all_ofinline_response20019_merchants_contacts_items import AllOfinlineResponse20019MerchantsContactsItems
from mobidy_groupon_api.models.all_ofinline_response20019_merchants_redemption_locations_items import AllOfinlineResponse20019MerchantsRedemptionLocationsItems
from mobidy_groupon_api.models.all_ofinline_response20019_merchants_services_items import AllOfinlineResponse20019MerchantsServicesItems
from mobidy_groupon_api.models.all_ofinline_response20019_merchants_writeups_items import AllOfinlineResponse20019MerchantsWriteupsItems
from mobidy_groupon_api.models.all_ofinline_response2001_bookings_items import AllOfinlineResponse2001BookingsItems
from mobidy_groupon_api.models.all_ofinline_response2004_data_items import AllOfinlineResponse2004DataItems
from mobidy_groupon_api.models.all_ofinline_response2005_products_items import AllOfinlineResponse2005ProductsItems
from mobidy_groupon_api.models.all_ofinline_response2006_accounting_details_buy_price import AllOfinlineResponse2006AccountingDetailsBuyPrice
from mobidy_groupon_api.models.all_ofinline_response2006_price_summary_base_price import AllOfinlineResponse2006PriceSummaryBasePrice
from mobidy_groupon_api.models.all_ofinline_response2006_price_summary_price import AllOfinlineResponse2006PriceSummaryPrice
from mobidy_groupon_api.models.all_ofinline_response2006_price_summary_value import AllOfinlineResponse2006PriceSummaryValue
from mobidy_groupon_api.models.all_ofinline_response2006_products_reserved_units_items import AllOfinlineResponse2006ProductsReservedUnitsItems
from mobidy_groupon_api.models.all_ofproducts_availability_body_data_items import AllOfproductsAvailabilityBodyDataItems
from mobidy_groupon_api.models.bookings_availability_body import BookingsAvailabilityBody
from mobidy_groupon_api.models.bookings_cancellations_body import BookingsCancellationsBody
from mobidy_groupon_api.models.boolean_field import BooleanField
from mobidy_groupon_api.models.email_field import EmailField
from mobidy_groupon_api.models.form_field import FormField
from mobidy_groupon_api.models.form_field_fields import FormFieldFields
from mobidy_groupon_api.models.group_field import GroupField
from mobidy_groupon_api.models.grouponv1bookings_availability import Grouponv1bookingsAvailability
from mobidy_groupon_api.models.grouponv1bookings_bookings import Grouponv1bookingsBookings
from mobidy_groupon_api.models.grouponv1bookings_purchaser_details import Grouponv1bookingsPurchaserDetails
from mobidy_groupon_api.models.grouponv1bookingsavailability_availability import Grouponv1bookingsavailabilityAvailability
from mobidy_groupon_api.models.grouponv1bookingscancellations_bookings import Grouponv1bookingscancellationsBookings
from mobidy_groupon_api.models.grouponv1reservations_data import Grouponv1reservationsData
from mobidy_groupon_api.models.grouponv1reservations_reserved_units import Grouponv1reservationsReservedUnits
from mobidy_groupon_api.models.grouponv1reservationsreservation_id_data import Grouponv1reservationsreservationIdData
from mobidy_groupon_api.models.grouponv1reservationsreservation_idfulfillments_data import Grouponv1reservationsreservationIdfulfillmentsData
from mobidy_groupon_api.models.grouponv1reservationsreservation_idunitscancellations_data import Grouponv1reservationsreservationIdunitscancellationsData
from mobidy_groupon_api.models.grouponv1reservationsreservation_idunitscancellations_data_reserved_units import Grouponv1reservationsreservationIdunitscancellationsDataReservedUnits
from mobidy_groupon_api.models.grouponv2productsavailability_availabilities import Grouponv2productsavailabilityAvailabilities
from mobidy_groupon_api.models.grouponv2productsavailability_products import Grouponv2productsavailabilityProducts
from mobidy_groupon_api.models.grouponv2reservationsreservation_idfulfillments_fulfillment import Grouponv2reservationsreservationIdfulfillmentsFulfillment
from mobidy_groupon_api.models.inline_response200 import InlineResponse200
from mobidy_groupon_api.models.inline_response2001 import InlineResponse2001
from mobidy_groupon_api.models.inline_response20010 import InlineResponse20010
from mobidy_groupon_api.models.inline_response20010_reservation import InlineResponse20010Reservation
from mobidy_groupon_api.models.inline_response20011 import InlineResponse20011
from mobidy_groupon_api.models.inline_response20011_data import InlineResponse20011Data
from mobidy_groupon_api.models.inline_response20011_data_price_summary import InlineResponse20011DataPriceSummary
from mobidy_groupon_api.models.inline_response20011_data_products import InlineResponse20011DataProducts
from mobidy_groupon_api.models.inline_response20012 import InlineResponse20012
from mobidy_groupon_api.models.inline_response20012_data import InlineResponse20012Data
from mobidy_groupon_api.models.inline_response20012_data_price_summary import InlineResponse20012DataPriceSummary
from mobidy_groupon_api.models.inline_response20012_data_products import InlineResponse20012DataProducts
from mobidy_groupon_api.models.inline_response20013 import InlineResponse20013
from mobidy_groupon_api.models.inline_response20013_data import InlineResponse20013Data
from mobidy_groupon_api.models.inline_response20014 import InlineResponse20014
from mobidy_groupon_api.models.inline_response20014_data import InlineResponse20014Data
from mobidy_groupon_api.models.inline_response20015 import InlineResponse20015
from mobidy_groupon_api.models.inline_response20015_brand import InlineResponse20015Brand
from mobidy_groupon_api.models.inline_response20015_fields import InlineResponse20015Fields
from mobidy_groupon_api.models.inline_response20015_images import InlineResponse20015Images
from mobidy_groupon_api.models.inline_response20015_offers import InlineResponse20015Offers
from mobidy_groupon_api.models.inline_response20015_provider import InlineResponse20015Provider
from mobidy_groupon_api.models.inline_response20015_purchaser_questions import InlineResponse20015PurchaserQuestions
from mobidy_groupon_api.models.inline_response20015_questions import InlineResponse20015Questions
from mobidy_groupon_api.models.inline_response20015_rating import InlineResponse20015Rating
from mobidy_groupon_api.models.inline_response20015_writeups import InlineResponse20015Writeups
from mobidy_groupon_api.models.inline_response20016 import InlineResponse20016
from mobidy_groupon_api.models.inline_response20016_errors import InlineResponse20016Errors
from mobidy_groupon_api.models.inline_response20016_purchaser_questions import InlineResponse20016PurchaserQuestions
from mobidy_groupon_api.models.inline_response20017 import InlineResponse20017
from mobidy_groupon_api.models.inline_response20018 import InlineResponse20018
from mobidy_groupon_api.models.inline_response20018_availability import InlineResponse20018Availability
from mobidy_groupon_api.models.inline_response20018_errors import InlineResponse20018Errors
from mobidy_groupon_api.models.inline_response20018_pricing import InlineResponse20018Pricing
from mobidy_groupon_api.models.inline_response20018_pricing_discounted_price import InlineResponse20018PricingDiscountedPrice
from mobidy_groupon_api.models.inline_response20018_pricing_original_price import InlineResponse20018PricingOriginalPrice
from mobidy_groupon_api.models.inline_response20018_services import InlineResponse20018Services
from mobidy_groupon_api.models.inline_response20019 import InlineResponse20019
from mobidy_groupon_api.models.inline_response20019_errors import InlineResponse20019Errors
from mobidy_groupon_api.models.inline_response20019_images import InlineResponse20019Images
from mobidy_groupon_api.models.inline_response20019_merchants import InlineResponse20019Merchants
from mobidy_groupon_api.models.inline_response20019_merchants1 import InlineResponse20019Merchants1
from mobidy_groupon_api.models.inline_response2002 import InlineResponse2002
from mobidy_groupon_api.models.inline_response2002_bookings import InlineResponse2002Bookings
from mobidy_groupon_api.models.inline_response2003 import InlineResponse2003
from mobidy_groupon_api.models.inline_response2003_bookings import InlineResponse2003Bookings
from mobidy_groupon_api.models.inline_response2004 import InlineResponse2004
from mobidy_groupon_api.models.inline_response2004_meta import InlineResponse2004Meta
from mobidy_groupon_api.models.inline_response2005 import InlineResponse2005
from mobidy_groupon_api.models.inline_response2006 import InlineResponse2006
from mobidy_groupon_api.models.inline_response2006_accounting_details import InlineResponse2006AccountingDetails
from mobidy_groupon_api.models.inline_response2006_data import InlineResponse2006Data
from mobidy_groupon_api.models.inline_response2006_price_summary import InlineResponse2006PriceSummary
from mobidy_groupon_api.models.inline_response2006_price_summary_adjustments import InlineResponse2006PriceSummaryAdjustments
from mobidy_groupon_api.models.inline_response2006_price_summary_value import InlineResponse2006PriceSummaryValue
from mobidy_groupon_api.models.inline_response2006_products import InlineResponse2006Products
from mobidy_groupon_api.models.inline_response2007 import InlineResponse2007
from mobidy_groupon_api.models.inline_response2007_data import InlineResponse2007Data
from mobidy_groupon_api.models.inline_response2007_data1 import InlineResponse2007Data1
from mobidy_groupon_api.models.inline_response2007_data1_products import InlineResponse2007Data1Products
from mobidy_groupon_api.models.inline_response2007_data1_reserved_units import InlineResponse2007Data1ReservedUnits
from mobidy_groupon_api.models.inline_response2008 import InlineResponse2008
from mobidy_groupon_api.models.inline_response2008_reservation import InlineResponse2008Reservation
from mobidy_groupon_api.models.inline_response2008_reservation_bookings import InlineResponse2008ReservationBookings
from mobidy_groupon_api.models.inline_response2008_reservation_products import InlineResponse2008ReservationProducts
from mobidy_groupon_api.models.inline_response2009 import InlineResponse2009
from mobidy_groupon_api.models.inline_response200_availability import InlineResponse200Availability
from mobidy_groupon_api.models.inline_response207 import InlineResponse207
from mobidy_groupon_api.models.inline_response2071 import InlineResponse2071
from mobidy_groupon_api.models.inline_response2071_errors import InlineResponse2071Errors
from mobidy_groupon_api.models.inline_response2072 import InlineResponse2072
from mobidy_groupon_api.models.inline_response2072_errors import InlineResponse2072Errors
from mobidy_groupon_api.models.inline_response207_errors import InlineResponse207Errors
from mobidy_groupon_api.models.inline_response400 import InlineResponse400
from mobidy_groupon_api.models.inline_response4001 import InlineResponse4001
from mobidy_groupon_api.models.inline_response40010 import InlineResponse40010
from mobidy_groupon_api.models.inline_response40010_errors import InlineResponse40010Errors
from mobidy_groupon_api.models.inline_response40011 import InlineResponse40011
from mobidy_groupon_api.models.inline_response40011_errors import InlineResponse40011Errors
from mobidy_groupon_api.models.inline_response40012 import InlineResponse40012
from mobidy_groupon_api.models.inline_response40012_errors import InlineResponse40012Errors
from mobidy_groupon_api.models.inline_response40012_services import InlineResponse40012Services
from mobidy_groupon_api.models.inline_response4001_errors import InlineResponse4001Errors
from mobidy_groupon_api.models.inline_response4001_products import InlineResponse4001Products
from mobidy_groupon_api.models.inline_response4002 import InlineResponse4002
from mobidy_groupon_api.models.inline_response4002_errors import InlineResponse4002Errors
from mobidy_groupon_api.models.inline_response4003 import InlineResponse4003
from mobidy_groupon_api.models.inline_response4003_errors import InlineResponse4003Errors
from mobidy_groupon_api.models.inline_response4004 import InlineResponse4004
from mobidy_groupon_api.models.inline_response4004_errors import InlineResponse4004Errors
from mobidy_groupon_api.models.inline_response4004_reservations import InlineResponse4004Reservations
from mobidy_groupon_api.models.inline_response4005 import InlineResponse4005
from mobidy_groupon_api.models.inline_response4005_errors import InlineResponse4005Errors
from mobidy_groupon_api.models.inline_response4006 import InlineResponse4006
from mobidy_groupon_api.models.inline_response4006_errors import InlineResponse4006Errors
from mobidy_groupon_api.models.inline_response4007 import InlineResponse4007
from mobidy_groupon_api.models.inline_response4007_errors import InlineResponse4007Errors
from mobidy_groupon_api.models.inline_response4007_units import InlineResponse4007Units
from mobidy_groupon_api.models.inline_response4008 import InlineResponse4008
from mobidy_groupon_api.models.inline_response4008_errors import InlineResponse4008Errors
from mobidy_groupon_api.models.inline_response4009 import InlineResponse4009
from mobidy_groupon_api.models.inline_response4009_errors import InlineResponse4009Errors
from mobidy_groupon_api.models.inline_response400_errors import InlineResponse400Errors
from mobidy_groupon_api.models.inline_response401 import InlineResponse401
from mobidy_groupon_api.models.inline_response4011 import InlineResponse4011
from mobidy_groupon_api.models.inline_response4011_error import InlineResponse4011Error
from mobidy_groupon_api.models.inline_response401_error import InlineResponse401Error
from mobidy_groupon_api.models.inline_response4_xx import InlineResponse4XX
from mobidy_groupon_api.models.inline_response4_xx1 import InlineResponse4XX1
from mobidy_groupon_api.models.inline_response4_xx1_bookings import InlineResponse4XX1Bookings
from mobidy_groupon_api.models.inline_response4_xx1_errors import InlineResponse4XX1Errors
from mobidy_groupon_api.models.inline_response4_xx2 import InlineResponse4XX2
from mobidy_groupon_api.models.inline_response4_xx2_bookings import InlineResponse4XX2Bookings
from mobidy_groupon_api.models.inline_response4_xx2_errors import InlineResponse4XX2Errors
from mobidy_groupon_api.models.inline_response4_xx3 import InlineResponse4XX3
from mobidy_groupon_api.models.inline_response4_xx3_errors import InlineResponse4XX3Errors
from mobidy_groupon_api.models.inline_response4_xx_errors import InlineResponse4XXErrors
from mobidy_groupon_api.models.inline_response4_xx_services import InlineResponse4XXServices
from mobidy_groupon_api.models.number_field import NumberField
from mobidy_groupon_api.models.partnerspartnerv1bookings_bookings import Partnerspartnerv1bookingsBookings
from mobidy_groupon_api.models.partnerspartnerv1reservations_data import Partnerspartnerv1reservationsData
from mobidy_groupon_api.models.partnerspartnerv1units_data import Partnerspartnerv1unitsData
from mobidy_groupon_api.models.phone_field import PhoneField
from mobidy_groupon_api.models.products_availability_body import ProductsAvailabilityBody
from mobidy_groupon_api.models.products_availability_body1 import ProductsAvailabilityBody1
from mobidy_groupon_api.models.reservation_id_fulfillments_body import ReservationIdFulfillmentsBody
from mobidy_groupon_api.models.reservation_id_fulfillments_body1 import ReservationIdFulfillmentsBody1
from mobidy_groupon_api.models.reservations_reservation_id_body import ReservationsReservationIdBody
from mobidy_groupon_api.models.text_field import TextField
from mobidy_groupon_api.models.units_cancellations_body import UnitsCancellationsBody
from mobidy_groupon_api.models.v1_bookings_body import V1BookingsBody
from mobidy_groupon_api.models.v1_bookings_body1 import V1BookingsBody1
from mobidy_groupon_api.models.v1_reservations_body import V1ReservationsBody
from mobidy_groupon_api.models.v1_reservations_body1 import V1ReservationsBody1
from mobidy_groupon_api.models.v1_units_body import V1UnitsBody
from mobidy_groupon_api.models.v2_reservations_body import V2ReservationsBody
