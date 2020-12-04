# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import illumina_iap_sdk
from illumina_iap_sdk.models.workflow import Workflow  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestWorkflow(unittest.TestCase):
    """Workflow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Workflow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.workflow.Workflow()  # noqa: E501
        if include_optional :
            return Workflow(
                id = '0', 
                urn = '0', 
                href = '0', 
                name = '0', 
                organization = '0', 
                description = '0', 
                tool_class = '0', 
                categories = [
                    '0'
                    ], 
                created_by_client_id = '0', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                modified_by = '0', 
                tenant_id = '0', 
                acl = [
                    '0'
                    ]
            )
        else :
            return Workflow(
        )

    def testWorkflow(self):
        """Test Workflow"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
