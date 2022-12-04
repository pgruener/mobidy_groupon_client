# Grouponv1bookingsAvailability

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the availability slot. See in ingestion availability spec *availability[].id*  | [optional] 
**available_at** | **datetime** | The start time and date of the availability slot/segment to be booked.  | 
**available_until** | **datetime** | The end time and date of the availability slot/segment to be booked.  | 
**service_id** | **str** | The IDs of the specific service to book.  | 
**attribute_ids** | **list[str]** | Reference to the attribute values that this availability slot has.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

