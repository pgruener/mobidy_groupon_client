# Grouponv1bookingsavailabilityAvailability

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_at** | **datetime** | The date and time which specifies the beging of the first availability slot/segment.  | 
**available_until** | **datetime** | The date and time which specifies the end of the last availability slot/segment.  | 
**service_ids** | **list[str]** | Reference to the service IDs for this availability slot. The value provided by partners in the merchant catalog feed.  | 
**attribute_ids** | **list[str]** | Reference to the attribute values that should be used as a filter for the availability request. If attribute values are not provided for the attribute, then availability with any value of that attribute should be returned. If this array is empty or null, then segments/slots with any attributes should be returned.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

