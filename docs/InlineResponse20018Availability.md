# InlineResponse20018Availability

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The partner’s external unique identifier for this availability information. The expectation is that this id will uniquely identify the data in the partner’s system.  | [optional] 
**available_at** | **datetime** | The date and time which specifies when the availability slot/segment first becomes available. This field is inclusive in terms of the availability, meaning that the slot/segment is available exactly at the moment this datetime specifies. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | 
**available_until** | **datetime** | The date and time which specifies when the availability slot/segment stops being available. This field is exclusive in terms of the availability, meaning that the slot/segment is not available exactly at the moment this datetime specifies. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | [optional] 
**service_ids** | **list[str]** | reference to the services that are available at this slot (*merchant[].services[].id*). | 
**attribute_ids** | **list[str]** | reference to the attribute values that this availability slot has (*merchant[].attributes[].values[].id*). | [optional] 
**estimated_remaining_quantity** | **int** | The estimated quantity remaining for this availability slot/segment. This value does not need to be real time, as it is used to inform remaining quantity but not control purchasing.  | [optional] 
**pricing** | [**InlineResponse20018Pricing**](InlineResponse20018Pricing.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

