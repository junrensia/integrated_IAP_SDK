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
from illumina_iap_sdk.models.session_status import SessionStatus  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestSessionStatus(unittest.TestCase):
    """SessionStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SessionStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.session_status.SessionStatus()  # noqa: E501
        if include_optional :
            return SessionStatus(
            )
        else :
            return SessionStatus(
        )

    def testSessionStatus(self):
        """Test SessionStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
