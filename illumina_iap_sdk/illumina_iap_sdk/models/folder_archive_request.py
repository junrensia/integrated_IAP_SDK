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

from illumina_iap_sdk.configuration import Configuration


class FolderArchiveRequest(object):
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
        'storage_tier': 'FolderArchiveStorageTier'
    }

    attribute_map = {
        'storage_tier': 'storageTier'
    }

    def __init__(self, storage_tier=None, local_vars_configuration=None):  # noqa: E501
        """FolderArchiveRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._storage_tier = None
        self.discriminator = None

        self.storage_tier = storage_tier

    @property
    def storage_tier(self):
        """Gets the storage_tier of this FolderArchiveRequest.  # noqa: E501


        :return: The storage_tier of this FolderArchiveRequest.  # noqa: E501
        :rtype: FolderArchiveStorageTier
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """Sets the storage_tier of this FolderArchiveRequest.


        :param storage_tier: The storage_tier of this FolderArchiveRequest.  # noqa: E501
        :type: FolderArchiveStorageTier
        """
        if self.local_vars_configuration.client_side_validation and storage_tier is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_tier`, must not be `None`")  # noqa: E501

        self._storage_tier = storage_tier

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
        if not isinstance(other, FolderArchiveRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderArchiveRequest):
            return True

        return self.to_dict() != other.to_dict()
