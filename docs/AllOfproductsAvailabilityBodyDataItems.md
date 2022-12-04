# AllOfproductsAvailabilityBodyDataItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The quantity of this product being reserved, usually used for voucher purchases.  When &#x60;prereservationId&#x60; is passed, then this attribute will not be included in the request since the quantity has already been established during the iframe flow.    When sending &#x60;bookings&#x60; this attribute will not be included since the quantity is determined by the number of bookings.  | [optional] 
**purchaser_answers** | **list[dict(str, str)]** | DEPRECATED, use the answers provided in the reserve call instead.    Answers provided by the purchaser on the questions of this product.   See *offers.products.purchaserQuestionIds* in ingestion feed.  | [optional] 
**bookings** | **list[object]** | This can be used when booking more than one availability slot or if there are multiple availability slots for the same time range. Note that purchaserAnswers are not going to be present in this API call, they will be sent in the Reserve call instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

