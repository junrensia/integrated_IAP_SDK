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


class Genome(object):
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
        'name': 'str',
        'display_name': 'str',
        'order': 'int',
        'organization': 'str',
        'description': 'str',
        'status': 'str',
        'species': 'str',
        'source': 'str',
        'build': 'str',
        'dragen_version': 'str',
        'data_location_urn': 'str',
        'genome_format': 'str',
        'settings': 'object',
        'source_file_metadata': 'object',
        'fasta_file_urn': 'str',
        'is_application_specific': 'bool',
        'is_illumina': 'bool',
        'checksum': 'str',
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
        'name': 'name',
        'display_name': 'displayName',
        'order': 'order',
        'organization': 'organization',
        'description': 'description',
        'status': 'status',
        'species': 'species',
        'source': 'source',
        'build': 'build',
        'dragen_version': 'dragenVersion',
        'data_location_urn': 'dataLocationUrn',
        'genome_format': 'genomeFormat',
        'settings': 'settings',
        'source_file_metadata': 'sourceFileMetadata',
        'fasta_file_urn': 'fastaFileUrn',
        'is_application_specific': 'isApplicationSpecific',
        'is_illumina': 'isIllumina',
        'checksum': 'checksum',
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

    def __init__(self, id=None, urn=None, href=None, name=None, display_name=None, order=None, organization=None, description=None, status=None, species=None, source=None, build=None, dragen_version=None, data_location_urn=None, genome_format=None, settings=None, source_file_metadata=None, fasta_file_urn=None, is_application_specific=None, is_illumina=None, checksum=None, sub_tenant_id=None, acl=None, tenant_id=None, tenant_name=None, created_by_client_id=None, created_by=None, modified_by=None, time_created=None, time_modified=None, local_vars_configuration=None):  # noqa: E501
        """Genome - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._urn = None
        self._href = None
        self._name = None
        self._display_name = None
        self._order = None
        self._organization = None
        self._description = None
        self._status = None
        self._species = None
        self._source = None
        self._build = None
        self._dragen_version = None
        self._data_location_urn = None
        self._genome_format = None
        self._settings = None
        self._source_file_metadata = None
        self._fasta_file_urn = None
        self._is_application_specific = None
        self._is_illumina = None
        self._checksum = None
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
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if order is not None:
            self.order = order
        if organization is not None:
            self.organization = organization
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if species is not None:
            self.species = species
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build
        if dragen_version is not None:
            self.dragen_version = dragen_version
        if data_location_urn is not None:
            self.data_location_urn = data_location_urn
        if genome_format is not None:
            self.genome_format = genome_format
        if settings is not None:
            self.settings = settings
        if source_file_metadata is not None:
            self.source_file_metadata = source_file_metadata
        if fasta_file_urn is not None:
            self.fasta_file_urn = fasta_file_urn
        if is_application_specific is not None:
            self.is_application_specific = is_application_specific
        if is_illumina is not None:
            self.is_illumina = is_illumina
        if checksum is not None:
            self.checksum = checksum
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
        """Gets the id of this Genome.  # noqa: E501

        Unique object ID  # noqa: E501

        :return: The id of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Genome.

        Unique object ID  # noqa: E501

        :param id: The id of this Genome.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this Genome.  # noqa: E501

        URN of the object  # noqa: E501

        :return: The urn of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this Genome.

        URN of the object  # noqa: E501

        :param urn: The urn of this Genome.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this Genome.  # noqa: E501

        HREF to the object  # noqa: E501

        :return: The href of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Genome.

        HREF to the object  # noqa: E501

        :param href: The href of this Genome.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this Genome.  # noqa: E501

        Name of the genome  # noqa: E501

        :return: The name of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Genome.

        Name of the genome  # noqa: E501

        :param name: The name of this Genome.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Genome.  # noqa: E501

        DisplayName of the genome  # noqa: E501

        :return: The display_name of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Genome.

        DisplayName of the genome  # noqa: E501

        :param display_name: The display_name of this Genome.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def order(self):
        """Gets the order of this Genome.  # noqa: E501

        Order of the genome  # noqa: E501

        :return: The order of this Genome.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Genome.

        Order of the genome  # noqa: E501

        :param order: The order of this Genome.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def organization(self):
        """Gets the organization of this Genome.  # noqa: E501

        Organization of the genome, Require gss.genomes.admin scope to set Organization to a value containing  Illumina (case-insensitive)  # noqa: E501

        :return: The organization of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Genome.

        Organization of the genome, Require gss.genomes.admin scope to set Organization to a value containing  Illumina (case-insensitive)  # noqa: E501

        :param organization: The organization of this Genome.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def description(self):
        """Gets the description of this Genome.  # noqa: E501

        Description of the genome  # noqa: E501

        :return: The description of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Genome.

        Description of the genome  # noqa: E501

        :param description: The description of this Genome.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Genome.  # noqa: E501

        Status of the genome  # noqa: E501

        :return: The status of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Genome.

        Status of the genome  # noqa: E501

        :param status: The status of this Genome.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def species(self):
        """Gets the species of this Genome.  # noqa: E501

        Species of the genome  # noqa: E501

        :return: The species of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this Genome.

        Species of the genome  # noqa: E501

        :param species: The species of this Genome.  # noqa: E501
        :type: str
        """

        self._species = species

    @property
    def source(self):
        """Gets the source of this Genome.  # noqa: E501

        Source of the genome  # noqa: E501

        :return: The source of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Genome.

        Source of the genome  # noqa: E501

        :param source: The source of this Genome.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def build(self):
        """Gets the build of this Genome.  # noqa: E501

        Build of the genome  # noqa: E501

        :return: The build of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this Genome.

        Build of the genome  # noqa: E501

        :param build: The build of this Genome.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def dragen_version(self):
        """Gets the dragen_version of this Genome.  # noqa: E501

        Dragen version for the genome, it is required when Illumina.GenomicSequencingService.Models.V1.GenomeCompact.GenomeFormat is Dragen  # noqa: E501

        :return: The dragen_version of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._dragen_version

    @dragen_version.setter
    def dragen_version(self, dragen_version):
        """Sets the dragen_version of this Genome.

        Dragen version for the genome, it is required when Illumina.GenomicSequencingService.Models.V1.GenomeCompact.GenomeFormat is Dragen  # noqa: E501

        :param dragen_version: The dragen_version of this Genome.  # noqa: E501
        :type: str
        """

        self._dragen_version = dragen_version

    @property
    def data_location_urn(self):
        """Gets the data_location_urn of this Genome.  # noqa: E501

        Urn of the file in GDS containing the genome data file  # noqa: E501

        :return: The data_location_urn of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._data_location_urn

    @data_location_urn.setter
    def data_location_urn(self, data_location_urn):
        """Sets the data_location_urn of this Genome.

        Urn of the file in GDS containing the genome data file  # noqa: E501

        :param data_location_urn: The data_location_urn of this Genome.  # noqa: E501
        :type: str
        """

        self._data_location_urn = data_location_urn

    @property
    def genome_format(self):
        """Gets the genome_format of this Genome.  # noqa: E501

        Format for the genome file, Illumina.GenomicSequencingService.Models.V1.GenomeCompact.DragenVersion is required when it is Dragen  # noqa: E501

        :return: The genome_format of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._genome_format

    @genome_format.setter
    def genome_format(self, genome_format):
        """Sets the genome_format of this Genome.

        Format for the genome file, Illumina.GenomicSequencingService.Models.V1.GenomeCompact.DragenVersion is required when it is Dragen  # noqa: E501

        :param genome_format: The genome_format of this Genome.  # noqa: E501
        :type: str
        """

        self._genome_format = genome_format

    @property
    def settings(self):
        """Gets the settings of this Genome.  # noqa: E501

        Custom settings for the genome  # noqa: E501

        :return: The settings of this Genome.  # noqa: E501
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Genome.

        Custom settings for the genome  # noqa: E501

        :param settings: The settings of this Genome.  # noqa: E501
        :type: object
        """

        self._settings = settings

    @property
    def source_file_metadata(self):
        """Gets the source_file_metadata of this Genome.  # noqa: E501

        Key-value pairs that indicate the source files for the specific genome  # noqa: E501

        :return: The source_file_metadata of this Genome.  # noqa: E501
        :rtype: object
        """
        return self._source_file_metadata

    @source_file_metadata.setter
    def source_file_metadata(self, source_file_metadata):
        """Sets the source_file_metadata of this Genome.

        Key-value pairs that indicate the source files for the specific genome  # noqa: E501

        :param source_file_metadata: The source_file_metadata of this Genome.  # noqa: E501
        :type: object
        """

        self._source_file_metadata = source_file_metadata

    @property
    def fasta_file_urn(self):
        """Gets the fasta_file_urn of this Genome.  # noqa: E501

        The Fasta file Urn being used by the genome  # noqa: E501

        :return: The fasta_file_urn of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._fasta_file_urn

    @fasta_file_urn.setter
    def fasta_file_urn(self, fasta_file_urn):
        """Sets the fasta_file_urn of this Genome.

        The Fasta file Urn being used by the genome  # noqa: E501

        :param fasta_file_urn: The fasta_file_urn of this Genome.  # noqa: E501
        :type: str
        """

        self._fasta_file_urn = fasta_file_urn

    @property
    def is_application_specific(self):
        """Gets the is_application_specific of this Genome.  # noqa: E501

        Whether the genome is application specific  # noqa: E501

        :return: The is_application_specific of this Genome.  # noqa: E501
        :rtype: bool
        """
        return self._is_application_specific

    @is_application_specific.setter
    def is_application_specific(self, is_application_specific):
        """Sets the is_application_specific of this Genome.

        Whether the genome is application specific  # noqa: E501

        :param is_application_specific: The is_application_specific of this Genome.  # noqa: E501
        :type: bool
        """

        self._is_application_specific = is_application_specific

    @property
    def is_illumina(self):
        """Gets the is_illumina of this Genome.  # noqa: E501

        Whether the genome is belonging to Illumina  # noqa: E501

        :return: The is_illumina of this Genome.  # noqa: E501
        :rtype: bool
        """
        return self._is_illumina

    @is_illumina.setter
    def is_illumina(self, is_illumina):
        """Sets the is_illumina of this Genome.

        Whether the genome is belonging to Illumina  # noqa: E501

        :param is_illumina: The is_illumina of this Genome.  # noqa: E501
        :type: bool
        """

        self._is_illumina = is_illumina

    @property
    def checksum(self):
        """Gets the checksum of this Genome.  # noqa: E501

        Stores the checksum of Genome  # noqa: E501

        :return: The checksum of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this Genome.

        Stores the checksum of Genome  # noqa: E501

        :param checksum: The checksum of this Genome.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this Genome.  # noqa: E501

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :return: The sub_tenant_id of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this Genome.

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this Genome.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def acl(self):
        """Gets the acl of this Genome.  # noqa: E501

        Access control list of the object  # noqa: E501

        :return: The acl of this Genome.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this Genome.

        Access control list of the object  # noqa: E501

        :param acl: The acl of this Genome.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Genome.  # noqa: E501

        Unique identifier for the resource tenant  # noqa: E501

        :return: The tenant_id of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Genome.

        Unique identifier for the resource tenant  # noqa: E501

        :param tenant_id: The tenant_id of this Genome.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this Genome.  # noqa: E501

        Unique tenant name for the resource tenant  # noqa: E501

        :return: The tenant_name of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this Genome.

        Unique tenant name for the resource tenant  # noqa: E501

        :param tenant_name: The tenant_name of this Genome.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this Genome.  # noqa: E501

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :return: The created_by_client_id of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this Genome.

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this Genome.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def created_by(self):
        """Gets the created_by of this Genome.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Genome.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this Genome.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this Genome.  # noqa: E501

        User that last modified the resource  # noqa: E501

        :return: The modified_by of this Genome.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Genome.

        User that last modified the resource  # noqa: E501

        :param modified_by: The modified_by of this Genome.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def time_created(self):
        """Gets the time_created of this Genome.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this Genome.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this Genome.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this Genome.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this Genome.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this Genome.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this Genome.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this Genome.  # noqa: E501
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
        if not isinstance(other, Genome):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Genome):
            return True

        return self.to_dict() != other.to_dict()
