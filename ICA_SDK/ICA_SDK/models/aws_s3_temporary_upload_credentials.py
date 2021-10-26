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


class AwsS3TemporaryUploadCredentials(object):
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
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'session_token': 'str',
        'region': 'str',
        'bucket_name': 'str',
        'key_prefix': 'str',
        'expiration_date': 'datetime'
    }

    attribute_map = {
        'access_key_id': 'access_Key_Id',
        'secret_access_key': 'secret_Access_Key',
        'session_token': 'session_Token',
        'region': 'region',
        'bucket_name': 'bucketName',
        'key_prefix': 'keyPrefix',
        'expiration_date': 'expirationDate'
    }

    def __init__(self, access_key_id=None, secret_access_key=None, session_token=None, region=None, bucket_name=None, key_prefix=None, expiration_date=None, local_vars_configuration=None):  # noqa: E501
        """AwsS3TemporaryUploadCredentials - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key_id = None
        self._secret_access_key = None
        self._session_token = None
        self._region = None
        self._bucket_name = None
        self._key_prefix = None
        self._expiration_date = None
        self.discriminator = None

        if access_key_id is not None:
            self.access_key_id = access_key_id
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if session_token is not None:
            self.session_token = session_token
        if region is not None:
            self.region = region
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if key_prefix is not None:
            self.key_prefix = key_prefix
        if expiration_date is not None:
            self.expiration_date = expiration_date

    @property
    def access_key_id(self):
        """Gets the access_key_id of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        Access key for use with AWS S3  # noqa: E501

        :return: The access_key_id of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this AwsS3TemporaryUploadCredentials.

        Access key for use with AWS S3  # noqa: E501

        :param access_key_id: The access_key_id of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        Secret key for use with AWS S3  # noqa: E501

        :return: The secret_access_key of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this AwsS3TemporaryUploadCredentials.

        Secret key for use with AWS S3  # noqa: E501

        :param secret_access_key: The secret_access_key of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def session_token(self):
        """Gets the session_token of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        Token for use with AWS S3  # noqa: E501

        :return: The session_token of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        """Sets the session_token of this AwsS3TemporaryUploadCredentials.

        Token for use with AWS S3  # noqa: E501

        :param session_token: The session_token of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: str
        """

        self._session_token = session_token

    @property
    def region(self):
        """Gets the region of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        AWS region the folder will/does reside in  # noqa: E501

        :return: The region of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsS3TemporaryUploadCredentials.

        AWS region the folder will/does reside in  # noqa: E501

        :param region: The region of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def bucket_name(self):
        """Gets the bucket_name of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        AWS bucket the folder will/does reside in  # noqa: E501

        :return: The bucket_name of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this AwsS3TemporaryUploadCredentials.

        AWS bucket the folder will/does reside in  # noqa: E501

        :param bucket_name: The bucket_name of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def key_prefix(self):
        """Gets the key_prefix of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        AWS upload location for this folder  # noqa: E501

        :return: The key_prefix of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: str
        """
        return self._key_prefix

    @key_prefix.setter
    def key_prefix(self, key_prefix):
        """Sets the key_prefix of this AwsS3TemporaryUploadCredentials.

        AWS upload location for this folder  # noqa: E501

        :param key_prefix: The key_prefix of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: str
        """

        self._key_prefix = key_prefix

    @property
    def expiration_date(self):
        """Gets the expiration_date of this AwsS3TemporaryUploadCredentials.  # noqa: E501

        expiration for temporary credentials  # noqa: E501

        :return: The expiration_date of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this AwsS3TemporaryUploadCredentials.

        expiration for temporary credentials  # noqa: E501

        :param expiration_date: The expiration_date of this AwsS3TemporaryUploadCredentials.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

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
        if not isinstance(other, AwsS3TemporaryUploadCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsS3TemporaryUploadCredentials):
            return True

        return self.to_dict() != other.to_dict()
