# AllOfinlineResponse2004DataItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The categorization for this product.  This field is a uuid and the only acceptable values are the provided categorization uuids.  | [optional] 
**quantity_summary** | **object** |  | [optional] 
**price_summary** | **object** |  | 
**prereservation_price_summary** | **object** | Object which contains the price associated with the pre-reservation ID if it has changed. This object should only be returned if there was a price change, and the price.amount value must differ from the priceSummary.price.amount value.  | [optional] 
**writeups** | **object** | Object which contains the partner supplied texts to be displayed to customers on an item. Note that the text needs to be localized with the **locale** parameter value.  | [optional] 
**reserved_units** | **list[object]** | An array of reserved units from the result of this availability check. This section is optional, and is used typically when passing both a product id and attributes in the check availability call in order to identify the specific units being reserved in the reserve call. It is also used to denote units which have a temporary hold placed on them for the user, allowing the user a certain amount of time to claim (i.e. reserve) the inventory before the temporary hold is lost. This section may also be used for iframe bookings to pass details from the partner back to Groupon about the reservation. Please note that if quantity is specified in the request and this is specified in the response, the size of this array should match the quantity in the request.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

