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
from illumina_iap_sdk.models.create_task_run_request import CreateTaskRunRequest  # noqa: E501
from illumina_iap_sdk.rest import ApiException

class TestCreateTaskRunRequest(unittest.TestCase):
    """CreateTaskRunRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTaskRunRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = illumina_iap_sdk.models.create_task_run_request.CreateTaskRunRequest()  # noqa: E501
        if include_optional :
            return CreateTaskRunRequest(
                name = '0', 
                description = '0', 
                acl = [
                    '0'
                    ], 
                execution = illumina_iap_sdk.models.execution.Execution(
                    image = illumina_iap_sdk.models.image.Image(
                        name = '0', 
                        tag = '0', 
                        digest = '0', 
                        credentials = illumina_iap_sdk.models.credentials.Credentials(
                            username = '0', 
                            password = '0', ), ), 
                    command = '0', 
                    args = [
                        '0'
                        ], 
                    inputs = [
                        illumina_iap_sdk.models.input_mount_mapping_with_creds.InputMountMappingWithCreds(
                            storage_provider = '0', 
                            path = '0', 
                            url = '0', 
                            urn = '0', 
                            mode = '0', 
                            type = 'File', )
                        ], 
                    outputs = [
                        illumina_iap_sdk.models.mount_mapping_with_creds.MountMappingWithCreds(
                            path = '0', 
                            url = '0', 
                            urn = '0', 
                            type = '0', 
                            storage_provider = '0', )
                        ], 
                    system_files = illumina_iap_sdk.models.system_files.SystemFiles(
                        url = '0', 
                        urn = '0', 
                        storage_provider = '0', ), 
                    environment = illumina_iap_sdk.models.environment.Environment(
                        variables = {
                            'key' : '0'
                            }, 
                        resources = illumina_iap_sdk.models.resources.Resources(
                            type = '0', 
                            size = '0', 
                            cpu_cores = 1.337, 
                            memory_gb = 1.337, 
                            hardware = [
                                '0'
                                ], 
                            tier = '0', ), 
                        input_stream_settings = illumina_iap_sdk.models.input_stream_settings.InputStreamSettings(
                            access_pattern = 'sequential', 
                            cache_size_gb = 5E+1, 
                            block_size_mb = 0, 
                            prefetch_blocks = 0, ), ), 
                    working_directory = '0', 
                    retry_limit = 56, 
                    retry_count = 56, )
            )
        else :
            return CreateTaskRunRequest(
        )

    def testCreateTaskRunRequest(self):
        """Test CreateTaskRunRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
