# InlineResponse20012DataProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Partner supplied id for the product. | 
**category_id** | **str** | The categorization for this product.  This field is a uuid and the only acceptable values are the provided categorization uuids.  | [optional] 
**quantity** | **int** | The quantity of this product being reserved. This isn&#x27;t used if bookings are present. | [optional] 
**price_summary** | [**InlineResponse20012DataPriceSummary**](InlineResponse20012DataPriceSummary.md) |  | 
**accounting_details** | [**InlineResponse2006AccountingDetails**](InlineResponse2006AccountingDetails.md) |  | [optional] 
**reserved_units** | **list[AllOfinlineResponse20012DataProductsReservedUnitsItems]** | An array of reserved units. This section may also be used for iframe bookings to pass details from the partner back to Groupon about the reservation. If quantity is specified in the request, the size of this array should match the quantity in the request.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

