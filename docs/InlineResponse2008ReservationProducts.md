# InlineResponse2008ReservationProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The Partner supplied id for the product. | 
**unit_id** | **str** | The Partner supplied id for the reserved unit. This id will be passed into reserve and subsequent calls of the purchase. This id must be unique across all units of all reservations.  | [optional] 
**status** | **str** | The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.  | 
**expires_at** | **datetime** | A datetime representing when the reservation was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | 
**bookings** | [**list[InlineResponse2008ReservationBookings]**](InlineResponse2008ReservationBookings.md) | segments being booked in the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

