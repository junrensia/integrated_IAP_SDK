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
from integrated_sdk.models.update_workflow_request import UpdateWorkflowRequest  # noqa: E501
from integrated_sdk.rest import ApiException

class TestUpdateWorkflowRequest(unittest.TestCase):
    """UpdateWorkflowRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateWorkflowRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = integrated_sdk.models.update_workflow_request.UpdateWorkflowRequest()  # noqa: E501
        if include_optional :
            return UpdateWorkflowRequest(
                name = '0', 
                description = '0', 
                organization = '0', 
                acl = [
                    '0'
                    ], 
                categories = [
                    '0'
                    ]
            )
        else :
            return UpdateWorkflowRequest(
        )

    def testUpdateWorkflowRequest(self):
        """Test UpdateWorkflowRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
