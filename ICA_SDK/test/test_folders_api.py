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
from ICA_SDK.api.folders_api import FoldersApi  # noqa: E501
from ICA_SDK.rest import ApiException


class TestFoldersApi(unittest.TestCase):
    """FoldersApi unit test stubs"""

    def setUp(self):
        self.api = ICA_SDK.api.folders_api.FoldersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_folder(self):
        """Test case for archive_folder

        Archive a folder  # noqa: E501
        """
        pass

    def test_complete_folder_session(self):
        """Test case for complete_folder_session

        Complete a folder upload in GDS  # noqa: E501
        """
        pass

    def test_copy_folder(self):
        """Test case for copy_folder

        Copy a folder  # noqa: E501
        """
        pass

    def test_create_folder(self):
        """Test case for create_folder

        Create a folder in GDS and receive credentials for upload  # noqa: E501
        """
        pass

    def test_delete_folder(self):
        """Test case for delete_folder

        Deletes a folder by id  # noqa: E501
        """
        pass

    def test_get_folder(self):
        """Test case for get_folder

        Get information about a folder in GDS.  # noqa: E501
        """
        pass

    def test_get_folder_job(self):
        """Test case for get_folder_job

        Get status of a folder job in GDS  # noqa: E501
        """
        pass

    def test_get_folder_session(self):
        """Test case for get_folder_session

        Get status of a folder upload in GDS  # noqa: E501
        """
        pass

    def test_list_folders(self):
        """Test case for list_folders

        Get a list of folders  # noqa: E501
        """
        pass

    def test_unarchive_folder(self):
        """Test case for unarchive_folder

        Unarchive a folder  # noqa: E501
        """
        pass

    def test_update_folder(self):
        """Test case for update_folder

        Update a folder content or acl  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
