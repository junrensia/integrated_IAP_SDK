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
from ICA_SDK.models.sequencing_run_analysis_summary import SequencingRunAnalysisSummary  # noqa: E501
from ICA_SDK.rest import ApiException

class TestSequencingRunAnalysisSummary(unittest.TestCase):
    """SequencingRunAnalysisSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SequencingRunAnalysisSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.sequencing_run_analysis_summary.SequencingRunAnalysisSummary()  # noqa: E501
        if include_optional :
            return SequencingRunAnalysisSummary(
                definition_id = '0', 
                configuration_id = '0', 
                name = '0', 
                display_name = '0', 
                version = '0', 
                organization = '0', 
                type = '0'
            )
        else :
            return SequencingRunAnalysisSummary(
        )

    def testSequencingRunAnalysisSummary(self):
        """Test SequencingRunAnalysisSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
