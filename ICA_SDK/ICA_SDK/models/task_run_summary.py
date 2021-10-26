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


class TaskRunSummary(object):
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
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'status_details': 'str',
        'type_of_resource': 'str',
        'size_of_resource': 'str',
        'tier_of_resource': 'str',
        'task_version_summary': 'TaskVersionSummary',
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
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'status_details': 'statusDetails',
        'type_of_resource': 'typeOfResource',
        'size_of_resource': 'sizeOfResource',
        'tier_of_resource': 'tierOfResource',
        'task_version_summary': 'taskVersionSummary',
        'acl': 'acl',
        'tenant_id': 'tenantId',
        'sub_tenant_id': 'subTenantId',
        'created_by': 'createdBy',
        'time_created': 'timeCreated',
        'modified_by': 'modifiedBy',
        'time_modified': 'timeModified'
    }

    def __init__(self, id=None, href=None, urn=None, name=None, description=None, status='Pending', status_details=None, type_of_resource=None, size_of_resource=None, tier_of_resource=None, task_version_summary=None, acl=None, tenant_id=None, sub_tenant_id=None, created_by=None, time_created=None, modified_by=None, time_modified=None, local_vars_configuration=None):  # noqa: E501
        """TaskRunSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._href = None
        self._urn = None
        self._name = None
        self._description = None
        self._status = None
        self._status_details = None
        self._type_of_resource = None
        self._size_of_resource = None
        self._tier_of_resource = None
        self._task_version_summary = None
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
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details
        if type_of_resource is not None:
            self.type_of_resource = type_of_resource
        if size_of_resource is not None:
            self.size_of_resource = size_of_resource
        if tier_of_resource is not None:
            self.tier_of_resource = tier_of_resource
        if task_version_summary is not None:
            self.task_version_summary = task_version_summary
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
        """Gets the id of this TaskRunSummary.  # noqa: E501

        Global identifier for object  # noqa: E501

        :return: The id of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskRunSummary.

        Global identifier for object  # noqa: E501

        :param id: The id of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this TaskRunSummary.  # noqa: E501

        Href of the object  # noqa: E501

        :return: The href of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TaskRunSummary.

        Href of the object  # noqa: E501

        :param href: The href of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def urn(self):
        """Gets the urn of this TaskRunSummary.  # noqa: E501

        URN of the resource  # noqa: E501

        :return: The urn of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this TaskRunSummary.

        URN of the resource  # noqa: E501

        :param urn: The urn of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def name(self):
        """Gets the name of this TaskRunSummary.  # noqa: E501


        :return: The name of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskRunSummary.


        :param name: The name of this TaskRunSummary.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this TaskRunSummary.  # noqa: E501


        :return: The description of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskRunSummary.


        :param description: The description of this TaskRunSummary.  # noqa: E501
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
    def status(self):
        """Gets the status of this TaskRunSummary.  # noqa: E501


        :return: The status of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskRunSummary.


        :param status: The status of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_details(self):
        """Gets the status_details of this TaskRunSummary.  # noqa: E501


        :return: The status_details of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this TaskRunSummary.


        :param status_details: The status_details of this TaskRunSummary.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status_details is not None and len(status_details) > 4096):
            raise ValueError("Invalid value for `status_details`, length must be less than or equal to `4096`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status_details is not None and len(status_details) < 0):
            raise ValueError("Invalid value for `status_details`, length must be greater than or equal to `0`")  # noqa: E501

        self._status_details = status_details

    @property
    def type_of_resource(self):
        """Gets the type_of_resource of this TaskRunSummary.  # noqa: E501


        :return: The type_of_resource of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._type_of_resource

    @type_of_resource.setter
    def type_of_resource(self, type_of_resource):
        """Sets the type_of_resource of this TaskRunSummary.


        :param type_of_resource: The type_of_resource of this TaskRunSummary.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type_of_resource is not None and len(type_of_resource) > 255):
            raise ValueError("Invalid value for `type_of_resource`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type_of_resource is not None and len(type_of_resource) < 0):
            raise ValueError("Invalid value for `type_of_resource`, length must be greater than or equal to `0`")  # noqa: E501

        self._type_of_resource = type_of_resource

    @property
    def size_of_resource(self):
        """Gets the size_of_resource of this TaskRunSummary.  # noqa: E501


        :return: The size_of_resource of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._size_of_resource

    @size_of_resource.setter
    def size_of_resource(self, size_of_resource):
        """Sets the size_of_resource of this TaskRunSummary.


        :param size_of_resource: The size_of_resource of this TaskRunSummary.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                size_of_resource is not None and len(size_of_resource) > 255):
            raise ValueError("Invalid value for `size_of_resource`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size_of_resource is not None and len(size_of_resource) < 0):
            raise ValueError("Invalid value for `size_of_resource`, length must be greater than or equal to `0`")  # noqa: E501

        self._size_of_resource = size_of_resource

    @property
    def tier_of_resource(self):
        """Gets the tier_of_resource of this TaskRunSummary.  # noqa: E501


        :return: The tier_of_resource of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._tier_of_resource

    @tier_of_resource.setter
    def tier_of_resource(self, tier_of_resource):
        """Sets the tier_of_resource of this TaskRunSummary.


        :param tier_of_resource: The tier_of_resource of this TaskRunSummary.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tier_of_resource is not None and len(tier_of_resource) > 255):
            raise ValueError("Invalid value for `tier_of_resource`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tier_of_resource is not None and len(tier_of_resource) < 0):
            raise ValueError("Invalid value for `tier_of_resource`, length must be greater than or equal to `0`")  # noqa: E501

        self._tier_of_resource = tier_of_resource

    @property
    def task_version_summary(self):
        """Gets the task_version_summary of this TaskRunSummary.  # noqa: E501


        :return: The task_version_summary of this TaskRunSummary.  # noqa: E501
        :rtype: TaskVersionSummary
        """
        return self._task_version_summary

    @task_version_summary.setter
    def task_version_summary(self, task_version_summary):
        """Sets the task_version_summary of this TaskRunSummary.


        :param task_version_summary: The task_version_summary of this TaskRunSummary.  # noqa: E501
        :type: TaskVersionSummary
        """

        self._task_version_summary = task_version_summary

    @property
    def acl(self):
        """Gets the acl of this TaskRunSummary.  # noqa: E501

        Access Control List  # noqa: E501

        :return: The acl of this TaskRunSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this TaskRunSummary.

        Access Control List  # noqa: E501

        :param acl: The acl of this TaskRunSummary.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TaskRunSummary.  # noqa: E501


        :return: The tenant_id of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TaskRunSummary.


        :param tenant_id: The tenant_id of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this TaskRunSummary.  # noqa: E501


        :return: The sub_tenant_id of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this TaskRunSummary.


        :param sub_tenant_id: The sub_tenant_id of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def created_by(self):
        """Gets the created_by of this TaskRunSummary.  # noqa: E501

        User who created the object  # noqa: E501

        :return: The created_by of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TaskRunSummary.

        User who created the object  # noqa: E501

        :param created_by: The created_by of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def time_created(self):
        """Gets the time_created of this TaskRunSummary.  # noqa: E501

        Date and Time (in UTC) when object was created in TES  # noqa: E501

        :return: The time_created of this TaskRunSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this TaskRunSummary.

        Date and Time (in UTC) when object was created in TES  # noqa: E501

        :param time_created: The time_created of this TaskRunSummary.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def modified_by(self):
        """Gets the modified_by of this TaskRunSummary.  # noqa: E501

        User who updated the object  # noqa: E501

        :return: The modified_by of this TaskRunSummary.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this TaskRunSummary.

        User who updated the object  # noqa: E501

        :param modified_by: The modified_by of this TaskRunSummary.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def time_modified(self):
        """Gets the time_modified of this TaskRunSummary.  # noqa: E501

        Date and Time (in UTC) when object was modified in TES  # noqa: E501

        :return: The time_modified of this TaskRunSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this TaskRunSummary.

        Date and Time (in UTC) when object was modified in TES  # noqa: E501

        :param time_modified: The time_modified of this TaskRunSummary.  # noqa: E501
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
        if not isinstance(other, TaskRunSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskRunSummary):
            return True

        return self.to_dict() != other.to_dict()
