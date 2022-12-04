# InlineResponse200

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | An unique merchant id provided by partners.  | 
**availability** | [**list[InlineResponse200Availability]**](InlineResponse200Availability.md) | An array of availabilities for a service corresponding to requested parameters. All availability segments within the requested time range and with the attributes specified in the request. If request doesn&#x27;t have the attributes array, all availability segments that are available for the requested time range should be returned. If there is no availability for the requested service, an empty array or null is to be returned.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

