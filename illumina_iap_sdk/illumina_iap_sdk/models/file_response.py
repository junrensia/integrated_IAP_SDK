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


class FileResponse(object):
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
        'name': 'str',
        'volume_id': 'str',
        'volume_name': 'str',
        'type': 'str',
        'tenant_id': 'str',
        'sub_tenant_id': 'str',
        'path': 'str',
        'time_created': 'datetime',
        'created_by': 'str',
        'time_modified': 'datetime',
        'modified_by': 'str',
        'inherited_acl': 'list[str]',
        'urn': 'str',
        'size_in_bytes': 'int',
        'metadata': 'object',
        'is_uploaded': 'bool',
        'archive_status': 'ArchiveStatuses',
        'time_archived': 'datetime',
        'storage_tier': 'StorageTier',
        'e_tag': 'str',
        'presigned_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'volume_id': 'volumeId',
        'volume_name': 'volumeName',
        'type': 'type',
        'tenant_id': 'tenantId',
        'sub_tenant_id': 'subTenantId',
        'path': 'path',
        'time_created': 'timeCreated',
        'created_by': 'createdBy',
        'time_modified': 'timeModified',
        'modified_by': 'modifiedBy',
        'inherited_acl': 'inheritedAcl',
        'urn': 'urn',
        'size_in_bytes': 'sizeInBytes',
        'metadata': 'metadata',
        'is_uploaded': 'isUploaded',
        'archive_status': 'archiveStatus',
        'time_archived': 'timeArchived',
        'storage_tier': 'storageTier',
        'e_tag': 'eTag',
        'presigned_url': 'presignedUrl'
    }

    def __init__(self, id=None, name=None, volume_id=None, volume_name=None, type=None, tenant_id=None, sub_tenant_id=None, path=None, time_created=None, created_by=None, time_modified=None, modified_by=None, inherited_acl=None, urn=None, size_in_bytes=None, metadata=None, is_uploaded=None, archive_status=None, time_archived=None, storage_tier=None, e_tag=None, presigned_url=None, local_vars_configuration=None):  # noqa: E501
        """FileResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._volume_id = None
        self._volume_name = None
        self._type = None
        self._tenant_id = None
        self._sub_tenant_id = None
        self._path = None
        self._time_created = None
        self._created_by = None
        self._time_modified = None
        self._modified_by = None
        self._inherited_acl = None
        self._urn = None
        self._size_in_bytes = None
        self._metadata = None
        self._is_uploaded = None
        self._archive_status = None
        self._time_archived = None
        self._storage_tier = None
        self._e_tag = None
        self._presigned_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if volume_id is not None:
            self.volume_id = volume_id
        if volume_name is not None:
            self.volume_name = volume_name
        if type is not None:
            self.type = type
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if sub_tenant_id is not None:
            self.sub_tenant_id = sub_tenant_id
        if path is not None:
            self.path = path
        if time_created is not None:
            self.time_created = time_created
        if created_by is not None:
            self.created_by = created_by
        if time_modified is not None:
            self.time_modified = time_modified
        if modified_by is not None:
            self.modified_by = modified_by
        if inherited_acl is not None:
            self.inherited_acl = inherited_acl
        if urn is not None:
            self.urn = urn
        if size_in_bytes is not None:
            self.size_in_bytes = size_in_bytes
        if metadata is not None:
            self.metadata = metadata
        if is_uploaded is not None:
            self.is_uploaded = is_uploaded
        if archive_status is not None:
            self.archive_status = archive_status
        if time_archived is not None:
            self.time_archived = time_archived
        if storage_tier is not None:
            self.storage_tier = storage_tier
        if e_tag is not None:
            self.e_tag = e_tag
        if presigned_url is not None:
            self.presigned_url = presigned_url

    @property
    def id(self):
        """Gets the id of this FileResponse.  # noqa: E501

        A unique identifier for this File  # noqa: E501

        :return: The id of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileResponse.

        A unique identifier for this File  # noqa: E501

        :param id: The id of this FileResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileResponse.  # noqa: E501

        The name of this File  # noqa: E501

        :return: The name of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileResponse.

        The name of this File  # noqa: E501

        :param name: The name of this FileResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this FileResponse.  # noqa: E501

        The unique identifier of the volume where the file resides  # noqa: E501

        :return: The volume_id of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this FileResponse.

        The unique identifier of the volume where the file resides  # noqa: E501

        :param volume_id: The volume_id of this FileResponse.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def volume_name(self):
        """Gets the volume_name of this FileResponse.  # noqa: E501

        The name of the volume where the file resides  # noqa: E501

        :return: The volume_name of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this FileResponse.

        The name of the volume where the file resides  # noqa: E501

        :param volume_name: The volume_name of this FileResponse.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def type(self):
        """Gets the type of this FileResponse.  # noqa: E501

        The type of the File  # noqa: E501

        :return: The type of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileResponse.

        The type of the File  # noqa: E501

        :param type: The type of this FileResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this FileResponse.  # noqa: E501

        The unique identifier for this File's Tenant  # noqa: E501

        :return: The tenant_id of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this FileResponse.

        The unique identifier for this File's Tenant  # noqa: E501

        :param tenant_id: The tenant_id of this FileResponse.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this FileResponse.  # noqa: E501

        The unique identifier for this File's Sub Tenant  # noqa: E501

        :return: The sub_tenant_id of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this FileResponse.

        The unique identifier for this File's Sub Tenant  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this FileResponse.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def path(self):
        """Gets the path of this FileResponse.  # noqa: E501

        The (GDS) path to this File  # noqa: E501

        :return: The path of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileResponse.

        The (GDS) path to this File  # noqa: E501

        :param path: The path of this FileResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def time_created(self):
        """Gets the time_created of this FileResponse.  # noqa: E501

        The date & time this File was created, in GDS  # noqa: E501

        :return: The time_created of this FileResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this FileResponse.

        The date & time this File was created, in GDS  # noqa: E501

        :param time_created: The time_created of this FileResponse.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def created_by(self):
        """Gets the created_by of this FileResponse.  # noqa: E501

        The creator of this File  # noqa: E501

        :return: The created_by of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FileResponse.

        The creator of this File  # noqa: E501

        :param created_by: The created_by of this FileResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def time_modified(self):
        """Gets the time_modified of this FileResponse.  # noqa: E501

        The date & time this File was updated, in GDS  # noqa: E501

        :return: The time_modified of this FileResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this FileResponse.

        The date & time this File was updated, in GDS  # noqa: E501

        :param time_modified: The time_modified of this FileResponse.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def modified_by(self):
        """Gets the modified_by of this FileResponse.  # noqa: E501

        The updator of this File  # noqa: E501

        :return: The modified_by of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this FileResponse.

        The updator of this File  # noqa: E501

        :param modified_by: The modified_by of this FileResponse.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def inherited_acl(self):
        """Gets the inherited_acl of this FileResponse.  # noqa: E501

        The inherited list of Id(s) that have access to this File  # noqa: E501

        :return: The inherited_acl of this FileResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._inherited_acl

    @inherited_acl.setter
    def inherited_acl(self, inherited_acl):
        """Sets the inherited_acl of this FileResponse.

        The inherited list of Id(s) that have access to this File  # noqa: E501

        :param inherited_acl: The inherited_acl of this FileResponse.  # noqa: E501
        :type: list[str]
        """

        self._inherited_acl = inherited_acl

    @property
    def urn(self):
        """Gets the urn of this FileResponse.  # noqa: E501

        The Universal Resource Name, unique to this File  # noqa: E501

        :return: The urn of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this FileResponse.

        The Universal Resource Name, unique to this File  # noqa: E501

        :param urn: The urn of this FileResponse.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def size_in_bytes(self):
        """Gets the size_in_bytes of this FileResponse.  # noqa: E501

        The File's Size in bytes  # noqa: E501

        :return: The size_in_bytes of this FileResponse.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """Sets the size_in_bytes of this FileResponse.

        The File's Size in bytes  # noqa: E501

        :param size_in_bytes: The size_in_bytes of this FileResponse.  # noqa: E501
        :type: int
        """

        self._size_in_bytes = size_in_bytes

    @property
    def metadata(self):
        """Gets the metadata of this FileResponse.  # noqa: E501

        Metadata about this File  # noqa: E501

        :return: The metadata of this FileResponse.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FileResponse.

        Metadata about this File  # noqa: E501

        :param metadata: The metadata of this FileResponse.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def is_uploaded(self):
        """Gets the is_uploaded of this FileResponse.  # noqa: E501

        The current upload state of the File  # noqa: E501

        :return: The is_uploaded of this FileResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_uploaded

    @is_uploaded.setter
    def is_uploaded(self, is_uploaded):
        """Sets the is_uploaded of this FileResponse.

        The current upload state of the File  # noqa: E501

        :param is_uploaded: The is_uploaded of this FileResponse.  # noqa: E501
        :type: bool
        """

        self._is_uploaded = is_uploaded

    @property
    def archive_status(self):
        """Gets the archive_status of this FileResponse.  # noqa: E501


        :return: The archive_status of this FileResponse.  # noqa: E501
        :rtype: ArchiveStatuses
        """
        return self._archive_status

    @archive_status.setter
    def archive_status(self, archive_status):
        """Sets the archive_status of this FileResponse.


        :param archive_status: The archive_status of this FileResponse.  # noqa: E501
        :type: ArchiveStatuses
        """

        self._archive_status = archive_status

    @property
    def time_archived(self):
        """Gets the time_archived of this FileResponse.  # noqa: E501

        The date & time this File was archived  # noqa: E501

        :return: The time_archived of this FileResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_archived

    @time_archived.setter
    def time_archived(self, time_archived):
        """Sets the time_archived of this FileResponse.

        The date & time this File was archived  # noqa: E501

        :param time_archived: The time_archived of this FileResponse.  # noqa: E501
        :type: datetime
        """

        self._time_archived = time_archived

    @property
    def storage_tier(self):
        """Gets the storage_tier of this FileResponse.  # noqa: E501


        :return: The storage_tier of this FileResponse.  # noqa: E501
        :rtype: StorageTier
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """Sets the storage_tier of this FileResponse.


        :param storage_tier: The storage_tier of this FileResponse.  # noqa: E501
        :type: StorageTier
        """

        self._storage_tier = storage_tier

    @property
    def e_tag(self):
        """Gets the e_tag of this FileResponse.  # noqa: E501

        The File's ETag  # noqa: E501

        :return: The e_tag of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        """Sets the e_tag of this FileResponse.

        The File's ETag  # noqa: E501

        :param e_tag: The e_tag of this FileResponse.  # noqa: E501
        :type: str
        """

        self._e_tag = e_tag

    @property
    def presigned_url(self):
        """Gets the presigned_url of this FileResponse.  # noqa: E501

        The presigned Url allowing access to this File  # noqa: E501

        :return: The presigned_url of this FileResponse.  # noqa: E501
        :rtype: str
        """
        return self._presigned_url

    @presigned_url.setter
    def presigned_url(self, presigned_url):
        """Sets the presigned_url of this FileResponse.

        The presigned Url allowing access to this File  # noqa: E501

        :param presigned_url: The presigned_url of this FileResponse.  # noqa: E501
        :type: str
        """

        self._presigned_url = presigned_url

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
        if not isinstance(other, FileResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileResponse):
            return True

        return self.to_dict() != other.to_dict()
