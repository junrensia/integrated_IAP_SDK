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


class TaskVersion(object):
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
        'id': 'str',
        'href': 'str',
        'urn': 'str',
        'version': 'str',
        'description': 'str',
        'execution': 'Execution',
        'acl': 'list[str]',
        'tenant_id': 'str',
        'sub_tenant_id': 'str',
        'created_by': 'str',
        'time_created': 'datetime',
        'modified_by': 'str',
        'time_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'urn': 'urn',
        'version': 'version',
        'description': 'description',
        'execution': 'execution',
        'acl': 'acl',
        'tenant_id': 'tenantId',
        'sub_tenant_id': 'subTenantId',
        'created_by': 'createdBy',
        'time_created': 'timeCreated',
        'modified_by': 'modifiedBy',
        'time_modified': 'timeModified'
    }

    def __init__(self, id=None, href=None, urn=None, version=None, description=None, execution=None, acl=None, tenant_id=None, sub_tenant_id=None, created_by=None, time_created=None, modified_by=None, time_modified=None, local_vars_configuration=None):  # noqa: E501
        """TaskVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._href = None
        self._urn = None
        self._version = None
        self._description = None
        self._execution = None
        self._acl = None
        self._tenant_id = None
        self._sub_tenant_id = None
        self._created_by = None
        self._time_created = None
        self._modified_by = None
        self._time_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if urn is not None:
            self.urn = urn
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if execution is not None:
            self.execution = execution
        if acl is not None:
            self.acl = acl
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if sub_tenant_id is not None:
            self.sub_tenant_id = sub_tenant_id
        if created_by is not None:
            self.created_by = created_by
        if time_created is not None:
            self.time_created = time_created
        if modified_by is not None:
            self.modified_by = modified_by
        if time_modified is not None:
            self.time_modified = time_modified

    @property
    def id(self):
        """Gets the id of this TaskVersion.  # noqa: E501

        Global identifier for object  # noqa: E501

        :return: The id of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskVersion.

        Global identifier for object  # noqa: E501

        :param id: The id of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this TaskVersion.  # noqa: E501

        Href of the object  # noqa: E501

        :return: The href of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TaskVersion.

        Href of the object  # noqa: E501

        :param href: The href of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def urn(self):
        """Gets the urn of this TaskVersion.  # noqa: E501

        URN of the resource  # noqa: E501

        :return: The urn of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this TaskVersion.

        URN of the resource  # noqa: E501

        :param urn: The urn of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def version(self):
        """Gets the version of this TaskVersion.  # noqa: E501


        :return: The version of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TaskVersion.


        :param version: The version of this TaskVersion.  # noqa: E501
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
        """Gets the description of this TaskVersion.  # noqa: E501


        :return: The description of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskVersion.


        :param description: The description of this TaskVersion.  # noqa: E501
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
        """Gets the execution of this TaskVersion.  # noqa: E501


        :return: The execution of this TaskVersion.  # noqa: E501
        :rtype: Execution
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this TaskVersion.


        :param execution: The execution of this TaskVersion.  # noqa: E501
        :type: Execution
        """

        self._execution = execution

    @property
    def acl(self):
        """Gets the acl of this TaskVersion.  # noqa: E501

        Access Control List  # noqa: E501

        :return: The acl of this TaskVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this TaskVersion.

        Access Control List  # noqa: E501

        :param acl: The acl of this TaskVersion.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TaskVersion.  # noqa: E501


        :return: The tenant_id of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TaskVersion.


        :param tenant_id: The tenant_id of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this TaskVersion.  # noqa: E501


        :return: The sub_tenant_id of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this TaskVersion.


        :param sub_tenant_id: The sub_tenant_id of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def created_by(self):
        """Gets the created_by of this TaskVersion.  # noqa: E501

        User who created the object  # noqa: E501

        :return: The created_by of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TaskVersion.

        User who created the object  # noqa: E501

        :param created_by: The created_by of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def time_created(self):
        """Gets the time_created of this TaskVersion.  # noqa: E501

        Date and Time (in UTC) when object was created in TES  # noqa: E501

        :return: The time_created of this TaskVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this TaskVersion.

        Date and Time (in UTC) when object was created in TES  # noqa: E501

        :param time_created: The time_created of this TaskVersion.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def modified_by(self):
        """Gets the modified_by of this TaskVersion.  # noqa: E501

        User who updated the object  # noqa: E501

        :return: The modified_by of this TaskVersion.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this TaskVersion.

        User who updated the object  # noqa: E501

        :param modified_by: The modified_by of this TaskVersion.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def time_modified(self):
        """Gets the time_modified of this TaskVersion.  # noqa: E501

        Date and Time (in UTC) when object was modified in TES  # noqa: E501

        :return: The time_modified of this TaskVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this TaskVersion.

        Date and Time (in UTC) when object was modified in TES  # noqa: E501

        :param time_modified: The time_modified of this TaskVersion.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

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
        if not isinstance(other, TaskVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskVersion):
            return True

        return self.to_dict() != other.to_dict()
