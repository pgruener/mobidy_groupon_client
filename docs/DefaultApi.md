# mobidy_groupon_api.DefaultApi

All URIs are relative to *https://{your domain}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_availability**](DefaultApi.md#get_availability) | **GET** /groupon/v1/feed/availability | Availability
[**get_merchant_feed**](DefaultApi.md#get_merchant_feed) | **GET** /groupon/v1/feed/services/merchants | Content
[**get_reservations_id**](DefaultApi.md#get_reservations_id) | **GET** /groupon/v1/reservations/{reservationId} | Retrieve Reservation
[**get_service_availability**](DefaultApi.md#get_service_availability) | **GET** /groupon/v1/feed/services/availability | Booking Availability
[**post_booking_availability**](DefaultApi.md#post_booking_availability) | **POST** /groupon/v1/bookings/availability | Booking Availability Check
[**post_booking_cancellations**](DefaultApi.md#post_booking_cancellations) | **POST** /groupon/v1/bookings/cancellations | Booking Cancellation
[**post_booking_creation**](DefaultApi.md#post_booking_creation) | **POST** /groupon/v1/bookings | Create Booking
[**post_products_availability**](DefaultApi.md#post_products_availability) | **POST** /groupon/v1/products/availability | Availability Check
[**post_reservations**](DefaultApi.md#post_reservations) | **POST** /groupon/v1/reservations | Create Reservation
[**post_reservations_id_cancellations**](DefaultApi.md#post_reservations_id_cancellations) | **POST** /groupon/v1/reservations/{reservationId}/cancellations | Cancellation
[**post_reservations_id_fulfillments**](DefaultApi.md#post_reservations_id_fulfillments) | **POST** /groupon/v1/reservations/{reservationId}/fulfillments | Fulfillment
[**webhook_bookings**](DefaultApi.md#webhook_bookings) | **PATCH** /partners/{partner}/v1/bookings | Booking Status Update
[**webhook_reservations**](DefaultApi.md#webhook_reservations) | **PATCH** /partners/{partner}/v1/reservations | Status Update
[**webhook_units**](DefaultApi.md#webhook_units) | **PATCH** /partners/{partner}/v1/units | Redemption

# **get_availability**
> InlineResponse20016 get_availability(product_ids, start_date, end_date, merchant_id=merchant_id, attribute_ids=attribute_ids)

Availability

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
product_ids = 'product_ids_example' # str | Comma delimited list of product IDs.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time specifying the beginning of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time specifying the end of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).
merchant_id = 'merchant_id_example' # str | The id of the merchant whose service availabilities should be provided.  (optional)
attribute_ids = 'attribute_ids_example' # str | Comma delimited list of attribute IDs that further refine the availability of the products. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.  (optional)

try:
    # Availability
    api_response = api_instance.get_availability(product_ids, start_date, end_date, merchant_id=merchant_id, attribute_ids=attribute_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_ids** | **str**| Comma delimited list of product IDs.  |
 **start_date** | **datetime**| Date/time specifying the beginning of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  |
 **end_date** | **datetime**| Date/time specifying the end of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  |
 **merchant_id** | **str**| The id of the merchant whose service availabilities should be provided.  | [optional]
 **attribute_ids** | **str**| Comma delimited list of attribute IDs that further refine the availability of the products. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.  | [optional]

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_feed**
> InlineResponse20019 get_merchant_feed(ids)

Content

This endpoint is used to retrieve the list of products and services that the merchant provides so that Groupon can make calls to the availability endpoints with the appropriate parameters.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
ids = 'ids_example' # str | Comma delimited list of merchant ids in the partner’s system.

try:
    # Content
    api_response = api_instance.get_merchant_feed(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_merchant_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma delimited list of merchant ids in the partner’s system.  |

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservations_id**
> InlineResponse2009 get_reservations_id(locale, reservation_id)

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
api_instance = mobidy_groupon_api.DefaultApi()
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.

try:
    # Retrieve Reservation
    api_response = api_instance.get_reservations_id(locale, reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_reservations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_availability**
> InlineResponse20018 get_service_availability(service_ids, start_date, end_date, merchant_id, attribute_ids=attribute_ids)

Booking Availability

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
service_ids = 'service_ids_example' # str | Comma delimited list of service IDs.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time specifying the beginning of the period for which segments should be provided. The results should all include availableAt date and times that are greater than or equal to this value. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time specifying the end of the period for which segments should be provided. The results should all include availableAt date and times that are less than or equal to this value. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).
merchant_id = 'merchant_id_example' # str | The id of the merchant whose service availabilities should be provided.
attribute_ids = 'attribute_ids_example' # str | Comma delimited list of attribute IDs that further refine the availability of the services. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.  (optional)

try:
    # Booking Availability
    api_response = api_instance.get_service_availability(service_ids, start_date, end_date, merchant_id, attribute_ids=attribute_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_ids** | **str**| Comma delimited list of service IDs.  |
 **start_date** | **datetime**| Date/time specifying the beginning of the period for which segments should be provided. The results should all include availableAt date and times that are greater than or equal to this value. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  |
 **end_date** | **datetime**| Date/time specifying the end of the period for which segments should be provided. The results should all include availableAt date and times that are less than or equal to this value. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  |
 **merchant_id** | **str**| The id of the merchant whose service availabilities should be provided.  |
 **attribute_ids** | **str**| Comma delimited list of attribute IDs that further refine the availability of the services. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.  | [optional]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_booking_availability**
> InlineResponse200 post_booking_availability(body)

Booking Availability Check

This endpoint is used to support an availability check before booking happens.  This endpoint to pull the availability in real time. This would be used as part of UX to update enabled options when a customer is making their selections and also when purchasing, to validate again that what they want to book is still available. The request would either be the raw segment Groupon got on the feed, or it might have the specific attributes that the customer selected (a subset of the attributeIds). If multiple attributes per group are used, the segments on the response might not match the request exactly if a specific attribute isn’t available anymore, main use case would be staff members. See an example.  ## Expected SLA TP99 35ms at 500rpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.BookingsAvailabilityBody() # BookingsAvailabilityBody |

try:
    # Booking Availability Check
    api_response = api_instance.post_booking_availability(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_booking_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BookingsAvailabilityBody**](BookingsAvailabilityBody.md)|  |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_booking_cancellations**
> InlineResponse2002 post_booking_cancellations(body)

Booking Cancellation

This endpoint is used to support booking level cancellation.  The state of the requested bookings should be transitioned to `cancelled`. This endpoint should behave in a transactional manner, that is, if any booking in the request can't be transitioned to `cancelled` the whole request should fail with error code `BOOKING_NOT_CANCELLABLE`,  and no state transition should happen to any of the bookings.  ## Expected SLA TP99 35ms at 500rpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.BookingsCancellationsBody() # BookingsCancellationsBody |

try:
    # Booking Cancellation
    api_response = api_instance.post_booking_cancellations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_booking_cancellations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BookingsCancellationsBody**](BookingsCancellationsBody.md)|  |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_booking_creation**
> InlineResponse2001 post_booking_creation(body)

Create Booking

This endpoint is used to support booking creation.  The status of the booking after this call should be `confirmed` or `hold`, depending on the `bookingType` value. This endpoint should behave in a transactional manner, that is, if any booking in the request can't be transitioned to `confirmed` the whole request should fail with error code `BOOKING_NOT_CREATED`, and no booking should be created.  This endpoint must be idempotent.  In case Groupon makes a second request with the same `grouponBookingId`, and the partner already created a booking in its system for this id, the previously created booking must be returned.  ## Expected SLA TP99 35ms at 500rpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.V1BookingsBody() # V1BookingsBody |

try:
    # Create Booking
    api_response = api_instance.post_booking_creation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_booking_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BookingsBody**](V1BookingsBody.md)|  |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_products_availability**
> InlineResponse2004 post_products_availability(body, locale, purchaser_id=purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)

Availability Check

This endpoint is used to determine availability and pricing for a specific product and attribute combination. The availability should be based off of real-time sources.  Optionally, the partner may choose to implement a temporary hold on inventory and return those reserved units in the response. For an iframe integration, the returned reservation ID (called a pre-reservation ID in this call) will be passed as a URL parameter.  A partner which is implementing only iframe transactions will not need to implement this call. However, even if a partner has “unlimited” inventory this endpoint should still be implemented. The reason is that the partner should return a `PRODUCT_NOT_AVAILABLE` error if the product is no longer offered for purchase.  ## Expected SLA TP99 35ms at 10k rpm  This is just the server response time, and does not include network transit time.  ## Request This request is specified as using POST for practical reasons as the full set of inputs may exceed static buffer space for query string size in common server stacks; however, the request should not create data, and the semantics should be the same as GET. The specific attributes supported will expand over time to fit the needs of a specific partner.

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.ProductsAvailabilityBody() # ProductsAvailabilityBody |
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
purchaser_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).  (optional)
prereservation_id = 'prereservation_id_example' # str | This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  (optional)
purchaser_email_hash = 'purchaser_email_hash_example' # str | The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  (optional)

try:
    # Availability Check
    api_response = api_instance.post_products_availability(body, locale, purchaser_id=purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_products_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsAvailabilityBody**](ProductsAvailabilityBody.md)|  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **purchaser_id** | [**str**](.md)| An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).  | [optional]
 **prereservation_id** | **str**| This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  | [optional]
 **purchaser_email_hash** | **str**| The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations**
> InlineResponse2007 post_reservations(body, locale, purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)

Create Reservation

This endpoint is used to put an indefinite hold on inventory. This can take the form of either a specific unit returned from the check availability call, or a general product. The reserved units should “belong” to the purchaser, and should not expire or be released unless cancel is explicitly called. The inventory should also not be released to the purchaser until it has been fulfilled.  In the case that a previously reserved unit (i.e. a temporary hold from the check availability call) is no longer available, this should be treated as any other availability failure.  The partner is able to verify the price Groupon is charging as it will be passed in the request. Groupon will also verify the price which the partner expected to be charged by comparing it to the price in the response. If Groupon detects an inconsistency, it may automatically cancel the order to avoid incorrectly charging the customer; however, it is recommended that the partner verify the price on the request and fail the request with the appropriate error code.  The status of the reservation after this call should be “reserved”.  ## Expected SLA TP99 80ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.V1ReservationsBody() # V1ReservationsBody |
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
purchaser_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).
prereservation_id = 'prereservation_id_example' # str | This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  (optional)
purchaser_email_hash = 'purchaser_email_hash_example' # str | The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  (optional)

try:
    # Create Reservation
    api_response = api_instance.post_reservations(body, locale, purchaser_id, prereservation_id=prereservation_id, purchaser_email_hash=purchaser_email_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ReservationsBody**](V1ReservationsBody.md)|  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **purchaser_id** | [**str**](.md)| An identifier representing the Groupon user purchasing this option. The format will be a UUID (canonical format).  |
 **prereservation_id** | **str**| This would be the data.reservationId attribute returned by the reservationPlaced event for an iframe integration or the meta.prereservationId field from a checkAvailability response.  | [optional]
 **purchaser_email_hash** | **str**| The email hash for the Groupon user purchasing this option. See the Purchaser Email Hash section for more details.  Since not all Groupon users have an associated email address, this field is not required.  | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations_id_cancellations**
> InlineResponse20012 post_reservations_id_cancellations(locale, reservation_id)

Cancellation

This endpoint is to transition a reservation in the “reserved” or “fulfilled” state to the “cancelled” state. This indicates that the reservation is now void, and should not be fulfilled or redeemed for the consumer. A variety of circumstances could cause this, but the important distinction for a partner is that it should not allow fulfillment and/or redemption for the customer if at all possible. It is considered valid for this endpoint to be invoked on a reservation for any status; however, not all reservation are allowed to be cancelled (e.g. the reservation type does not allow cancels or the time window for cancellation has elapsed).  Please refer to the reservation lifecycle state machine for more details about possible state for a reservation.  The status of the reservation after this call should be “cancelling” or “cancelled”.   ## Expected SLA TP99 35ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request  While this request is a POST, there is no request body passed.  Note: The response body is the same as the [Reserve request](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post).

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.

try:
    # Cancellation
    api_response = api_instance.post_reservations_id_cancellations(locale, reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_reservations_id_cancellations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reservations_id_fulfillments**
> InlineResponse20011 post_reservations_id_fulfillments(body, reservation_id, locale=locale)

Fulfillment

This endpoint is to transition a reservation in the `reserved` state to the `fulfilled` state. This indicates that the payment has been captured by Groupon, and the reservation is now able to be fulfilled by the partner. The inventory should not be released to the user until it is fulfilled.  It is considered valid for this endpoint to be invoked on a `fulfilled` or `fulfilling` reservation, but not a `cancelled`, `cancelling`, or `reserving` reservation. Please refer to the reservation lifecycle state machine for more details about possible state for a reservation.  The status of the reservation after this call should be `fulfilling` or `fulfilled`. The status should be set to `fulfilling` until the inventory has been shipped (for shipping products) or an electronic form is available (for electronic fulfillmentType products). Once this occurs, the status can be changed to the final `fulfilled` status. The important aspect here is that the status should not be set to `fulfilled` unless the inventory has been guaranteed to be available for the purchaser.  ## Expected SLA TP99 35ms at 10krpm  This is just the server response time, and does not include network transit time.  ## Request  While this request is a POST, there is no request body passed. Please note that locale is not required to be passed in this call.  Note: The response body is the same as the [Reserve request](#tag/Endpoint-Definitions/paths/~1groupon~1v1~1reservations/post).

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.ReservationIdFulfillmentsBody() # ReservationIdFulfillmentsBody |
reservation_id = 'reservation_id_example' # str | The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.
locale = 'locale_example' # str | The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  (optional)

try:
    # Fulfillment
    api_response = api_instance.post_reservations_id_fulfillments(body, reservation_id, locale=locale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_reservations_id_fulfillments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReservationIdFulfillmentsBody**](ReservationIdFulfillmentsBody.md)|  |
 **reservation_id** | **str**| The partner id for the reservation being retrieved. This id is for the reservation in the partner’s system.  |
 **locale** | **str**| The locale and country code which represents the language for the content.  This should use the ISO-3166-1 and UN M.49 variation of the [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag#ISO_3166-1_and_UN_M.49).  | [optional]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_bookings**
> InlineResponse2003 webhook_bookings(body, client_id, partner)

Booking Status Update

This endpoint can be used by partners to notify Groupon of bookings status updates (e.g., when a booking is cancelled on partner side).  ## SLA TP99 100ms at 10k rpm.  ## Request The request body should include a list of bookings to update.  Each entry of the list specifies the partner-generated booking id, the update of the booking (`cancelled`, `check-in`, `no-show`), and a datetime representing when the booking was last updated.

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.V1BookingsBody1() # V1BookingsBody1 |
client_id = 'client_id_example' # str | A client id required to make the request.  This id will be provided to partners by Groupon.
partner = 'partner_example' # str | The partner name.

try:
    # Booking Status Update
    api_response = api_instance.webhook_bookings(body, client_id, partner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->webhook_bookings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BookingsBody1**](V1BookingsBody1.md)|  |
 **client_id** | **str**| A client id required to make the request.  This id will be provided to partners by Groupon.  |
 **partner** | **str**| The partner name.  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_reservations**
> InlineResponse20013 webhook_reservations(body, client_id, partner)

Status Update

This endpoint can be used by partners to notify Groupon of reservation status updates, when a reservation is fulfilled or cancelled on partner side.  ## SLA TP99 100ms at 10k rpm.  ## Request The request body should include a list of reservation to update.  Each entry of the list specifies the partner-generated reservation id, the new status of the reservation (`fulfilled` or `cancelled`), and a datetime representing when the reservation was last updated.

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.V1ReservationsBody1() # V1ReservationsBody1 |
client_id = 'client_id_example' # str | A client id required to make the request.  This id will be provided to partners by Groupon.
partner = 'partner_example' # str | The partner name.

try:
    # Status Update
    api_response = api_instance.webhook_reservations(body, client_id, partner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->webhook_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ReservationsBody1**](V1ReservationsBody1.md)|  |
 **client_id** | **str**| A client id required to make the request.  This id will be provided to partners by Groupon.  |
 **partner** | **str**| The partner name.  |

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_units**
> InlineResponse20014 webhook_units(body, client_id, partner)

Redemption

This endpoint can be used by partners to notify Groupon of units status updates, when a unit is redeemed or cancelled on partner side.  ## SLA TP99 100ms at 10k rpm.  ## Request The request body should include a list of units to update.  Each entry of the list specifies the partner-generated unit id, the new status of the unit (`redeemed` or `cancelled`), and a datetime representing when the reservation containing the unit was last updated.

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.DefaultApi()
body = mobidy_groupon_api.V1UnitsBody() # V1UnitsBody |
client_id = 'client_id_example' # str | A client id required to make the request.  This id will be provided to partners by Groupon.
partner = 'partner_example' # str | The partner name.

try:
    # Redemption
    api_response = api_instance.webhook_units(body, client_id, partner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->webhook_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UnitsBody**](V1UnitsBody.md)|  |
 **client_id** | **str**| A client id required to make the request.  This id will be provided to partners by Groupon.  |
 **partner** | **str**| The partner name.  |

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

