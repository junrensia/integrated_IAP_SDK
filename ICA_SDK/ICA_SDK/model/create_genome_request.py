"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ICA_SDK.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class CreateGenomeRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('genome_format',): {
            'DRAGEN': "Dragen",
            'FASTA': "Fasta",
        },
        ('status',): {
            'ACTIVE': "Active",
            'INACTIVE': "Inactive",
        },
    }

    validations = {
        ('name',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('display_name',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('order',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('build',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('organization',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('description',): {
            'max_length': 8192,
            'min_length': 0,
        },
        ('species',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('source',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('dragen_version',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('data_location_urn',): {
            'max_length': 1152,
            'min_length': 0,
        },
        ('fasta_file_urn',): {
            'max_length': 1152,
            'min_length': 0,
        },
        ('checksum',): {
            'max_length': 255,
            'min_length': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'name': (str,),  # noqa: E501
            'genome_format': (str,),  # noqa: E501
            'acl': ([str],),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'order': (int,),  # noqa: E501
            'is_application_specific': (bool,),  # noqa: E501
            'build': (str,),  # noqa: E501
            'organization': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'species': (str,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'dragen_version': (str,),  # noqa: E501
            'data_location_urn': (str,),  # noqa: E501
            'settings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'source_file_metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'fasta_file_urn': (str,),  # noqa: E501
            'checksum': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'genome_format': 'genomeFormat',  # noqa: E501
        'acl': 'acl',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'order': 'order',  # noqa: E501
        'is_application_specific': 'isApplicationSpecific',  # noqa: E501
        'build': 'build',  # noqa: E501
        'organization': 'organization',  # noqa: E501
        'description': 'description',  # noqa: E501
        'status': 'status',  # noqa: E501
        'species': 'species',  # noqa: E501
        'source': 'source',  # noqa: E501
        'dragen_version': 'dragenVersion',  # noqa: E501
        'data_location_urn': 'dataLocationUrn',  # noqa: E501
        'settings': 'settings',  # noqa: E501
        'source_file_metadata': 'sourceFileMetadata',  # noqa: E501
        'fasta_file_urn': 'fastaFileUrn',  # noqa: E501
        'checksum': 'checksum',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, name, genome_format, *args, **kwargs):  # noqa: E501
        """CreateGenomeRequest - a model defined in OpenAPI

        Args:
            name (str): Name of the genome
            genome_format (str): Format for the genome file, Illumina.GenomicSequencingService.Models.Domain.CreateGenomeParameters.DragenVersion is required when it is Dragen

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            acl ([str]): [optional]  # noqa: E501
            display_name (str): DisplayName of the genome. [optional]  # noqa: E501
            order (int): Order of the genome, default is 0. [optional]  # noqa: E501
            is_application_specific (bool): Whether the genome is application specific. [optional]  # noqa: E501
            build (str): Build of the genome. [optional]  # noqa: E501
            organization (str): Organization of the genome. [optional]  # noqa: E501
            description (str): Description of the genome. [optional]  # noqa: E501
            status (str): Status of the genome. [optional]  # noqa: E501
            species (str): Species of the genome. [optional]  # noqa: E501
            source (str): Source of the genome. [optional]  # noqa: E501
            dragen_version (str): Dragen version for the genome, it is required when Illumina.GenomicSequencingService.Models.Domain.CreateGenomeParameters.GenomeFormat is Dragen. [optional]  # noqa: E501
            data_location_urn (str): Urn of the file in GDS containing the genome data file. [optional]  # noqa: E501
            settings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Custom settings for the genome. [optional]  # noqa: E501
            source_file_metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Key-value pairs that indicate the source files for the specific genome. [optional]  # noqa: E501
            fasta_file_urn (str): Urn of the Fasta file being used by the genome. [optional]  # noqa: E501
            checksum (str): Checksum of Genome. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        self.genome_format = genome_format
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
