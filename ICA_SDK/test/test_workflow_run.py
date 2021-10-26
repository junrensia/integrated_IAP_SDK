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

import ICA_SDK
from ICA_SDK.models.workflow_run import WorkflowRun  # noqa: E501
from ICA_SDK.rest import ApiException

class TestWorkflowRun(unittest.TestCase):
    """WorkflowRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowRun
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.workflow_run.WorkflowRun()  # noqa: E501
        if include_optional :
            return WorkflowRun(
                id = '0', 
                urn = '0', 
                href = '0', 
                name = '0', 
                time_started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_stopped = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = '0', 
                idempotency_key = '0', 
                status_summary = '0', 
                error = '0', 
                error_cause = '0', 
                workflow_version = ICA_SDK.models.workflow_version_compact.WorkflowVersionCompact(
                    id = '0', 
                    urn = '0', 
                    href = '0', 
                    version = '0', 
                    category = '0', 
                    description = '0', 
                    language = ICA_SDK.models.workflow_language.WorkflowLanguage(
                        name = '0', 
                        version = '0', ), 
                    status = '0', 
                    created_by_client_id = '0', 
                    time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = '0', 
                    modified_by = '0', 
                    tenant_id = '0', 
                    acl = [
                        '0'
                        ], ), 
                created_by_client_id = '0', 
                input = None, 
                output = None, 
                definition = '0', 
                engine_parameters = '0', 
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
            return WorkflowRun(
        )

    def testWorkflowRun(self):
        """Test WorkflowRun"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
