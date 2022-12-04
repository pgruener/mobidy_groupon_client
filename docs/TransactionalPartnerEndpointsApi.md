# mobidy_groupon_api.TransactionalPartnerEndpointsApi

All URIs are relative to *https://{your domain}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reservations**](TransactionalPartnerEndpointsApi.md#get_reservations) | **GET** /groupon/v1/reservations | Search Reservations
[**get_reservations_id_v2**](TransactionalPartnerEndpointsApi.md#get_reservations_id_v2) | **GET** /groupon/v2/reservations/{reservationId} | Retrieve Reservation
[**get_system_availability**](TransactionalPartnerEndpointsApi.md#get_system_availability) | **GET** /groupon/v1/system/availability | Heartbeat
[**post_products_availability_v2**](TransactionalPartnerEndpointsApi.md#post_products_availability_v2) | **POST** /groupon/v2/products/availability | Check Availability
[**post_reservations_id_cancellations_v2**](TransactionalPartnerEndpointsApi.md#post_reservations_id_cancellations_v2) | **POST** /groupon/v2/reservations/{reservationId}/cancellations | Cancel v2
[**post_reservations_id_fulfillments_v2**](TransactionalPartnerEndpointsApi.md#post_reservations_id_fulfillments_v2) | **POST** /groupon/v2/reservations/{reservationId}/fulfillments | Fulfill V2
[**post_reservations_id_unit_cancellations**](TransactionalPartnerEndpointsApi.md#post_reservations_id_unit_cancellations) | **POST** /groupon/v1/reservations/{reservationId}/units/cancellations | Unit Cancel
[**post_reservations_v2**](TransactionalPartnerEndpointsApi.md#post_reservations_v2) | **POST** /groupon/v2/reservations | Reserve
[**put_reservations_id**](TransactionalPartnerEndpointsApi.md#put_reservations_id) | **PUT** /groupon/v1/reservations/{reservationId} | Update Reservation

# **get_reservations**
> InlineResponse2006 get_reservations(locale, updated_since, updated_until, status=status, offset=offset, limit=limit)

Search Reservations

This endpoint is a search endpoint for Groupon to retrieve a collection of relevant reservations matching a specified query. This endpoint will be used by Groupon for post-purchase reservation status reconciliations with partner. This helps to reduce multiple calls to partner on individual reservation with Retrieve Reservation api and consolidating into fewer bulk calls.  The results should be sorted by the reservation updatedAt field in ascending order, then by the id field in ascending order. Sorting will ensure records maintain definite order across pagination queries.  To ensure Groupon polls all the updated reservations with the endpoint, the reservation updatedAt field should be updated by partner when: * Reservation status is updated * ReservedUnits associated with reservation are updated  Note: Groupon will make calls to this endpoint at recurring intervals and paginate over the results if needed.  For example if calling every 10 minutes: t: /groupon/v1/reservations?status=fulfilled&updatedSince=2018-11-04T00:00:00Z&updatedUntil=2018-11-04T00:10:00Z&limit=100&offset=0&locale=en_US t+10min: /groupon/v1/reservations?status=fulfilled&updatedSince=2018-11-04T00:10:00Z&updatedUntil=2018-11-04T00:20:00Z&limit=100&offset=0&locale=en_US ## Expected SLA TP99 1000ms at 100rpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
updated_since = '2013-10-20T19:20:30+01:00' # datetime | Returns reservations changed since this timestamp as determined by the updatedAt field (updatedAt >= updatedSince). Datetime should be a UTC time and formatted as yyyy-MM-ddTHH:mm:ssZ.
updated_until = '2013-10-20T19:20:30+01:00' # datetime | Returns reservations changed until this timestamp as determined by the updatedAt field (updatedAt < updatedUntil). Datetime should be a UTC time and formatted as yyyy-MM-ddTHH:mm:ssZ.
status = 'status_example' # str | The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.  (optional)
offset = 0 # int | The starting point of the returned results. For example, if you have a collection of 300 reservations matching the specified query and you specify limit=100, you can retrieve the entire set of results in 3 successive requests by varying the offset value: offset=0, offset=100, and offset=200.  (optional) (default to 0)
limit = 100 # int | The maximum number of records that should be returned.  (optional) (default to 100)

try:
    # Search Reservations
    api_response = api_instance.get_reservations(locale, updated_since, updated_until, status=status, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->get_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **updated_since** | **datetime**| Returns reservations changed since this timestamp as determined by the updatedAt field (updatedAt &gt;&#x3D; updatedSince). Datetime should be a UTC time and formatted as yyyy-MM-ddTHH:mm:ssZ.  |
 **updated_until** | **datetime**| Returns reservations changed until this timestamp as determined by the updatedAt field (updatedAt &lt; updatedUntil). Datetime should be a UTC time and formatted as yyyy-MM-ddTHH:mm:ssZ.  |
 **status** | **str**| The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.  | [optional]
 **offset** | **int**| The starting point of the returned results. For example, if you have a collection of 300 reservations matching the specified query and you specify limit&#x3D;100, you can retrieve the entire set of results in 3 successive requests by varying the offset value: offset&#x3D;0, offset&#x3D;100, and offset&#x3D;200.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of records that should be returned.  | [optional] [default to 100]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations_id_v2**
> InlineResponse20010 get_reservations_id_v2(locale, reservation_id)

Retrieve Reservation

This endpoint is used to retrieve an existing reservation created through a [reserve call](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post) from the Partner.  ## Expected SLA TP99 50ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request  Note: The response body is the same as the [Reserve endpoint](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post).

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.

try:
    # Retrieve Reservation
    api_response = api_instance.get_reservations_id_v2(locale, reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->get_reservations_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_availability**
> get_system_availability()

Heartbeat

This endpoint is a simple health check endpoint for Groupon to monitor system availability. It will be fired periodically by Groupon outside of any purchase transactions to test for any connectivity or availability issues.  ## Expected SLA TP99 10ms at 10krpm  This is just the server response time, and does not include network transit time.  No response body is expected, as HTTP response codes will dictate whether the partner system is considered available or not. In the future, a response body may be added to support passing debug information

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()

try:
    # Heartbeat
    api_instance.get_system_availability()
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->get_system_availability: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_products_availability_v2**
> InlineResponse2005 post_products_availability_v2(body, locale, purchaser_id=purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)

Check Availability

This endpoint is used to determine availability and pricing for a specific product and attribute combination. The availability should be based off of real-time sources.  Optionally, the partner may choose to implement a temporary hold on inventory and return those reserved units in the response. For an iframe integration, the returned reservation ID (called a pre-reservation ID in this call) will be passed as a URL parameter.  A partner which is implementing only iframe transactions will not need to implement this call. However, even if a partner has “unlimited” inventory this endpoint should still be implemented. The reason is that the partner should return a `PRODUCT_NOT_AVAILABLE` error if the product is no longer offered for purchase.  ## Expected SLA TP99 35ms at 10k rpm  This is just the server response time, and does not include network transit time.  ## Request This request is specified as using POST for practical reasons as the full set of inputs may exceed static buffer space for query string size in common server stacks; however, the request should not create data, and the semantics should be the same as GET. The specific attributes supported will expand over time to fit the needs of a specific partner.

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
body = mobidy_groupon_api.ProductsAvailabilityBody1() # ProductsAvailabilityBody1 |
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
purchaser_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).  (optional)
prereservation_id = 'prereservation_id_example' # str | This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  (optional)
purchaser_email_hash = 'purchaser_email_hash_example' # str | The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  (optional)

try:
    # Check Availability
    api_response = api_instance.post_products_availability_v2(body, locale, purchaser_id=purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->post_products_availability_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAvailabilityBody1**](ProductsAvailabilityBody1.md)|  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **purchaser_id** | [**str**](.md)| An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).  | [optional]
 **prereservation_id** | **str**| This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  | [optional]
 **purchaser_email_hash** | **str**| The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations_id_cancellations_v2**
> InlineResponse20010 post_reservations_id_cancellations_v2(locale, reservation_id)

Cancel v2

This endpoint is to transition a reservation in the “reserved” or “fulfilled” state to the “cancelled” state. This indicates that the reservation is now void, and should not be fulfilled or redeemed for the consumer. A variety of circumstances could cause this, but the important distinction for a partner is that it should not allow fulfillment and/or redemption for the customer if at all possible. It is considered valid for this endpoint to be invoked on a reservation for any status; however, not all reservation are allowed to be cancelled (e.g. the reservation type does not allow cancels or the time window for cancellation has elapsed).  Please refer to the reservation lifecycle state machine for more details about possible state for a reservation.  The status of the reservation after this call should be “cancelling” or “cancelled”.   ## Expected SLA TP99 35ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request  While this request is a POST, there is no request body passed.  Note: The response body is the same as the [Reserve request](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post).

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.

try:
    # Cancel v2
    api_response = api_instance.post_reservations_id_cancellations_v2(locale, reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->post_reservations_id_cancellations_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations_id_fulfillments_v2**
> InlineResponse20010 post_reservations_id_fulfillments_v2(body, reservation_id, locale=locale)

Fulfill V2

This endpoint is to transition a reservation in the `reserved` state to the `fulfilled` state. This indicates that the payment has been captured by Groupon, and the reservation is now able to be fulfilled by the partner. The inventory should not be released to the user until it is fulfilled.  It is considered valid for this endpoint to be invoked on a `fulfilled` or `fulfilling` reservation, but not a `cancelled`, `cancelling`, or `reserving` reservation. Please refer to the reservation lifecycle state machine for more details about possible state for a reservation.  The status of the reservation after this call should be `fulfilling` or `fulfilled`. The status should be set to `fulfilling` until the inventory has been shipped (for shipping products) or an electronic form is available (for electronic fulfillmentType products). Once this occurs, the status can be changed to the final `fulfilled` status. The important aspect here is that the status should not be set to `fulfilled` unless the inventory has been guaranteed to be available for the purchaser.  ## Expected SLA TP99 35ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request  While this request is a POST, there is no request body passed. Please note that locale is not required to be passed in this call.  Note: The response body is the same as the [Reserve request](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post).

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
body = mobidy_groupon_api.ReservationIdFulfillmentsBody1() # ReservationIdFulfillmentsBody1 |
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  (optional)

try:
    # Fulfill V2
    api_response = api_instance.post_reservations_id_fulfillments_v2(body, reservation_id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->post_reservations_id_fulfillments_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReservationIdFulfillmentsBody1**](ReservationIdFulfillmentsBody1.md)|  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations_id_unit_cancellations**
> InlineResponse20012 post_reservations_id_unit_cancellations(body, locale, reservation_id)

Unit Cancel

This endpoint is used to support unit level cancellations, although the whole reservation can be cancelled if all of its units are cancelled. The following scenarios are possible:  1. Customer wants to cancel all the units of the reservation (Full reservation cancellation). This endpoint can be used, sending all    reservedUnits of the reservation. The `/groupon/v1/reservations/{reservationId}/cancellations` endpoint can also be used instead. 2. Customer wants to cancel a subset of the units in a reservation (Partial reservation cancellation), if reservation has more than one unit.    The request body will contain the units in reservedUnits field that the customer wants to cancel.  The state of the requested units should be transitioned to `cancelled`. This endpoint should behave in a transactional manner, that is, if any unit in the request can't be transitioned to `cancelled` the whole request should fail with error code `UNIT_NOT_CANCELLABLE`, and no state transition should happen to any of the units.  If all units of a reservation are in the `cancelled` state, then the state of the reservation should be `cancelled`. Note that unit states changes might happen on multiple API calls.  Please refer to the reservation lifecycle state machine and the unit lifecycle state machine for more details.  Note - If a partner only supports reservation level (full) cancellations, then there is no need to track unit state seperately, however this endpoint can still be implemented and only support full cancellations as described above.  ## Expected SLA TP99 35ms at 500rpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
body = mobidy_groupon_api.UnitsCancellationsBody() # UnitsCancellationsBody |
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.

try:
    # Unit Cancel
    api_response = api_instance.post_reservations_id_unit_cancellations(body, locale, reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->post_reservations_id_unit_cancellations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitsCancellationsBody**](UnitsCancellationsBody.md)|  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations_v2**
> InlineResponse2008 post_reservations_v2(body, locale, purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)

Reserve

This endpoint is used to put an indefinite hold on inventory. This can take the form of either a specific unit returned from the check availability call, or a general product. The reserved units should “belong” to the purchaser, and should not expire or be released unless cancel is explicitly called. The inventory should also not be released to the purchaser until it has been fulfilled.  In the case that a previously reserved unit (i.e. a temporary hold from the check availability call) is no longer available, this should be treated as any other availability failure.  The partner is able to verify the price Groupon is charging as it will be passed in the request. Groupon will also verify the price which the partner expected to be charged by comparing it to the price in the response. If Groupon detects an inconsistency, it may automatically cancel the order to avoid incorrectly charging the customer; however, it is recommended that the partner verify the price on the request and fail the request with the appropriate error code.  The status of the reservation after this call should be “reserved”.  ## Expected SLA TP99 80ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
body = mobidy_groupon_api.V2ReservationsBody() # V2ReservationsBody |
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
purchaser_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).
prereservation_id = 'prereservation_id_example' # str | This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  (optional)
purchaser_email_hash = 'purchaser_email_hash_example' # str | The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  (optional)

try:
    # Reserve
    api_response = api_instance.post_reservations_v2(body, locale, purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->post_reservations_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2ReservationsBody**](V2ReservationsBody.md)|  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **purchaser_id** | [**str**](.md)| An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).  |
 **prereservation_id** | **str**| This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  | [optional]
 **purchaser_email_hash** | **str**| The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reservations_id**
> InlineResponse2009 put_reservations_id(body, locale, reservation_id)

Update Reservation

This endpoint updates the reservation details of a reservation previously created through a reserve call. They payload is the same as the Reserve endpoint.  ## Expected SLA TP99 50ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request  Note: The request and response body is same of the [Reserve request](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post).

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.TransactionalPartnerEndpointsApi()
body = mobidy_groupon_api.ReservationsReservationIdBody() # ReservationsReservationIdBody |
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.

try:
    # Update Reservation
    api_response = api_instance.put_reservations_id(body, locale, reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalPartnerEndpointsApi->put_reservations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReservationsReservationIdBody**](ReservationsReservationIdBody.md)|  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

