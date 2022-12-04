# mobidy_groupon_api.IngestionFeedV2Api

All URIs are relative to *https://{your domain}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_availability_v2**](IngestionFeedV2Api.md#get_availability_v2) | **GET** /groupon/v2/feed/availability | Availability_v2

# **get_availability_v2**
> InlineResponse20017 get_availability_v2(product_ids, start_date, end_date, merchant_id=merchant_id, attribute_ids=attribute_ids)

Availability_v2

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.IngestionFeedV2Api()
product_ids = 'product_ids_example' # str | Comma delimited list of product IDs.
start_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time specifying the beginning of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).
end_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time specifying the end of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).
merchant_id = 'merchant_id_example' # str | The id of the merchant whose service availabilities should be provided.  (optional)
attribute_ids = 'attribute_ids_example' # str | Comma delimited list of attribute IDs that further refine the availability of the products. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.  (optional)

try:
    # Availability_v2
    api_response = api_instance.get_availability_v2(product_ids, start_date, end_date, merchant_id=merchant_id, attribute_ids=attribute_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IngestionFeedV2Api->get_availability_v2: %s\n" % e)
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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

