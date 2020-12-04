# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import illumina_iap_sdk
from illumina_iap_sdk.api.workflow_runs_api import WorkflowRunsApi  # noqa: E501
from illumina_iap_sdk.rest import ApiException


class TestWorkflowRunsApi(unittest.TestCase):
    """WorkflowRunsApi unit test stubs"""

    def setUp(self):
        self.api = illumina_iap_sdk.api.workflow_runs_api.WorkflowRunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_workflow_run(self):
        """Test case for abort_workflow_run

        Abort a workflow run  # noqa: E501
        """
        pass

    def test_get_workflow_run(self):
        """Test case for get_workflow_run

        Get the details of a workflow run  # noqa: E501
        """
        pass

    def test_list_workflow_run_history(self):
        """Test case for list_workflow_run_history

        Get a list of workflow run history events  # noqa: E501
        """
        pass

    def test_list_workflow_runs(self):
        """Test case for list_workflow_runs

        Get a list of workflow runs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
