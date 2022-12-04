# V1BookingsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | the ID of the merchant | 
**groupon_customer_service_id** | **str** | Groupon’s Customer Service reference ID for the purchase associated with this booking. This can be used when communicating with Groupon Customer Service to reference the purchase.  | [optional] 
**bookings** | [**list[Grouponv1bookingsBookings]**](Grouponv1bookingsBookings.md) | This is a list of bookings that should be created. | 
**purchaser_details** | [**Grouponv1bookingsPurchaserDetails**](Grouponv1bookingsPurchaserDetails.md) |  | [optional] 
**booking_type** | **str** | Determines whether the bookings should be created (as &#x60;confirmed&#x60;), or only pre-reserved (&#x60;hold&#x60;) until confirmation.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

