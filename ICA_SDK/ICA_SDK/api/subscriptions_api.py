# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ICA_SDK.api_client import ApiClient
from ICA_SDK.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SubscriptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_subscription(self, **kwargs):  # noqa: E501
        """Creates a subscription to an event type and defines how those events get delivered.  # noqa: E501

        Events can be delivered to AWS SQS, AWS SNS, or can be used to launch a WES workflow.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_subscription(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateSubscriptionRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_subscription_with_http_info(**kwargs)  # noqa: E501

    def create_subscription_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a subscription to an event type and defines how those events get delivered.  # noqa: E501

        Events can be delivered to AWS SQS, AWS SNS, or can be used to launch a WES workflow.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_subscription_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateSubscriptionRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Subscription, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscription" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/subscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def disable_subscription(self, subscription_id, **kwargs):  # noqa: E501
        """Given a subscription id, disables the specified subscription.  # noqa: E501

        Given a subscription id, disables that subscription with the current JWT tokenâ€™s tenant Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_subscription(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str subscription_id: Id of the subscription to be disabled (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.disable_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501

    def disable_subscription_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Given a subscription id, disables the specified subscription.  # noqa: E501

        Given a subscription id, disables that subscription with the current JWT tokenâ€™s tenant Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_subscription_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str subscription_id: Id of the subscription to be disabled (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Subscription, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'subscription_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_subscription" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscription_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscription_id` when calling `disable_subscription`")  # noqa: E501

        if self.api_client.client_side_validation and ('subscription_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['subscription_id']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `subscription_id` when calling `disable_subscription`, length must be less than or equal to `255`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscriptionId'] = local_var_params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/subscriptions/{subscriptionId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscription(self, subscription_id, **kwargs):  # noqa: E501
        """Given a subscription id, returns information about that subscription.  # noqa: E501

        Given a subscription id, returns information about that subscription accessible by the current JWT tokenâ€™s tenant Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscription(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str subscription_id: Id of the subscription to return (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501

    def get_subscription_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Given a subscription id, returns information about that subscription.  # noqa: E501

        Given a subscription id, returns information about that subscription accessible by the current JWT tokenâ€™s tenant Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscription_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str subscription_id: Id of the subscription to return (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Subscription, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'subscription_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and ('subscription_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscription_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscription_id` when calling `get_subscription`")  # noqa: E501

        if self.api_client.client_side_validation and ('subscription_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['subscription_id']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `subscription_id` when calling `get_subscription`, length must be less than or equal to `255`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscriptionId'] = local_var_params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/subscriptions/{subscriptionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_subscriptions(self, **kwargs):  # noqa: E501
        """Get a list of subscriptions.  # noqa: E501

        Get a list of subscriptions accessible by the current JWT tokenâ€™s tenant Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_type: Optional event type for filtering returned subscriptions
        :param int page_size: Optional parameter to define the page size returned. Valid inputs range from 1-1000.
        :param str page_token: Utilized for navigation after initial listing. Valid values include those of  firstPageToken, nextPageToken, and previousPageToken in the list response.  When there are no more pages, the nextPageToken will be null.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SubscriptionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_subscriptions_with_http_info(**kwargs)  # noqa: E501

    def list_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of subscriptions.  # noqa: E501

        Get a list of subscriptions accessible by the current JWT tokenâ€™s tenant Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_type: Optional event type for filtering returned subscriptions
        :param int page_size: Optional parameter to define the page size returned. Valid inputs range from 1-1000.
        :param str page_token: Utilized for navigation after initial listing. Valid values include those of  firstPageToken, nextPageToken, and previousPageToken in the list response.  When there are no more pages, the nextPageToken will be null.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SubscriptionList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'event_type',
            'page_size',
            'page_token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_subscriptions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('event_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['event_type']) > 255):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `event_type` when calling `list_subscriptions`, length must be less than or equal to `255`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_subscriptions`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_subscriptions`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'event_type' in local_var_params and local_var_params['event_type'] is not None:  # noqa: E501
            query_params.append(('eventType', local_var_params['event_type']))  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'page_token' in local_var_params and local_var_params['page_token'] is not None:  # noqa: E501
            query_params.append(('pageToken', local_var_params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
