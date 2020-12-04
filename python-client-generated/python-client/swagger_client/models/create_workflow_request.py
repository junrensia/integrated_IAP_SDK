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


class CreateWorkflowRequest(object):
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
        'name': 'str',
        'description': 'str',
        'organization': 'str',
        'workflow_version': 'CreateWorkflowVersionRequest',
        'tool_class': 'str',
        'acl': 'list[str]',
        'categories': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'organization': 'organization',
        'workflow_version': 'workflowVersion',
        'tool_class': 'toolClass',
        'acl': 'acl',
        'categories': 'categories'
    }

    def __init__(self, name=None, description=None, organization=None, workflow_version=None, tool_class=None, acl=None, categories=None):  # noqa: E501
        """CreateWorkflowRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._organization = None
        self._workflow_version = None
        self._tool_class = None
        self._acl = None
        self._categories = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if organization is not None:
            self.organization = organization
        if workflow_version is not None:
            self.workflow_version = workflow_version
        if tool_class is not None:
            self.tool_class = tool_class
        if acl is not None:
            self.acl = acl
        if categories is not None:
            self.categories = categories

    @property
    def name(self):
        """Gets the name of this CreateWorkflowRequest.  # noqa: E501


        :return: The name of this CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWorkflowRequest.


        :param name: The name of this CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateWorkflowRequest.  # noqa: E501


        :return: The description of this CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateWorkflowRequest.


        :param description: The description of this CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 256:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def organization(self):
        """Gets the organization of this CreateWorkflowRequest.  # noqa: E501


        :return: The organization of this CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this CreateWorkflowRequest.


        :param organization: The organization of this CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        if organization is not None and len(organization) > 255:
            raise ValueError("Invalid value for `organization`, length must be less than or equal to `255`")  # noqa: E501
        if organization is not None and len(organization) < 0:
            raise ValueError("Invalid value for `organization`, length must be greater than or equal to `0`")  # noqa: E501

        self._organization = organization

    @property
    def workflow_version(self):
        """Gets the workflow_version of this CreateWorkflowRequest.  # noqa: E501


        :return: The workflow_version of this CreateWorkflowRequest.  # noqa: E501
        :rtype: CreateWorkflowVersionRequest
        """
        return self._workflow_version

    @workflow_version.setter
    def workflow_version(self, workflow_version):
        """Sets the workflow_version of this CreateWorkflowRequest.


        :param workflow_version: The workflow_version of this CreateWorkflowRequest.  # noqa: E501
        :type: CreateWorkflowVersionRequest
        """

        self._workflow_version = workflow_version

    @property
    def tool_class(self):
        """Gets the tool_class of this CreateWorkflowRequest.  # noqa: E501


        :return: The tool_class of this CreateWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._tool_class

    @tool_class.setter
    def tool_class(self, tool_class):
        """Sets the tool_class of this CreateWorkflowRequest.


        :param tool_class: The tool_class of this CreateWorkflowRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["workflow", "commandLineTool"]  # noqa: E501
        if tool_class not in allowed_values:
            raise ValueError(
                "Invalid value for `tool_class` ({0}), must be one of {1}"  # noqa: E501
                .format(tool_class, allowed_values)
            )

        self._tool_class = tool_class

    @property
    def acl(self):
        """Gets the acl of this CreateWorkflowRequest.  # noqa: E501


        :return: The acl of this CreateWorkflowRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this CreateWorkflowRequest.


        :param acl: The acl of this CreateWorkflowRequest.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def categories(self):
        """Gets the categories of this CreateWorkflowRequest.  # noqa: E501


        :return: The categories of this CreateWorkflowRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CreateWorkflowRequest.


        :param categories: The categories of this CreateWorkflowRequest.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

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
        if issubclass(CreateWorkflowRequest, dict):
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
        if not isinstance(other, CreateWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
