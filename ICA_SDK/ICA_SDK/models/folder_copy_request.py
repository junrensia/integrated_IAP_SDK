# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ICA_SDK.configuration import Configuration


class FolderCopyRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'target_parent_folder_id': 'str',
        'destination_folder_name': 'str'
    }

    attribute_map = {
        'target_parent_folder_id': 'targetParentFolderId',
        'destination_folder_name': 'destinationFolderName'
    }

    def __init__(self, target_parent_folder_id=None, destination_folder_name=None, local_vars_configuration=None):  # noqa: E501
        """FolderCopyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_parent_folder_id = None
        self._destination_folder_name = None
        self.discriminator = None

        self.target_parent_folder_id = target_parent_folder_id
        if destination_folder_name is not None:
            self.destination_folder_name = destination_folder_name

    @property
    def target_parent_folder_id(self):
        """Gets the target_parent_folder_id of this FolderCopyRequest.  # noqa: E501

        The parent folder into which the source folder will be copied.  # noqa: E501

        :return: The target_parent_folder_id of this FolderCopyRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_parent_folder_id

    @target_parent_folder_id.setter
    def target_parent_folder_id(self, target_parent_folder_id):
        """Sets the target_parent_folder_id of this FolderCopyRequest.

        The parent folder into which the source folder will be copied.  # noqa: E501

        :param target_parent_folder_id: The target_parent_folder_id of this FolderCopyRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_parent_folder_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_parent_folder_id`, must not be `None`")  # noqa: E501

        self._target_parent_folder_id = target_parent_folder_id

    @property
    def destination_folder_name(self):
        """Gets the destination_folder_name of this FolderCopyRequest.  # noqa: E501

        A new name for the destination folder. Required if target parent folder is the same as the destination folder.  When optional and not provided, the source folder name is used as the destination folder name.  # noqa: E501

        :return: The destination_folder_name of this FolderCopyRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_folder_name

    @destination_folder_name.setter
    def destination_folder_name(self, destination_folder_name):
        """Sets the destination_folder_name of this FolderCopyRequest.

        A new name for the destination folder. Required if target parent folder is the same as the destination folder.  When optional and not provided, the source folder name is used as the destination folder name.  # noqa: E501

        :param destination_folder_name: The destination_folder_name of this FolderCopyRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                destination_folder_name is not None and not re.search(r'^[^\/]+$', destination_folder_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `destination_folder_name`, must be a follow pattern or equal to `/^[^\/]+$/`")  # noqa: E501

        self._destination_folder_name = destination_folder_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FolderCopyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderCopyRequest):
            return True

        return self.to_dict() != other.to_dict()
