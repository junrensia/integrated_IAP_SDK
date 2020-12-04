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


class WorkflowRunHistoryEvent(object):
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
        'name': 'str',
        'event_id': 'int',
        'previous_event_id': 'int',
        'event_type': 'str',
        'timestamp': 'datetime',
        'event_details': 'object'
    }

    attribute_map = {
        'name': 'name',
        'event_id': 'eventId',
        'previous_event_id': 'previousEventId',
        'event_type': 'eventType',
        'timestamp': 'timestamp',
        'event_details': 'eventDetails'
    }

    def __init__(self, name=None, event_id=None, previous_event_id=None, event_type=None, timestamp=None, event_details=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowRunHistoryEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._event_id = None
        self._previous_event_id = None
        self._event_type = None
        self._timestamp = None
        self._event_details = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if event_id is not None:
            self.event_id = event_id
        if previous_event_id is not None:
            self.previous_event_id = previous_event_id
        if event_type is not None:
            self.event_type = event_type
        if timestamp is not None:
            self.timestamp = timestamp
        if event_details is not None:
            self.event_details = event_details

    @property
    def name(self):
        """Gets the name of this WorkflowRunHistoryEvent.  # noqa: E501

        Name of the event, such as the name of the step/task for state-level events and run name for run-level events  # noqa: E501

        :return: The name of this WorkflowRunHistoryEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowRunHistoryEvent.

        Name of the event, such as the name of the step/task for state-level events and run name for run-level events  # noqa: E501

        :param name: The name of this WorkflowRunHistoryEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def event_id(self):
        """Gets the event_id of this WorkflowRunHistoryEvent.  # noqa: E501

        Identifier for the history event, if any  # noqa: E501

        :return: The event_id of this WorkflowRunHistoryEvent.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this WorkflowRunHistoryEvent.

        Identifier for the history event, if any  # noqa: E501

        :param event_id: The event_id of this WorkflowRunHistoryEvent.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def previous_event_id(self):
        """Gets the previous_event_id of this WorkflowRunHistoryEvent.  # noqa: E501

        Identifier for any previous history event (if available)  # noqa: E501

        :return: The previous_event_id of this WorkflowRunHistoryEvent.  # noqa: E501
        :rtype: int
        """
        return self._previous_event_id

    @previous_event_id.setter
    def previous_event_id(self, previous_event_id):
        """Sets the previous_event_id of this WorkflowRunHistoryEvent.

        Identifier for any previous history event (if available)  # noqa: E501

        :param previous_event_id: The previous_event_id of this WorkflowRunHistoryEvent.  # noqa: E501
        :type: int
        """

        self._previous_event_id = previous_event_id

    @property
    def event_type(self):
        """Gets the event_type of this WorkflowRunHistoryEvent.  # noqa: E501

        Type of history event. The associated details entry will be populated based on the type of event.  # noqa: E501

        :return: The event_type of this WorkflowRunHistoryEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this WorkflowRunHistoryEvent.

        Type of history event. The associated details entry will be populated based on the type of event.  # noqa: E501

        :param event_type: The event_type of this WorkflowRunHistoryEvent.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def timestamp(self):
        """Gets the timestamp of this WorkflowRunHistoryEvent.  # noqa: E501

        Timestamp for the history event  # noqa: E501

        :return: The timestamp of this WorkflowRunHistoryEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WorkflowRunHistoryEvent.

        Timestamp for the history event  # noqa: E501

        :param timestamp: The timestamp of this WorkflowRunHistoryEvent.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def event_details(self):
        """Gets the event_details of this WorkflowRunHistoryEvent.  # noqa: E501

        Details for history event  # noqa: E501

        :return: The event_details of this WorkflowRunHistoryEvent.  # noqa: E501
        :rtype: object
        """
        return self._event_details

    @event_details.setter
    def event_details(self, event_details):
        """Sets the event_details of this WorkflowRunHistoryEvent.

        Details for history event  # noqa: E501

        :param event_details: The event_details of this WorkflowRunHistoryEvent.  # noqa: E501
        :type: object
        """

        self._event_details = event_details

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
        if not isinstance(other, WorkflowRunHistoryEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowRunHistoryEvent):
            return True

        return self.to_dict() != other.to_dict()
