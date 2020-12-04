# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WorkflowRunCompact(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'urn': 'str',
        'href': 'str',
        'name': 'str',
        'time_started': 'datetime',
        'time_stopped': 'datetime',
        'status': 'str',
        'status_summary': 'str',
        'error': 'str',
        'error_cause': 'str',
        'workflow_version': 'WorkflowVersionCompact',
        'created_by_client_id': 'str',
        'time_created': 'datetime',
        'time_modified': 'datetime',
        'created_by': 'str',
        'modified_by': 'str',
        'tenant_id': 'str',
        'acl': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'href': 'href',
        'name': 'name',
        'time_started': 'timeStarted',
        'time_stopped': 'timeStopped',
        'status': 'status',
        'status_summary': 'statusSummary',
        'error': 'error',
        'error_cause': 'errorCause',
        'workflow_version': 'workflowVersion',
        'created_by_client_id': 'createdByClientId',
        'time_created': 'timeCreated',
        'time_modified': 'timeModified',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'tenant_id': 'tenantId',
        'acl': 'acl'
    }

    def __init__(self, id=None, urn=None, href=None, name=None, time_started=None, time_stopped=None, status=None, status_summary=None, error=None, error_cause=None, workflow_version=None, created_by_client_id=None, time_created=None, time_modified=None, created_by=None, modified_by=None, tenant_id=None, acl=None):  # noqa: E501
        """WorkflowRunCompact - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._urn = None
        self._href = None
        self._name = None
        self._time_started = None
        self._time_stopped = None
        self._status = None
        self._status_summary = None
        self._error = None
        self._error_cause = None
        self._workflow_version = None
        self._created_by_client_id = None
        self._time_created = None
        self._time_modified = None
        self._created_by = None
        self._modified_by = None
        self._tenant_id = None
        self._acl = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if time_started is not None:
            self.time_started = time_started
        if time_stopped is not None:
            self.time_stopped = time_stopped
        if status is not None:
            self.status = status
        if status_summary is not None:
            self.status_summary = status_summary
        if error is not None:
            self.error = error
        if error_cause is not None:
            self.error_cause = error_cause
        if workflow_version is not None:
            self.workflow_version = workflow_version
        if created_by_client_id is not None:
            self.created_by_client_id = created_by_client_id
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if acl is not None:
            self.acl = acl

    @property
    def id(self):
        """Gets the id of this WorkflowRunCompact.  # noqa: E501

        Unique resource ID  # noqa: E501

        :return: The id of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowRunCompact.

        Unique resource ID  # noqa: E501

        :param id: The id of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this WorkflowRunCompact.  # noqa: E501

        URN of the resource  # noqa: E501

        :return: The urn of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this WorkflowRunCompact.

        URN of the resource  # noqa: E501

        :param urn: The urn of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this WorkflowRunCompact.  # noqa: E501

        HREF to the resource  # noqa: E501

        :return: The href of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this WorkflowRunCompact.

        HREF to the resource  # noqa: E501

        :param href: The href of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this WorkflowRunCompact.  # noqa: E501

        Name of the workflow run  # noqa: E501

        :return: The name of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowRunCompact.

        Name of the workflow run  # noqa: E501

        :param name: The name of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def time_started(self):
        """Gets the time_started of this WorkflowRunCompact.  # noqa: E501

        The time (in UTC) the workflow run started  # noqa: E501

        :return: The time_started of this WorkflowRunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """Sets the time_started of this WorkflowRunCompact.

        The time (in UTC) the workflow run started  # noqa: E501

        :param time_started: The time_started of this WorkflowRunCompact.  # noqa: E501
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_stopped(self):
        """Gets the time_stopped of this WorkflowRunCompact.  # noqa: E501

        The time (in UTC) the Workflow Run stopped  # noqa: E501

        :return: The time_stopped of this WorkflowRunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stopped

    @time_stopped.setter
    def time_stopped(self, time_stopped):
        """Sets the time_stopped of this WorkflowRunCompact.

        The time (in UTC) the Workflow Run stopped  # noqa: E501

        :param time_stopped: The time_stopped of this WorkflowRunCompact.  # noqa: E501
        :type: datetime
        """

        self._time_stopped = time_stopped

    @property
    def status(self):
        """Gets the status of this WorkflowRunCompact.  # noqa: E501

        Workflow run status  # noqa: E501

        :return: The status of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowRunCompact.

        Workflow run status  # noqa: E501

        :param status: The status of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_summary(self):
        """Gets the status_summary of this WorkflowRunCompact.  # noqa: E501

        Workflow run status summary  # noqa: E501

        :return: The status_summary of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this WorkflowRunCompact.

        Workflow run status summary  # noqa: E501

        :param status_summary: The status_summary of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def error(self):
        """Gets the error of this WorkflowRunCompact.  # noqa: E501

        Error for a failed workflow run  # noqa: E501

        :return: The error of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this WorkflowRunCompact.

        Error for a failed workflow run  # noqa: E501

        :param error: The error of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_cause(self):
        """Gets the error_cause of this WorkflowRunCompact.  # noqa: E501

        Error cause for a failed workflow run  # noqa: E501

        :return: The error_cause of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._error_cause

    @error_cause.setter
    def error_cause(self, error_cause):
        """Sets the error_cause of this WorkflowRunCompact.

        Error cause for a failed workflow run  # noqa: E501

        :param error_cause: The error_cause of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._error_cause = error_cause

    @property
    def workflow_version(self):
        """Gets the workflow_version of this WorkflowRunCompact.  # noqa: E501


        :return: The workflow_version of this WorkflowRunCompact.  # noqa: E501
        :rtype: WorkflowVersionCompact
        """
        return self._workflow_version

    @workflow_version.setter
    def workflow_version(self, workflow_version):
        """Sets the workflow_version of this WorkflowRunCompact.


        :param workflow_version: The workflow_version of this WorkflowRunCompact.  # noqa: E501
        :type: WorkflowVersionCompact
        """

        self._workflow_version = workflow_version

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this WorkflowRunCompact.  # noqa: E501

        Client ID of the Origin Request  # noqa: E501

        :return: The created_by_client_id of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this WorkflowRunCompact.

        Client ID of the Origin Request  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def time_created(self):
        """Gets the time_created of this WorkflowRunCompact.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this WorkflowRunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this WorkflowRunCompact.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this WorkflowRunCompact.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this WorkflowRunCompact.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this WorkflowRunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this WorkflowRunCompact.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this WorkflowRunCompact.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowRunCompact.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowRunCompact.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this WorkflowRunCompact.  # noqa: E501

        User that modified the resource  # noqa: E501

        :return: The modified_by of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this WorkflowRunCompact.

        User that modified the resource  # noqa: E501

        :param modified_by: The modified_by of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def tenant_id(self):
        """Gets the tenant_id of this WorkflowRunCompact.  # noqa: E501

        Tenant ID the resource belongs to  # noqa: E501

        :return: The tenant_id of this WorkflowRunCompact.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this WorkflowRunCompact.

        Tenant ID the resource belongs to  # noqa: E501

        :param tenant_id: The tenant_id of this WorkflowRunCompact.  # noqa: E501
        :type: str
        """
        if tenant_id is not None and len(tenant_id) > 255:
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `255`")  # noqa: E501
        if tenant_id is not None and len(tenant_id) < 0:
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def acl(self):
        """Gets the acl of this WorkflowRunCompact.  # noqa: E501

        Access control list of the resource  # noqa: E501

        :return: The acl of this WorkflowRunCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this WorkflowRunCompact.

        Access control list of the resource  # noqa: E501

        :param acl: The acl of this WorkflowRunCompact.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(WorkflowRunCompact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowRunCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
