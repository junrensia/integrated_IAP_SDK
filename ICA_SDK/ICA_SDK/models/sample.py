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


class Sample(object):
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
        'analysis_datasets': 'list[AnalysisDatasetCompact]',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'lab_status': 'str',
        'data_aggregation_group': 'str',
        'project_name': 'str',
        'external_id': 'str',
        'sub_tenant_id': 'str',
        'acl': 'list[str]',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'created_by_client_id': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'time_created': 'datetime',
        'time_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'href': 'href',
        'analysis_datasets': 'analysisDatasets',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'lab_status': 'labStatus',
        'data_aggregation_group': 'dataAggregationGroup',
        'project_name': 'projectName',
        'external_id': 'externalId',
        'sub_tenant_id': 'subTenantId',
        'acl': 'acl',
        'tenant_id': 'tenantId',
        'tenant_name': 'tenantName',
        'created_by_client_id': 'createdByClientId',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'time_created': 'timeCreated',
        'time_modified': 'timeModified'
    }

    def __init__(self, id=None, urn=None, href=None, analysis_datasets=None, name=None, description=None, status=None, lab_status=None, data_aggregation_group=None, project_name=None, external_id=None, sub_tenant_id=None, acl=None, tenant_id=None, tenant_name=None, created_by_client_id=None, created_by=None, modified_by=None, time_created=None, time_modified=None, local_vars_configuration=None):  # noqa: E501
        """Sample - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._urn = None
        self._href = None
        self._analysis_datasets = None
        self._name = None
        self._description = None
        self._status = None
        self._lab_status = None
        self._data_aggregation_group = None
        self._project_name = None
        self._external_id = None
        self._sub_tenant_id = None
        self._acl = None
        self._tenant_id = None
        self._tenant_name = None
        self._created_by_client_id = None
        self._created_by = None
        self._modified_by = None
        self._time_created = None
        self._time_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn
        if href is not None:
            self.href = href
        if analysis_datasets is not None:
            self.analysis_datasets = analysis_datasets
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if lab_status is not None:
            self.lab_status = lab_status
        if data_aggregation_group is not None:
            self.data_aggregation_group = data_aggregation_group
        if project_name is not None:
            self.project_name = project_name
        if external_id is not None:
            self.external_id = external_id
        if sub_tenant_id is not None:
            self.sub_tenant_id = sub_tenant_id
        if acl is not None:
            self.acl = acl
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if created_by_client_id is not None:
            self.created_by_client_id = created_by_client_id
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified

    @property
    def id(self):
        """Gets the id of this Sample.  # noqa: E501

        Unique object ID  # noqa: E501

        :return: The id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sample.

        Unique object ID  # noqa: E501

        :param id: The id of this Sample.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this Sample.  # noqa: E501

        URN of the object  # noqa: E501

        :return: The urn of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this Sample.

        URN of the object  # noqa: E501

        :param urn: The urn of this Sample.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this Sample.  # noqa: E501

        HREF to the object  # noqa: E501

        :return: The href of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Sample.

        HREF to the object  # noqa: E501

        :param href: The href of this Sample.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def analysis_datasets(self):
        """Gets the analysis_datasets of this Sample.  # noqa: E501

        Analysis datasets of the sample  # noqa: E501

        :return: The analysis_datasets of this Sample.  # noqa: E501
        :rtype: list[AnalysisDatasetCompact]
        """
        return self._analysis_datasets

    @analysis_datasets.setter
    def analysis_datasets(self, analysis_datasets):
        """Sets the analysis_datasets of this Sample.

        Analysis datasets of the sample  # noqa: E501

        :param analysis_datasets: The analysis_datasets of this Sample.  # noqa: E501
        :type: list[AnalysisDatasetCompact]
        """

        self._analysis_datasets = analysis_datasets

    @property
    def name(self):
        """Gets the name of this Sample.  # noqa: E501

        Name of the sample  # noqa: E501

        :return: The name of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sample.

        Name of the sample  # noqa: E501

        :param name: The name of this Sample.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Sample.  # noqa: E501

        Description of the sample  # noqa: E501

        :return: The description of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Sample.

        Description of the sample  # noqa: E501

        :param description: The description of this Sample.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Sample.  # noqa: E501

        Status of the sample  # noqa: E501

        :return: The status of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Sample.

        Status of the sample  # noqa: E501

        :param status: The status of this Sample.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def lab_status(self):
        """Gets the lab_status of this Sample.  # noqa: E501

        User-customizable value indicating the status of the sample  # noqa: E501

        :return: The lab_status of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._lab_status

    @lab_status.setter
    def lab_status(self, lab_status):
        """Sets the lab_status of this Sample.

        User-customizable value indicating the status of the sample  # noqa: E501

        :param lab_status: The lab_status of this Sample.  # noqa: E501
        :type: str
        """

        self._lab_status = lab_status

    @property
    def data_aggregation_group(self):
        """Gets the data_aggregation_group of this Sample.  # noqa: E501

        Data aggregation group  # noqa: E501

        :return: The data_aggregation_group of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._data_aggregation_group

    @data_aggregation_group.setter
    def data_aggregation_group(self, data_aggregation_group):
        """Sets the data_aggregation_group of this Sample.

        Data aggregation group  # noqa: E501

        :param data_aggregation_group: The data_aggregation_group of this Sample.  # noqa: E501
        :type: str
        """

        self._data_aggregation_group = data_aggregation_group

    @property
    def project_name(self):
        """Gets the project_name of this Sample.  # noqa: E501

        Project Name  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated.  # noqa: E501

        :return: The project_name of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Sample.

        Project Name  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated.  # noqa: E501

        :param project_name: The project_name of this Sample.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def external_id(self):
        """Gets the external_id of this Sample.  # noqa: E501

        Optional external ID associated with the sample  # noqa: E501

        :return: The external_id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Sample.

        Optional external ID associated with the sample  # noqa: E501

        :param external_id: The external_id of this Sample.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this Sample.  # noqa: E501

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :return: The sub_tenant_id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this Sample.

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this Sample.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def acl(self):
        """Gets the acl of this Sample.  # noqa: E501

        Access control list of the object  # noqa: E501

        :return: The acl of this Sample.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this Sample.

        Access control list of the object  # noqa: E501

        :param acl: The acl of this Sample.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Sample.  # noqa: E501

        Unique identifier for the resource tenant  # noqa: E501

        :return: The tenant_id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Sample.

        Unique identifier for the resource tenant  # noqa: E501

        :param tenant_id: The tenant_id of this Sample.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this Sample.  # noqa: E501

        Unique tenant name for the resource tenant  # noqa: E501

        :return: The tenant_name of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this Sample.

        Unique tenant name for the resource tenant  # noqa: E501

        :param tenant_name: The tenant_name of this Sample.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this Sample.  # noqa: E501

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :return: The created_by_client_id of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this Sample.

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this Sample.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def created_by(self):
        """Gets the created_by of this Sample.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Sample.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this Sample.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this Sample.  # noqa: E501

        User that last modified the resource  # noqa: E501

        :return: The modified_by of this Sample.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Sample.

        User that last modified the resource  # noqa: E501

        :param modified_by: The modified_by of this Sample.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def time_created(self):
        """Gets the time_created of this Sample.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this Sample.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this Sample.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this Sample.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this Sample.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this Sample.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this Sample.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this Sample.  # noqa: E501
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
        if not isinstance(other, Sample):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sample):
            return True

        return self.to_dict() != other.to_dict()
