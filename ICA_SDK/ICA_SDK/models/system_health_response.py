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


class SystemHealthResponse(object):
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
        'status': 'HealthCheckStatuses',
        'details': 'list[ServiceHealthResponse]'
    }

    attribute_map = {
        'status': 'status',
        'details': 'details'
    }

    def __init__(self, status=None, details=None, local_vars_configuration=None):  # noqa: E501
        """SystemHealthResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._details = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if details is not None:
            self.details = details

    @property
    def status(self):
        """Gets the status of this SystemHealthResponse.  # noqa: E501


        :return: The status of this SystemHealthResponse.  # noqa: E501
        :rtype: HealthCheckStatuses
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SystemHealthResponse.


        :param status: The status of this SystemHealthResponse.  # noqa: E501
        :type: HealthCheckStatuses
        """

        self._status = status

    @property
    def details(self):
        """Gets the details of this SystemHealthResponse.  # noqa: E501

        Service health details  # noqa: E501

        :return: The details of this SystemHealthResponse.  # noqa: E501
        :rtype: list[ServiceHealthResponse]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SystemHealthResponse.

        Service health details  # noqa: E501

        :param details: The details of this SystemHealthResponse.  # noqa: E501
        :type: list[ServiceHealthResponse]
        """

        self._details = details

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
        if not isinstance(other, SystemHealthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemHealthResponse):
            return True

        return self.to_dict() != other.to_dict()
