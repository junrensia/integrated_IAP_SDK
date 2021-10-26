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


class ObjectStoreSettings(object):
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
        'aws_s3': 'AWSS3ObjectStoreSetting',
        'secret_name': 'str',
        'secret_id': 'str'
    }

    attribute_map = {
        'aws_s3': 'awsS3',
        'secret_name': 'secretName',
        'secret_id': 'secretId'
    }

    def __init__(self, aws_s3=None, secret_name=None, secret_id=None, local_vars_configuration=None):  # noqa: E501
        """ObjectStoreSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aws_s3 = None
        self._secret_name = None
        self._secret_id = None
        self.discriminator = None

        self.aws_s3 = aws_s3
        if secret_name is not None:
            self.secret_name = secret_name
        if secret_id is not None:
            self.secret_id = secret_id

    @property
    def aws_s3(self):
        """Gets the aws_s3 of this ObjectStoreSettings.  # noqa: E501


        :return: The aws_s3 of this ObjectStoreSettings.  # noqa: E501
        :rtype: AWSS3ObjectStoreSetting
        """
        return self._aws_s3

    @aws_s3.setter
    def aws_s3(self, aws_s3):
        """Sets the aws_s3 of this ObjectStoreSettings.


        :param aws_s3: The aws_s3 of this ObjectStoreSettings.  # noqa: E501
        :type: AWSS3ObjectStoreSetting
        """
        if self.local_vars_configuration.client_side_validation and aws_s3 is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_s3`, must not be `None`")  # noqa: E501

        self._aws_s3 = aws_s3

    @property
    def secret_name(self):
        """Gets the secret_name of this ObjectStoreSettings.  # noqa: E501

        Platform credentials Name  Must provide either SecretId or SecretName  # noqa: E501

        :return: The secret_name of this ObjectStoreSettings.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this ObjectStoreSettings.

        Platform credentials Name  Must provide either SecretId or SecretName  # noqa: E501

        :param secret_name: The secret_name of this ObjectStoreSettings.  # noqa: E501
        :type: str
        """

        self._secret_name = secret_name

    @property
    def secret_id(self):
        """Gets the secret_id of this ObjectStoreSettings.  # noqa: E501

        Platform credentials Id  Must provide either SecretId or SecretName  # noqa: E501

        :return: The secret_id of this ObjectStoreSettings.  # noqa: E501
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this ObjectStoreSettings.

        Platform credentials Id  Must provide either SecretId or SecretName  # noqa: E501

        :param secret_id: The secret_id of this ObjectStoreSettings.  # noqa: E501
        :type: str
        """

        self._secret_id = secret_id

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
        if not isinstance(other, ObjectStoreSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectStoreSettings):
            return True

        return self.to_dict() != other.to_dict()
