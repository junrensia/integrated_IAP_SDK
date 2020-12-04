# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from integrated_sdk.configuration import Configuration


class WorkflowSignal(object):
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
        'urn': 'str',
        'href': 'str',
        'send_heartbeat_href': 'str',
        'send_success_response_href': 'str',
        'send_failure_response_href': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'description': 'str',
        'inputs': 'object',
        'workflow_run': 'WorkflowRunCompact',
        'timeout_seconds': 'int',
        'result': 'object',
        'error': 'str',
        'error_cause': 'str',
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
        'send_heartbeat_href': 'sendHeartbeatHref',
        'send_success_response_href': 'sendSuccessResponseHref',
        'send_failure_response_href': 'sendFailureResponseHref',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'description': 'description',
        'inputs': 'inputs',
        'workflow_run': 'workflowRun',
        'timeout_seconds': 'timeoutSeconds',
        'result': 'result',
        'error': 'error',
        'error_cause': 'errorCause',
        'created_by_client_id': 'createdByClientId',
        'time_created': 'timeCreated',
        'time_modified': 'timeModified',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'tenant_id': 'tenantId',
        'acl': 'acl'
    }

    def __init__(self, id=None, urn=None, href=None, send_heartbeat_href=None, send_success_response_href=None, send_failure_response_href=None, name=None, status=None, type=None, description=None, inputs=None, workflow_run=None, timeout_seconds=None, result=None, error=None, error_cause=None, created_by_client_id=None, time_created=None, time_modified=None, created_by=None, modified_by=None, tenant_id=None, acl=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowSignal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._urn = None
        self._href = None
        self._send_heartbeat_href = None
        self._send_success_response_href = None
        self._send_failure_response_href = None
        self._name = None
        self._status = None
        self._type = None
        self._description = None
        self._inputs = None
        self._workflow_run = None
        self._timeout_seconds = None
        self._result = None
        self._error = None
        self._error_cause = None
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
        if send_heartbeat_href is not None:
            self.send_heartbeat_href = send_heartbeat_href
        if send_success_response_href is not None:
            self.send_success_response_href = send_success_response_href
        if send_failure_response_href is not None:
            self.send_failure_response_href = send_failure_response_href
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if inputs is not None:
            self.inputs = inputs
        if workflow_run is not None:
            self.workflow_run = workflow_run
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if result is not None:
            self.result = result
        if error is not None:
            self.error = error
        if error_cause is not None:
            self.error_cause = error_cause
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
        """Gets the id of this WorkflowSignal.  # noqa: E501

        Unique resource ID  # noqa: E501

        :return: The id of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowSignal.

        Unique resource ID  # noqa: E501

        :param id: The id of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this WorkflowSignal.  # noqa: E501

        URN of the resource  # noqa: E501

        :return: The urn of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this WorkflowSignal.

        URN of the resource  # noqa: E501

        :param urn: The urn of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this WorkflowSignal.  # noqa: E501

        HREF to the resource  # noqa: E501

        :return: The href of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this WorkflowSignal.

        HREF to the resource  # noqa: E501

        :param href: The href of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def send_heartbeat_href(self):
        """Gets the send_heartbeat_href of this WorkflowSignal.  # noqa: E501

        HREF to send a heartbeat to a workflow signal  # noqa: E501

        :return: The send_heartbeat_href of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._send_heartbeat_href

    @send_heartbeat_href.setter
    def send_heartbeat_href(self, send_heartbeat_href):
        """Sets the send_heartbeat_href of this WorkflowSignal.

        HREF to send a heartbeat to a workflow signal  # noqa: E501

        :param send_heartbeat_href: The send_heartbeat_href of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._send_heartbeat_href = send_heartbeat_href

    @property
    def send_success_response_href(self):
        """Gets the send_success_response_href of this WorkflowSignal.  # noqa: E501

        HREF to succeed a workflow signal  # noqa: E501

        :return: The send_success_response_href of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._send_success_response_href

    @send_success_response_href.setter
    def send_success_response_href(self, send_success_response_href):
        """Sets the send_success_response_href of this WorkflowSignal.

        HREF to succeed a workflow signal  # noqa: E501

        :param send_success_response_href: The send_success_response_href of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._send_success_response_href = send_success_response_href

    @property
    def send_failure_response_href(self):
        """Gets the send_failure_response_href of this WorkflowSignal.  # noqa: E501

        HREF to fail a workflow signal  # noqa: E501

        :return: The send_failure_response_href of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._send_failure_response_href

    @send_failure_response_href.setter
    def send_failure_response_href(self, send_failure_response_href):
        """Sets the send_failure_response_href of this WorkflowSignal.

        HREF to fail a workflow signal  # noqa: E501

        :param send_failure_response_href: The send_failure_response_href of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._send_failure_response_href = send_failure_response_href

    @property
    def name(self):
        """Gets the name of this WorkflowSignal.  # noqa: E501

        Unique name of the signal  # noqa: E501

        :return: The name of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowSignal.

        Unique name of the signal  # noqa: E501

        :param name: The name of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this WorkflowSignal.  # noqa: E501

        Current status of the signal  # noqa: E501

        :return: The status of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowSignal.

        Current status of the signal  # noqa: E501

        :param status: The status of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this WorkflowSignal.  # noqa: E501

        User-defined type associated with the signal  # noqa: E501

        :return: The type of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkflowSignal.

        User-defined type associated with the signal  # noqa: E501

        :param type: The type of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this WorkflowSignal.  # noqa: E501

        Description of the signal  # noqa: E501

        :return: The description of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowSignal.

        Description of the signal  # noqa: E501

        :param description: The description of this WorkflowSignal.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 256):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def inputs(self):
        """Gets the inputs of this WorkflowSignal.  # noqa: E501

        Inputs defined by the originating WaitForSignal state, in JSON.  # noqa: E501

        :return: The inputs of this WorkflowSignal.  # noqa: E501
        :rtype: object
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this WorkflowSignal.

        Inputs defined by the originating WaitForSignal state, in JSON.  # noqa: E501

        :param inputs: The inputs of this WorkflowSignal.  # noqa: E501
        :type: object
        """

        self._inputs = inputs

    @property
    def workflow_run(self):
        """Gets the workflow_run of this WorkflowSignal.  # noqa: E501


        :return: The workflow_run of this WorkflowSignal.  # noqa: E501
        :rtype: WorkflowRunCompact
        """
        return self._workflow_run

    @workflow_run.setter
    def workflow_run(self, workflow_run):
        """Sets the workflow_run of this WorkflowSignal.


        :param workflow_run: The workflow_run of this WorkflowSignal.  # noqa: E501
        :type: WorkflowRunCompact
        """

        self._workflow_run = workflow_run

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this WorkflowSignal.  # noqa: E501

        Signal timeout in seconds. The Signal will timeout if a heartbeat, succeed or fail is not received in this time interval.  # noqa: E501

        :return: The timeout_seconds of this WorkflowSignal.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this WorkflowSignal.

        Signal timeout in seconds. The Signal will timeout if a heartbeat, succeed or fail is not received in this time interval.  # noqa: E501

        :param timeout_seconds: The timeout_seconds of this WorkflowSignal.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    @property
    def result(self):
        """Gets the result of this WorkflowSignal.  # noqa: E501

        The result of a successful signalling action in JSON.  # noqa: E501

        :return: The result of this WorkflowSignal.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this WorkflowSignal.

        The result of a successful signalling action in JSON.  # noqa: E501

        :param result: The result of this WorkflowSignal.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def error(self):
        """Gets the error of this WorkflowSignal.  # noqa: E501

        The error of a failed signal.  # noqa: E501

        :return: The error of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this WorkflowSignal.

        The error of a failed signal.  # noqa: E501

        :param error: The error of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_cause(self):
        """Gets the error_cause of this WorkflowSignal.  # noqa: E501

        The error cause of a failed signal.  # noqa: E501

        :return: The error_cause of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._error_cause

    @error_cause.setter
    def error_cause(self, error_cause):
        """Sets the error_cause of this WorkflowSignal.

        The error cause of a failed signal.  # noqa: E501

        :param error_cause: The error_cause of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._error_cause = error_cause

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this WorkflowSignal.  # noqa: E501

        Client ID of the Origin Request  # noqa: E501

        :return: The created_by_client_id of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this WorkflowSignal.

        Client ID of the Origin Request  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def time_created(self):
        """Gets the time_created of this WorkflowSignal.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this WorkflowSignal.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this WorkflowSignal.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this WorkflowSignal.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this WorkflowSignal.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this WorkflowSignal.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this WorkflowSignal.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this WorkflowSignal.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowSignal.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowSignal.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this WorkflowSignal.  # noqa: E501

        User that modified the resource  # noqa: E501

        :return: The modified_by of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this WorkflowSignal.

        User that modified the resource  # noqa: E501

        :param modified_by: The modified_by of this WorkflowSignal.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def tenant_id(self):
        """Gets the tenant_id of this WorkflowSignal.  # noqa: E501

        Tenant ID the resource belongs to  # noqa: E501

        :return: The tenant_id of this WorkflowSignal.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this WorkflowSignal.

        Tenant ID the resource belongs to  # noqa: E501

        :param tenant_id: The tenant_id of this WorkflowSignal.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) > 255):
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 0):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def acl(self):
        """Gets the acl of this WorkflowSignal.  # noqa: E501

        Access control list of the resource  # noqa: E501

        :return: The acl of this WorkflowSignal.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this WorkflowSignal.

        Access control list of the resource  # noqa: E501

        :param acl: The acl of this WorkflowSignal.  # noqa: E501
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
        if not isinstance(other, WorkflowSignal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowSignal):
            return True

        return self.to_dict() != other.to_dict()
