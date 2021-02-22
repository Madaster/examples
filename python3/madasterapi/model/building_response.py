"""
    Madaster Private API - Build: 

    Welcome to the **Madaster Private API** endpoint. This endpoint can be used to interact with the Madaster Platform and its resources. This API does not fully cover all functionality of the platform yet, please see below for the available functions and what they can be used for. For detailed information about the platform and this API, please refer to the [Madaster Documentation](https://docs.madaster.com) or the [Madaster API Documentation](https://docs.madaster.com/api).<br/><br/>To access these resources, you need an authorization token. If you do not have one yet, see the chapter about Authorization in the [API documentation](https://docs.madaster.com/api). This token should be sent as a header with the name 'X-API-Key', which will authenticate the request with the token. The documentation below specifies which requests are available and which responses they might produce.<br/><br/>This API can be reached at the endpoint: **[https://api.madaster.com/](https://api.madaster.com/)**<br/>The interactive Swagger/OpenAPI documentation can be found at: **[https://api.madaster.com/](https://api.madaster.com/)**<br/>If you prefer a static documentation: **[https://docs.madaster.com/api-docs](https://docs.madaster.com/api-docs)**  # noqa: E501

    The version of the OpenAPI document: v3.0
    Contact: service@madaster.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from madasterapi.model_utils import (  # noqa: F401
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


class BuildingResponse(ModelNormal):
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
    }

    validations = {
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
            'id': (str,),  # noqa: E501
            'folder_id': (str,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'cadastral_designation': (str, none_type,),  # noqa: E501
            'cadastral_area': (int,),  # noqa: E501
            'parcelnumber': (str, none_type,),  # noqa: E501
            'public_law_restriction': (str, none_type,),  # noqa: E501
            'completion_date': (datetime,),  # noqa: E501
            'last_renovation_date': (datetime,),  # noqa: E501
            'address_street': (str, none_type,),  # noqa: E501
            'address_housenumber': (str, none_type,),  # noqa: E501
            'address_housenumber_addition': (str, none_type,),  # noqa: E501
            'address_zipcode': (str, none_type,),  # noqa: E501
            'address_city': (str, none_type,),  # noqa: E501
            'address_country': (str, none_type,),  # noqa: E501
            'building_usage': (str, none_type,),  # noqa: E501
            'gross_surface_area': (float,),  # noqa: E501
            'energy_label': (str, none_type,),  # noqa: E501
            'beng1': (float, none_type,),  # noqa: E501
            'beng2': (float, none_type,),  # noqa: E501
            'beng3': (float, none_type,),  # noqa: E501
            'rto': (float, none_type,),  # noqa: E501
            'energy_index': (float,),  # noqa: E501
            'expected_lifespan': (int,),  # noqa: E501
            'expected_lifespan_structure': (int,),  # noqa: E501
            'expected_lifespan_skin': (int,),  # noqa: E501
            'expected_lifespan_services': (int,),  # noqa: E501
            'expected_lifespan_space_plan': (int,),  # noqa: E501
            'expected_lifespan_stuff': (int,),  # noqa: E501
            'breeam_label': (int,),  # noqa: E501
            'gpr_score_energy': (float, none_type,),  # noqa: E501
            'gpr_score_health': (float, none_type,),  # noqa: E501
            'gpr_score_future_value': (float, none_type,),  # noqa: E501
            'gpr_score_usage_quality': (float, none_type,),  # noqa: E501
            'gpr_score_environment': (float, none_type,),  # noqa: E501
            'mpg_label': (float,),  # noqa: E501
            'mpg_label_manual': (float,),  # noqa: E501
            'mpg_label_indicative': (float,),  # noqa: E501
            'leed_label': (str, none_type,),  # noqa: E501
            'well_score_building': (int,),  # noqa: E501
            'well_score_interior': (int,),  # noqa: E501
            'well_score_core_and_shell': (int,),  # noqa: E501
            'is_dirty': (bool,),  # noqa: E501
            'has_dirty_elements': (bool,),  # noqa: E501
            'most_recent_bim_info': (datetime,),  # noqa: E501
            'geo_latitude': (float,),  # noqa: E501
            'geo_longtitude': (float,),  # noqa: E501
            'phase_type': (str,),  # noqa: E501
            'classification_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'folder_id': 'folderId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'cadastral_designation': 'cadastralDesignation',  # noqa: E501
        'cadastral_area': 'cadastralArea',  # noqa: E501
        'parcelnumber': 'parcelnumber',  # noqa: E501
        'public_law_restriction': 'publicLawRestriction',  # noqa: E501
        'completion_date': 'completionDate',  # noqa: E501
        'last_renovation_date': 'lastRenovationDate',  # noqa: E501
        'address_street': 'addressStreet',  # noqa: E501
        'address_housenumber': 'addressHousenumber',  # noqa: E501
        'address_housenumber_addition': 'addressHousenumberAddition',  # noqa: E501
        'address_zipcode': 'addressZipcode',  # noqa: E501
        'address_city': 'addressCity',  # noqa: E501
        'address_country': 'addressCountry',  # noqa: E501
        'building_usage': 'buildingUsage',  # noqa: E501
        'gross_surface_area': 'grossSurfaceArea',  # noqa: E501
        'energy_label': 'energyLabel',  # noqa: E501
        'beng1': 'beng1',  # noqa: E501
        'beng2': 'beng2',  # noqa: E501
        'beng3': 'beng3',  # noqa: E501
        'rto': 'rto',  # noqa: E501
        'energy_index': 'energyIndex',  # noqa: E501
        'expected_lifespan': 'expectedLifespan',  # noqa: E501
        'expected_lifespan_structure': 'expectedLifespanStructure',  # noqa: E501
        'expected_lifespan_skin': 'expectedLifespanSkin',  # noqa: E501
        'expected_lifespan_services': 'expectedLifespanServices',  # noqa: E501
        'expected_lifespan_space_plan': 'expectedLifespanSpacePlan',  # noqa: E501
        'expected_lifespan_stuff': 'expectedLifespanStuff',  # noqa: E501
        'breeam_label': 'breeamLabel',  # noqa: E501
        'gpr_score_energy': 'gprScoreEnergy',  # noqa: E501
        'gpr_score_health': 'gprScoreHealth',  # noqa: E501
        'gpr_score_future_value': 'gprScoreFutureValue',  # noqa: E501
        'gpr_score_usage_quality': 'gprScoreUsageQuality',  # noqa: E501
        'gpr_score_environment': 'gprScoreEnvironment',  # noqa: E501
        'mpg_label': 'mpgLabel',  # noqa: E501
        'mpg_label_manual': 'mpgLabelManual',  # noqa: E501
        'mpg_label_indicative': 'mpgLabelIndicative',  # noqa: E501
        'leed_label': 'leedLabel',  # noqa: E501
        'well_score_building': 'wellScoreBuilding',  # noqa: E501
        'well_score_interior': 'wellScoreInterior',  # noqa: E501
        'well_score_core_and_shell': 'wellScoreCoreAndShell',  # noqa: E501
        'is_dirty': 'isDirty',  # noqa: E501
        'has_dirty_elements': 'hasDirtyElements',  # noqa: E501
        'most_recent_bim_info': 'mostRecentBimInfo',  # noqa: E501
        'geo_latitude': 'geoLatitude',  # noqa: E501
        'geo_longtitude': 'geoLongtitude',  # noqa: E501
        'phase_type': 'phaseType',  # noqa: E501
        'classification_type': 'classificationType',  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """BuildingResponse - a model defined in OpenAPI

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
            id (str): The identifier of the building. [optional]  # noqa: E501
            folder_id (str): The identifier of the parent folder. [optional]  # noqa: E501
            name (str, none_type): The name of the building. [optional]  # noqa: E501
            cadastral_designation (str, none_type): The cadastral designation of the building. [optional]  # noqa: E501
            cadastral_area (int): The cadastral area of the building in square meters. [optional]  # noqa: E501
            parcelnumber (str, none_type): The parcel number of the building. [optional]  # noqa: E501
            public_law_restriction (str, none_type): The restrictions of public law in place for the building. [optional]  # noqa: E501
            completion_date (datetime): The completion date of the building. [optional]  # noqa: E501
            last_renovation_date (datetime): The last renovation date of the building. [optional]  # noqa: E501
            address_street (str, none_type): The street that the building is situated on. [optional]  # noqa: E501
            address_housenumber (str, none_type): The housenumber in the street that the building is situated on. [optional]  # noqa: E501
            address_housenumber_addition (str, none_type): The addition of the housenumber in the street that the building is situated on. [optional]  # noqa: E501
            address_zipcode (str, none_type): The zipcode of the location that the building is situated on. [optional]  # noqa: E501
            address_city (str, none_type): The city that the building is situated in. [optional]  # noqa: E501
            address_country (str, none_type): The identifier of the country that the building is situated in. [optional]  # noqa: E501
            building_usage (str, none_type): The current designation of the building. [optional]  # noqa: E501
            gross_surface_area (float): The gross surface area of the building. [optional]  # noqa: E501
            energy_label (str, none_type): The current energy label of the building. [optional]  # noqa: E501
            beng1 (float, none_type): Energiebehoefte (BENG 1) - kWh/m2.jr. [optional]  # noqa: E501
            beng2 (float, none_type): Primaire fossiele energie (BENG 2) - kWh/m2.jr. [optional]  # noqa: E501
            beng3 (float, none_type): Hernieuwbare energie (BENG 3) - %. [optional]  # noqa: E501
            rto (float, none_type): Risico temperatuuroverschrijding (T0-juli). [optional]  # noqa: E501
            energy_index (float): The energy index. [optional]  # noqa: E501
            expected_lifespan (int): The expected lifespan for the building. [optional]  # noqa: E501
            expected_lifespan_structure (int): The expected lifespan building for the structure brand layer. [optional]  # noqa: E501
            expected_lifespan_skin (int): The expected lifespan building for the skin brand layer. [optional]  # noqa: E501
            expected_lifespan_services (int): The expected lifespan for the services brand layer. [optional]  # noqa: E501
            expected_lifespan_space_plan (int): The expected lifespan for the space plan brand layer. [optional]  # noqa: E501
            expected_lifespan_stuff (int): The expected lifespan for the stuff brand layer. [optional]  # noqa: E501
            breeam_label (int): The BREEAM label. [optional]  # noqa: E501
            gpr_score_energy (float, none_type): The GPR-energy score of the building. [optional]  # noqa: E501
            gpr_score_health (float, none_type): The GPR-health score of the building. [optional]  # noqa: E501
            gpr_score_future_value (float, none_type): The GPR-future score of the building. [optional]  # noqa: E501
            gpr_score_usage_quality (float, none_type): The GPR-usage quality score of the building. [optional]  # noqa: E501
            gpr_score_environment (float, none_type): The GPR-environment score of the building. [optional]  # noqa: E501
            mpg_label (float): The MPG-score of the building. [optional]  # noqa: E501
            mpg_label_manual (float): The manual MPG-score of the building. [optional]  # noqa: E501
            mpg_label_indicative (float): The indicative MPG-score of the building. [optional]  # noqa: E501
            leed_label (str, none_type): The LEED label of the building. [optional]  # noqa: E501
            well_score_building (int): The WELL score of the building. [optional]  # noqa: E501
            well_score_interior (int): The WELL score of the interior. [optional]  # noqa: E501
            well_score_core_and_shell (int): The WELL score of the core and shell. [optional]  # noqa: E501
            is_dirty (bool): Indicates whether this building is dirty and thus contains data that should be updated. [optional]  # noqa: E501
            has_dirty_elements (bool): Indicates whether the building contains any elements that have changed. [optional]  # noqa: E501
            most_recent_bim_info (datetime): The time of the most recent BIM info change. [optional]  # noqa: E501
            geo_latitude (float): The geo latitude of the building. [optional]  # noqa: E501
            geo_longtitude (float): The geo longtitude of the building. [optional]  # noqa: E501
            phase_type (str): The identifier of the phase type of the buildinge. [optional]  # noqa: E501
            classification_type (str): The identifier of the building classification type of the buildinge. [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
