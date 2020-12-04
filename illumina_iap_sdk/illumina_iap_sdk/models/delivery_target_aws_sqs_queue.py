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


class DeliveryTargetAwsSqsQueue(object):
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
        'queue_url': 'str'
    }

    attribute_map = {
        'queue_url': 'queueUrl'
    }

    def __init__(self, queue_url=None, local_vars_configuration=None):  # noqa: E501
        """DeliveryTargetAwsSqsQueue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._queue_url = None
        self.discriminator = None

        self.queue_url = queue_url

    @property
    def queue_url(self):
        """Gets the queue_url of this DeliveryTargetAwsSqsQueue.  # noqa: E501

        URL for the AWS SQS queue  # noqa: E501

        :return: The queue_url of this DeliveryTargetAwsSqsQueue.  # noqa: E501
        :rtype: str
        """
        return self._queue_url

    @queue_url.setter
    def queue_url(self, queue_url):
        """Sets the queue_url of this DeliveryTargetAwsSqsQueue.

        URL for the AWS SQS queue  # noqa: E501

        :param queue_url: The queue_url of this DeliveryTargetAwsSqsQueue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and queue_url is None:  # noqa: E501
            raise ValueError("Invalid value for `queue_url`, must not be `None`")  # noqa: E501

        self._queue_url = queue_url

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
        if not isinstance(other, DeliveryTargetAwsSqsQueue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryTargetAwsSqsQueue):
            return True

        return self.to_dict() != other.to_dict()
