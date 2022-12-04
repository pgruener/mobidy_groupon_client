# InlineResponse2008Reservation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | The partner-generated id for this reservation. This id must be unique across all reservations. | 
**status** | **str** | The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.  | 
**created_at** | **datetime** | A datetime representing when the reservation was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | 
**updated_at** | **datetime** | A datetime representing when the reservation was last updated. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | 
**products** | [**list[InlineResponse2008ReservationProducts]**](InlineResponse2008ReservationProducts.md) | An array of products involved with this reservation | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

