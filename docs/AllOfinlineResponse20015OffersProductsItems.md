# AllOfinlineResponse20015OffersProductsItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_category_id** | **str** | The primary categorization for this product. This field is a uuid and the only acceptable values are the provided categorization uuids (please see the section on Categorization).  | 
**categories** | **list[object]** | The list of additional categorization for this product.  | [optional] 
**purchase_url** | **str** | The URL used to link out to an external purchase page. This field is optional, and only used for link out offers which leave the Groupon site when the user clicks the buy button.  | [optional] 
**iframe_url** | **str** | The URL used to render iframe content when this offer is using iframe transactions. This field is optional, and only used for iframe transactions.  A parameter called “grouponOpportunityId” will be appended to this URL with Groupon’s opportunity id for tracking purposes.  | [optional] 
**expires_at** | **datetime** | The datetime which specifies when the product expires. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  | [optional] 
**expires_in_days_from_purchase** | **int** | Specifies the number of days relative from purchase which the product expires. This allows non-fixed expiration based on the purchase date by a user. This is used to signal to the user that the product expires a certain number of days from the date of purchase.  | [optional] 
**pricing** | **object** |  | 
**redemption_locations** | **list[object]** | The list of locations at which this product can be redeemed.  | [optional] 
**points_of_interest** | **list[object]** | A list of locations that will show up in a map to give more context to the purchaser. For example this can be used for locations that a tour will visit. If pointsOfInterest aren&#x27;t present, we will show the redemptionLocations on the map.  | [optional] 
**writeups** | **list[object]** | The text which describes the specific items or services being offered.  | 
**fulfillment_type** | **str** | The type of fulfillment for this product. This indicates how the user will receive the product after purchase.  &#x60;Pickup&#x60; indicates the purchaser must go and pick up their product, such as \&quot;will call\&quot; for tickets.  &#x60;Shipped&#x60; indicates that the product will be shipped to the purchaser.  &#x60;Electronic&#x60; indicates that the purchaser will receive their product electronically, such as a PDF version of a ticket or voucher. Please note that this means that the &#x60;data.products[].reservedUnits[].details.voucherUrl&#x60; attribute on the reservation in the transactional endpoints needs to be set when the purchase is fulfilled.  | [optional] 
**restrictions** | **object** | The restrictions associated with this product. | [optional] 
**performers** | **list[object]** | The performers or artists associated with this product.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

