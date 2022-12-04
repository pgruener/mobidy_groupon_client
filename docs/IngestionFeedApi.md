# mobidy_groupon_api.IngestionFeedApi

All URIs are relative to *https://{your domain}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feed**](IngestionFeedApi.md#get_feed) | **GET** /groupon/v1/feed | Feed

# **get_feed**
> InlineResponse20015 get_feed()

Feed

### Example
```python
from __future__ import print_function
import time
import mobidy_groupon_api
from mobidy_groupon_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mobidy_groupon_api.IngestionFeedApi()

try:
    # Feed
    api_response = api_instance.get_feed()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IngestionFeedApi->get_feed: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

