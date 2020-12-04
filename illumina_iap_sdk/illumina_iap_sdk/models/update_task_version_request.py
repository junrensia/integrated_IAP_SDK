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


class UpdateTaskVersionRequest(object):
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
        'version': 'str',
        'description': 'str',
        'execution': 'Execution',
        'acl': 'list[str]'
    }

    attribute_map = {
        'version': 'version',
        'description': 'description',
        'execution': 'execution',
        'acl': 'acl'
    }

    def __init__(self, version=None, description=None, execution=None, acl=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTaskVersionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._description = None
        self._execution = None
        self._acl = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if execution is not None:
            self.execution = execution
        if acl is not None:
            self.acl = acl

    @property
    def version(self):
        """Gets the version of this UpdateTaskVersionRequest.  # noqa: E501

        User-defined version of task version  # noqa: E501

        :return: The version of this UpdateTaskVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateTaskVersionRequest.

        User-defined version of task version  # noqa: E501

        :param version: The version of this UpdateTaskVersionRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 255):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 0):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `0`")  # noqa: E501

        self._version = version

    @property
    def description(self):
        """Gets the description of this UpdateTaskVersionRequest.  # noqa: E501

        User-defined description of task version  # noqa: E501

        :return: The description of this UpdateTaskVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTaskVersionRequest.

        User-defined description of task version  # noqa: E501

        :param description: The description of this UpdateTaskVersionRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 4096):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4096`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def execution(self):
        """Gets the execution of this UpdateTaskVersionRequest.  # noqa: E501


        :return: The execution of this UpdateTaskVersionRequest.  # noqa: E501
        :rtype: Execution
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this UpdateTaskVersionRequest.


        :param execution: The execution of this UpdateTaskVersionRequest.  # noqa: E501
        :type: Execution
        """

        self._execution = execution

    @property
    def acl(self):
        """Gets the acl of this UpdateTaskVersionRequest.  # noqa: E501


        :return: The acl of this UpdateTaskVersionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this UpdateTaskVersionRequest.


        :param acl: The acl of this UpdateTaskVersionRequest.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

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
        if not isinstance(other, UpdateTaskVersionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTaskVersionRequest):
            return True

        return self.to_dict() != other.to_dict()
