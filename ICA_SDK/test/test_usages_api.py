"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import ICA_SDK
from ICA_SDK.api.usages_api import UsagesApi  # noqa: E501


class TestUsagesApi(unittest.TestCase):
    """UsagesApi unit test stubs"""

    def setUp(self):
        self.api = UsagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_usage(self):
        """Test case for get_usage

        Get current tenant's usage detail by period.  Default returns current period usage data.   # noqa: E501
        """
        pass

    def test_get_usage_details(self):
        """Test case for get_usage_details

        Get current tenant's usage detail by period.  Default returns current period usage data.   # noqa: E501
        """
        pass

    def test_get_usage_periods(self):
        """Test case for get_usage_periods

        Get periods detail info   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
