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
from illumina_iap_sdk.models.update_volume_configuration_request import UpdateVolumeConfigurationRequest  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestUpdateVolumeConfigurationRequest(unittest.TestCase):
    """UpdateVolumeConfigurationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateVolumeConfigurationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.update_volume_configuration_request.UpdateVolumeConfigurationRequest()  # noqa: E501
        if include_optional :
            return UpdateVolumeConfigurationRequest(
                name = '0', 
                object_store_settings = illumina_iap_sdk.models.object_store_settings.ObjectStoreSettings(
                    aws_s3 = illumina_iap_sdk.models.awss3_object_store_setting.AWSS3ObjectStoreSetting(
                        bucket_name = '012', 
                        key_prefix = 'gds-volumes/', ), 
                    platform_credentials_name = '0', )
            )
        else :
            return UpdateVolumeConfigurationRequest(
                name = '0',
                object_store_settings = illumina_iap_sdk.models.object_store_settings.ObjectStoreSettings(
                    aws_s3 = illumina_iap_sdk.models.awss3_object_store_setting.AWSS3ObjectStoreSetting(
                        bucket_name = '012', 
                        key_prefix = 'gds-volumes/', ), 
                    platform_credentials_name = '0', ),
        )

    def testUpdateVolumeConfigurationRequest(self):
        """Test UpdateVolumeConfigurationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
