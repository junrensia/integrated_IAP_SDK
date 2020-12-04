# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import integrated_sdk
from integrated_sdk.models.workflow_connection import WorkflowConnection  # noqa: E501
from integrated_sdk.rest import ApiException

class TestWorkflowConnection(unittest.TestCase):
    """WorkflowConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowConnection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = integrated_sdk.models.workflow_connection.WorkflowConnection()  # noqa: E501
        if include_optional :
            return WorkflowConnection(
                name = '0', 
                type = '0', 
                host = 'https://api.myhost.com/v1/', 
                host_validation_regex = '0', 
                credentials = '0', 
                options = '0', 
                auto_disable_url = '0', 
                auto_disable_http_method = '0'
            )
        else :
            return WorkflowConnection(
                name = '0',
        )

    def testWorkflowConnection(self):
        """Test WorkflowConnection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
