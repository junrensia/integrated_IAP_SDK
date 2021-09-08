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
from ICA_SDK.model.error_response import ErrorResponse
from ICA_SDK.model.sequencing_analysis_run import SequencingAnalysisRun
from ICA_SDK.model.sequencing_analysis_run_compact_sequencing_analysis_run_sort_fields_paged_items import SequencingAnalysisRunCompactSequencingAnalysisRunSortFieldsPagedItems


class SequencingAnalysisRunsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_sequencing_analysis_run(
            self,
            analysis_run_id,
            **kwargs
        ):
            """Get SequencingAnalysisRun details.  # noqa: E501

            For a given ID, return information about that SequencingAnalysisRun.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_sequencing_analysis_run(analysis_run_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_run_id (str): ID of the analysis run

            Keyword Args:
                include ([str]): Include flags to specify what is included in the response. [optional]
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
                SequencingAnalysisRun
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
            kwargs['analysis_run_id'] = \
                analysis_run_id
            return self.call_with_http_info(**kwargs)

        self.get_sequencing_analysis_run = _Endpoint(
            settings={
                'response_type': (SequencingAnalysisRun,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisRuns/{analysisRunId}',
                'operation_id': 'get_sequencing_analysis_run',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_run_id',
                    'include',
                ],
                'required': [
                    'analysis_run_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'include',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('include',): {

                        "INCLUDEANALYSISDATASETS": "IncludeAnalysisDatasets"
                    },
                },
                'openapi_types': {
                    'analysis_run_id':
                        (str,),
                    'include':
                        ([str],),
                },
                'attribute_map': {
                    'analysis_run_id': 'analysisRunId',
                    'include': 'include',
                },
                'location_map': {
                    'analysis_run_id': 'path',
                    'include': 'query',
                },
                'collection_format_map': {
                    'include': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_sequencing_analysis_run
        )

        def __list_sequencing_analysis_runs(
            self,
            **kwargs
        ):
            """Get a list of analysis runs.  # noqa: E501

            Get a list of analysis runs accessible by the request token.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_sequencing_analysis_runs(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                include ([str]): Include flags to specify what is included in the response. [optional]
                status ([str]): Optional parameter. Set to filter the analysis run list and only include analysis runs with the specified status.. [optional]
                sequencing_run_id ([str]): Optional parameter. Set to filter the analysis run and only include analysis runs associated with the specific sequencing runs. [optional]
                tenant_ids ([str]): Optional parameter to limit the response to be with in provided tenant ids  Comma separated to support multiple tenant ids. [optional]
                page_size (int): Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified.. [optional] if omitted the server will use the default value of 10
                page_token (str): Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified.. [optional]
                sort (str): Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending).. [optional] if omitted the server will use the default value of "timeCreated asc"
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
                SequencingAnalysisRunCompactSequencingAnalysisRunSortFieldsPagedItems
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

        self.list_sequencing_analysis_runs = _Endpoint(
            settings={
                'response_type': (SequencingAnalysisRunCompactSequencingAnalysisRunSortFieldsPagedItems,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisRuns',
                'operation_id': 'list_sequencing_analysis_runs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'include',
                    'status',
                    'sequencing_run_id',
                    'tenant_ids',
                    'page_size',
                    'page_token',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'include',
                    'status',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('include',): {

                        "TOTALITEMCOUNT": "TotalItemCount",
                        "SEQUENCINGRUN": "SequencingRun"
                    },
                    ('status',): {

                        "ABORTED": "Aborted",
                        "ABORTING": "Aborting",
                        "FAILED": "Failed",
                        "LAUNCHED": "Launched",
                        "LAUNCHING": "Launching",
                        "NEW": "New",
                        "READYTOLAUNCH": "ReadyToLaunch",
                        "RUNNING": "Running",
                        "STARTING": "Starting",
                        "SUCCEEDED": "Succeeded",
                        "TIMEDOUT": "TimedOut"
                    },
                },
                'openapi_types': {
                    'include':
                        ([str],),
                    'status':
                        ([str],),
                    'sequencing_run_id':
                        ([str],),
                    'tenant_ids':
                        ([str],),
                    'page_size':
                        (int,),
                    'page_token':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'include': 'include',
                    'status': 'status',
                    'sequencing_run_id': 'sequencingRunId',
                    'tenant_ids': 'tenantIds',
                    'page_size': 'pageSize',
                    'page_token': 'pageToken',
                    'sort': 'sort',
                },
                'location_map': {
                    'include': 'query',
                    'status': 'query',
                    'sequencing_run_id': 'query',
                    'tenant_ids': 'query',
                    'page_size': 'query',
                    'page_token': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                    'include': 'csv',
                    'status': 'csv',
                    'sequencing_run_id': 'csv',
                    'tenant_ids': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_sequencing_analysis_runs
        )

        def __sync_sequencing_analysis_run(
            self,
            analysis_run_id,
            **kwargs
        ):
            """Sync A SequencingAnalysisRun.  # noqa: E501

            For a given ID, sync the SequencingAnalysisRun.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.sync_sequencing_analysis_run(analysis_run_id, async_req=True)
            >>> result = thread.get()

            Args:
                analysis_run_id (str):

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
                SequencingAnalysisRun
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
            kwargs['analysis_run_id'] = \
                analysis_run_id
            return self.call_with_http_info(**kwargs)

        self.sync_sequencing_analysis_run = _Endpoint(
            settings={
                'response_type': (SequencingAnalysisRun,),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/v1/sequencing/analysisRuns/{analysisRunId}:sync',
                'operation_id': 'sync_sequencing_analysis_run',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'analysis_run_id',
                ],
                'required': [
                    'analysis_run_id',
                ],
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
                    'analysis_run_id':
                        (str,),
                },
                'attribute_map': {
                    'analysis_run_id': 'analysisRunId',
                },
                'location_map': {
                    'analysis_run_id': 'path',
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
            callable=__sync_sequencing_analysis_run
        )
