# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ICA_SDK
from ICA_SDK.api.samples_api import SamplesApi  # noqa: E501
from ICA_SDK.rest import ApiException


class TestSamplesApi(unittest.TestCase):
    """SamplesApi unit test stubs"""

    def setUp(self):
        self.api = ICA_SDK.api.samples_api.SamplesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sample(self):
        """Test case for create_sample

        Create a sample.  # noqa: E501
        """
        pass

    def test_deliver_samples(self):
        """Test case for deliver_samples

        Deliver samples.  # noqa: E501
        """
        pass

    def test_get_sample(self):
        """Test case for get_sample

        Get sample details.  # noqa: E501
        """
        pass

    def test_list_sample_analysis_datasets(self):
        """Test case for list_sample_analysis_datasets

        List analysis datasets associated with the specified sample.  # noqa: E501
        """
        pass

    def test_list_samples(self):
        """Test case for list_samples

        Get a list of samples.  # noqa: E501
        """
        pass

    def test_merge_sample_acl(self):
        """Test case for merge_sample_acl

        Merge the access control list of a sample with the input access control list.  # noqa: E501
        """
        pass

    def test_register_sample_data(self):
        """Test case for register_sample_data

        Register data for a sample.  # noqa: E501
        """
        pass

    def test_remove_sample_acl(self):
        """Test case for remove_sample_acl

        Remove the access control list of a sample.  # noqa: E501
        """
        pass

    def test_replace_sample_acl(self):
        """Test case for replace_sample_acl

        Replace the access control list of a sample with the input access control list.  # noqa: E501
        """
        pass

    def test_update_sample(self):
        """Test case for update_sample

        Update sample information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
