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
from illumina_iap_sdk.models.create_volume_response import CreateVolumeResponse  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestCreateVolumeResponse(unittest.TestCase):
    """CreateVolumeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateVolumeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.create_volume_response.CreateVolumeResponse()  # noqa: E501
        if include_optional :
            return CreateVolumeResponse(
                id = '0', 
                name = '0', 
                tenant_id = '0', 
                sub_tenant_id = '0', 
                urn = '0', 
                root_folder_id = '0', 
                root_key_prefix = '0', 
                volume_configuration_name = '0', 
                inherited_acl = [
                    '0'
                    ], 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by = '0', 
                job_status = 'None', 
                metadata = None, 
                import_session_id = '0', 
                object_store_access = illumina_iap_sdk.models.object_store_access.ObjectStoreAccess(
                    session_id = '0', 
                    aws_s3_temporary_upload_credentials = illumina_iap_sdk.models.aws_s3_temporary_upload_credentials.AwsS3TemporaryUploadCredentials(
                        access_key_id = '0', 
                        secret_access_key = '0', 
                        session_token = '0', 
                        region = '0', 
                        bucket_name = '0', 
                        key_prefix = '0', 
                        expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_url = '0', ), )
            )
        else :
            return CreateVolumeResponse(
        )

    def testCreateVolumeResponse(self):
        """Test CreateVolumeResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
