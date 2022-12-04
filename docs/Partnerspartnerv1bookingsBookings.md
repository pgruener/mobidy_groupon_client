# Partnerspartnerv1bookingsBookings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The partner-generated id for this booking. This will be the id returned from the Booking Creation API call.  | 
**merchant_id** | **str** | The merchant id for this booking. | 
**status** | **str** | The update for this booking: - &#x60;check-in&#x60;: the customer successfully checked-in for the booking. - &#x60;no-show&#x60;: the customer missed the booking. - &#x60;cancelled&#x60;: the booking was cancelled by the merchant.  | 
**updated_at** | **datetime** | A datetime representing when the booking was last updated. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

