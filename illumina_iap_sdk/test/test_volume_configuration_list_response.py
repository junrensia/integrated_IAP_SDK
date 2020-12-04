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
from illumina_iap_sdk.models.volume_configuration_list_response import VolumeConfigurationListResponse  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestVolumeConfigurationListResponse(unittest.TestCase):
    """VolumeConfigurationListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VolumeConfigurationListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.volume_configuration_list_response.VolumeConfigurationListResponse()  # noqa: E501
        if include_optional :
            return VolumeConfigurationListResponse(
                items = [
                    illumina_iap_sdk.models.volume_configuration_response.VolumeConfigurationResponse(
                        name = '0', 
                        tenant_id = '0', 
                        sub_tenant_id = '0', 
                        urn = '0', 
                        online_status = 'Initializing', 
                        error_code = '0', 
                        error_message = '0', 
                        time_of_last_error = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = '0', 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_by = '0', 
                        object_store_settings = illumina_iap_sdk.models.object_store_settings.ObjectStoreSettings(
                            aws_s3 = illumina_iap_sdk.models.awss3_object_store_setting.AWSS3ObjectStoreSetting(
                                bucket_name = '012', 
                                key_prefix = 'gds-volumes/', ), 
                            platform_credentials_name = '0', ), )
                    ], 
                item_count = 56, 
                first_page_token = '0', 
                next_page_token = '0', 
                prev_page_token = '0', 
                last_page_token = '0', 
                total_item_count = 56, 
                total_page_count = 56
            )
        else :
            return VolumeConfigurationListResponse(
        )

    def testVolumeConfigurationListResponse(self):
        """Test VolumeConfigurationListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
