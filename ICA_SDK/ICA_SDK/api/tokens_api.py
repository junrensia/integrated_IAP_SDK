"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ICA_SDK.api_client import ApiClient, Endpoint as _Endpoint
from ICA_SDK.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ICA_SDK.model.access_token_request import AccessTokenRequest
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.token_detail_response import TokenDetailResponse
from ICA_SDK.model.token_response import TokenResponse


class TokensApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_token(
            self,
            **kwargs
        ):
            """Creates a JWT token to call IAP services.  # noqa: E501

            This endpoint creates a JWT token to call IAP services. Authorization can be a Bearer psToken,  Basic Base64 encoded username:password or Basic with apiKey.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_token(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                x_api_key (str): Api Key can be passed in header to generate a JWT.. [optional]
                client_id (str): Optionally pass client Id from calling app to set as authorized party on JWT.. [optional]
                api_key (str): OBSOLETE: api key should now be passed as as an X-API-Key header.. [optional]
                domain (str): Optionally pass the domain name you are logging into. [optional]
                data (str): Data is a custom meta data field that will be applied to the session field in the JWT payload.. [optional]
                scopes ([str]): Scopes can be passed in during token generation to limit the token to particular scopes.. [optional]
                cwid (str): Set the current workgroup on the token. Used for aligning resources to a workgroup.. [optional]
                cid (str): Set the current context on the token. Used for aligning resources to a context.. [optional]
                return_session_token (bool): By default, this endpoint returns a JWT token. You can specify returnSessionToken=true to get an Illumina psToken instead.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TokenResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.create_token = _Endpoint(
            settings={
                'response_type': (TokenResponse,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/tokens',
                'operation_id': 'create_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_api_key',
                    'client_id',
                    'api_key',
                    'domain',
                    'data',
                    'scopes',
                    'cwid',
                    'cid',
                    'return_session_token',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_api_key':
                        (str,),
                    'client_id':
                        (str,),
                    'api_key':
                        (str,),
                    'domain':
                        (str,),
                    'data':
                        (str,),
                    'scopes':
                        ([str],),
                    'cwid':
                        (str,),
                    'cid':
                        (str,),
                    'return_session_token':
                        (bool,),
                },
                'attribute_map': {
                    'x_api_key': 'X-API-Key',
                    'client_id': 'clientId',
                    'api_key': 'api_key',
                    'domain': 'domain',
                    'data': 'data',
                    'scopes': 'scopes',
                    'cwid': 'cwid',
                    'cid': 'cid',
                    'return_session_token': 'returnSessionToken',
                },
                'location_map': {
                    'x_api_key': 'header',
                    'client_id': 'query',
                    'api_key': 'query',
                    'domain': 'query',
                    'data': 'query',
                    'scopes': 'query',
                    'cwid': 'query',
                    'cid': 'query',
                    'return_session_token': 'query',
                },
                'collection_format_map': {
                    'scopes': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__create_token
        )

        def __get_token_details(
            self,
            **kwargs
        ):
            """Get current tokens info require authorization Bearer token  # noqa: E501

            Get token details  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_token_details(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TokenDetailResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_token_details = _Endpoint(
            settings={
                'response_type': (TokenDetailResponse,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/tokens/details',
                'operation_id': 'get_token_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_token_details
        )

        def __refresh_token(
            self,
            **kwargs
        ):
            """Refresh session psToken.  # noqa: E501

            This endpoint extends the session for the psToken.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.refresh_token(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                body (AccessTokenRequest): Access token request accepts a psToken in the access_token field in the body of the request.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TokenResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.refresh_token = _Endpoint(
            settings={
                'response_type': (TokenResponse,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/tokens:refresh',
                'operation_id': 'refresh_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (AccessTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__refresh_token
        )

        def __revoke_token(
            self,
            **kwargs
        ):
            """Revokes an access token.  # noqa: E501

            This endpoint revokes the access token that is passed in.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.revoke_token(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                body (AccessTokenRequest): Access token request accepts either a psToken or a JWT in the access_token field in the body of the request.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.revoke_token = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/tokens',
                'operation_id': 'revoke_token',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (AccessTokenRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__revoke_token
        )
