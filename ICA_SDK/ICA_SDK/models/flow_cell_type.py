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


class FlowCellType(object):
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
        'type': 'str',
        'max_number_of_lanes': 'int'
    }

    attribute_map = {
        'type': 'type',
        'max_number_of_lanes': 'maxNumberOfLanes'
    }

    def __init__(self, type=None, max_number_of_lanes=None, local_vars_configuration=None):  # noqa: E501
        """FlowCellType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._max_number_of_lanes = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if max_number_of_lanes is not None:
            self.max_number_of_lanes = max_number_of_lanes

    @property
    def type(self):
        """Gets the type of this FlowCellType.  # noqa: E501

        Indicates flow cell type  # noqa: E501

        :return: The type of this FlowCellType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FlowCellType.

        Indicates flow cell type  # noqa: E501

        :param type: The type of this FlowCellType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def max_number_of_lanes(self):
        """Gets the max_number_of_lanes of this FlowCellType.  # noqa: E501

        Indicates the maximum number of lanes supported by flowcell type  # noqa: E501

        :return: The max_number_of_lanes of this FlowCellType.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_lanes

    @max_number_of_lanes.setter
    def max_number_of_lanes(self, max_number_of_lanes):
        """Sets the max_number_of_lanes of this FlowCellType.

        Indicates the maximum number of lanes supported by flowcell type  # noqa: E501

        :param max_number_of_lanes: The max_number_of_lanes of this FlowCellType.  # noqa: E501
        :type: int
        """

        self._max_number_of_lanes = max_number_of_lanes

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
        if not isinstance(other, FlowCellType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FlowCellType):
            return True

        return self.to_dict() != other.to_dict()
