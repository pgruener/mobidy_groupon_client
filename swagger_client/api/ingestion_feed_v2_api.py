# coding: utf-8

"""
    Groupon Connect APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: 3pip@groupon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mobidy_groupon_api.api_client import ApiClient


class IngestionFeedV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_availability_v2(self, product_ids, start_date, end_date, **kwargs):  # noqa: E501
        """Availability_v2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_v2(product_ids, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_ids: Comma delimited list of product IDs.  (required)
        :param datetime start_date: Date/time specifying the beginning of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  (required)
        :param datetime end_date: Date/time specifying the end of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  (required)
        :param str merchant_id: The id of the merchant whose service availabilities should be provided.
        :param str attribute_ids: Comma delimited list of attribute IDs that further refine the availability of the products. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_availability_v2_with_http_info(product_ids, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_availability_v2_with_http_info(product_ids, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def get_availability_v2_with_http_info(self, product_ids, start_date, end_date, **kwargs):  # noqa: E501
        """Availability_v2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_availability_v2_with_http_info(product_ids, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_ids: Comma delimited list of product IDs.  (required)
        :param datetime start_date: Date/time specifying the beginning of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  (required)
        :param datetime end_date: Date/time specifying the end of the period for which segments should be provided. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).  (required)
        :param str merchant_id: The id of the merchant whose service availabilities should be provided.
        :param str attribute_ids: Comma delimited list of attribute IDs that further refine the availability of the products. This list should be considered an OR for related attributes. If no attribute is passed then that is considered as if all attributes are possible for availability.
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_ids', 'start_date', 'end_date', 'merchant_id', 'attribute_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_availability_v2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_ids' is set
        if ('product_ids' not in params or
                params['product_ids'] is None):
            raise ValueError("Missing the required parameter `product_ids` when calling `get_availability_v2`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_availability_v2`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_availability_v2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_ids' in params:
            query_params.append(('productIds', params['product_ids']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'merchant_id' in params:
            query_params.append(('merchantId', params['merchant_id']))  # noqa: E501
        if 'attribute_ids' in params:
            query_params.append(('attributeIds', params['attribute_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/groupon/v2/feed/availability', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)