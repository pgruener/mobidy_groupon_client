# InlineResponse2002Bookings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The partner-generated id for this booking. This id must be unique across all bookings for this unit. | 
**groupon_booking_id** | **str** | Groupon’s Booking reference ID.  | [optional] 
**created_at** | **datetime** | A datetime representing when the booking was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | [optional] 
**updated_at** | **datetime** | A datetime representing when the booking was last updated. Required if implementing the &#x60;units/{unitId}/bookings&#x60; endpoint. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | 
**cancellation_deadline** | **datetime** | The date and tme which specifies until when the booking is eligible for cancellation by end user. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | [optional] 
**status** | **str** | Status of the booking. Required if implementing the &#x60;bookings&#x60; endpoint. These are the meanings of each one: * &#x60;hold&#x60;: The booking has a temporary hold, and a later request can be made to confirm it. * &#x60;confirmed&#x60;: The booking is confirmed and the customer can make use of it. * &#x60;cancelled&#x60;: The booking was previously &#x60;confirmed&#x60;, but has since then been cancelled. Customer can&#x27;t make use of the booking.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

