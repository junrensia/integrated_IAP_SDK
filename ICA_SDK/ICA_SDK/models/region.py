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


class Region(object):
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
        'name': 'str',
        'display_name': 'str',
        'base_url': 'str',
        'is_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'base_url': 'baseUrl',
        'is_enabled': 'isEnabled'
    }

    def __init__(self, name=None, display_name=None, base_url=None, is_enabled=None, local_vars_configuration=None):  # noqa: E501
        """Region - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._display_name = None
        self._base_url = None
        self._is_enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if base_url is not None:
            self.base_url = base_url
        if is_enabled is not None:
            self.is_enabled = is_enabled

    @property
    def name(self):
        """Gets the name of this Region.  # noqa: E501

        Name of the environment  # noqa: E501

        :return: The name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Region.

        Name of the environment  # noqa: E501

        :param name: The name of this Region.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Region.  # noqa: E501

        Display name for the environment  # noqa: E501

        :return: The display_name of this Region.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Region.

        Display name for the environment  # noqa: E501

        :param display_name: The display_name of this Region.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def base_url(self):
        """Gets the base_url of this Region.  # noqa: E501

        BaseUrl for the environment  # noqa: E501

        :return: The base_url of this Region.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this Region.

        BaseUrl for the environment  # noqa: E501

        :param base_url: The base_url of this Region.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def is_enabled(self):
        """Gets the is_enabled of this Region.  # noqa: E501

        True if the environment is enabled  # noqa: E501

        :return: The is_enabled of this Region.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this Region.

        True if the environment is enabled  # noqa: E501

        :param is_enabled: The is_enabled of this Region.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

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
        if not isinstance(other, Region):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Region):
            return True

        return self.to_dict() != other.to_dict()
