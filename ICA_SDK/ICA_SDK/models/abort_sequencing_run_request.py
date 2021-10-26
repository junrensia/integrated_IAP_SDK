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


class AbortSequencingRunRequest(object):
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
        'instrument_run_status': 'str',
        'instrument_run_status_summary': 'str'
    }

    attribute_map = {
        'instrument_run_status': 'instrumentRunStatus',
        'instrument_run_status_summary': 'instrumentRunStatusSummary'
    }

    def __init__(self, instrument_run_status=None, instrument_run_status_summary=None, local_vars_configuration=None):  # noqa: E501
        """AbortSequencingRunRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_run_status = None
        self._instrument_run_status_summary = None
        self.discriminator = None

        if instrument_run_status is not None:
            self.instrument_run_status = instrument_run_status
        if instrument_run_status_summary is not None:
            self.instrument_run_status_summary = instrument_run_status_summary

    @property
    def instrument_run_status(self):
        """Gets the instrument_run_status of this AbortSequencingRunRequest.  # noqa: E501

        Optional run status from instrument  # noqa: E501

        :return: The instrument_run_status of this AbortSequencingRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_run_status

    @instrument_run_status.setter
    def instrument_run_status(self, instrument_run_status):
        """Sets the instrument_run_status of this AbortSequencingRunRequest.

        Optional run status from instrument  # noqa: E501

        :param instrument_run_status: The instrument_run_status of this AbortSequencingRunRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_status is not None and len(instrument_run_status) > 40):
            raise ValueError("Invalid value for `instrument_run_status`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_status is not None and len(instrument_run_status) < 0):
            raise ValueError("Invalid value for `instrument_run_status`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_run_status = instrument_run_status

    @property
    def instrument_run_status_summary(self):
        """Gets the instrument_run_status_summary of this AbortSequencingRunRequest.  # noqa: E501

        Optional reason/summary for abort  # noqa: E501

        :return: The instrument_run_status_summary of this AbortSequencingRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument_run_status_summary

    @instrument_run_status_summary.setter
    def instrument_run_status_summary(self, instrument_run_status_summary):
        """Sets the instrument_run_status_summary of this AbortSequencingRunRequest.

        Optional reason/summary for abort  # noqa: E501

        :param instrument_run_status_summary: The instrument_run_status_summary of this AbortSequencingRunRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_status_summary is not None and len(instrument_run_status_summary) > 255):
            raise ValueError("Invalid value for `instrument_run_status_summary`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instrument_run_status_summary is not None and len(instrument_run_status_summary) < 0):
            raise ValueError("Invalid value for `instrument_run_status_summary`, length must be greater than or equal to `0`")  # noqa: E501

        self._instrument_run_status_summary = instrument_run_status_summary

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
        if not isinstance(other, AbortSequencingRunRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AbortSequencingRunRequest):
            return True

        return self.to_dict() != other.to_dict()
