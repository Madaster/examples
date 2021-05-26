"""
    Madaster Private API - Build: 8815

    Welcome to the **Madaster Private API** endpoint. This endpoint can be used to interact with the Madaster Platform and its resources. This API does not fully cover all functionality of the platform yet, please see below for the available functions and what they can be used for. For detailed information about the platform and this API, please refer to the [Madaster Documentation](https://docs.madaster.com) or the [Madaster API Documentation](https://docs.madaster.com/api).<br/><br/>To access these resources, you need an authorization token. If you do not have one yet, see the chapter about Authorization in the [API documentation](https://docs.madaster.com/api). This token should be sent as a header with the name 'X-API-Key', which will authenticate the request with the token. The documentation below specifies which requests are available and which responses they might produce.<br/><br/>This API can be reached at the endpoint: **[https://api.madaster.com/](https://api.madaster.com/)**  # noqa: E501

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


class ProductCircularInformation(ModelNormal):
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
        ('product_reused_percentage_feedstock',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
        },
        ('product_reused_percentage_end_of_life',): {
            'inclusive_maximum': 1,
            'inclusive_minimum': 0,
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
            'product_reused_percentage_feedstock': (float,),  # noqa: E501
            'product_reused_percentage_end_of_life': (float,),  # noqa: E501
            'efficiency_percentage_recycling_feedstock': (float,),  # noqa: E501
            'efficiency_percentage_recycling_end_of_life': (float,),  # noqa: E501
            'product_recycled_percentage_feedstock': (float,),  # noqa: E501
            'product_rapid_renewables_percentage_feedstock': (float,),  # noqa: E501
            'product_virgin_percentage_feedstock': (float,),  # noqa: E501
            'product_recycled_percentage_end_of_life': (float,),  # noqa: E501
            'product_landfill_percentage_end_of_life': (float,),  # noqa: E501
            'product_incineration_percentage_end_of_life': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'product_reused_percentage_feedstock': 'productReusedPercentageFeedstock',  # noqa: E501
        'product_reused_percentage_end_of_life': 'productReusedPercentageEndOfLife',  # noqa: E501
        'efficiency_percentage_recycling_feedstock': 'efficiencyPercentageRecyclingFeedstock',  # noqa: E501
        'efficiency_percentage_recycling_end_of_life': 'efficiencyPercentageRecyclingEndOfLife',  # noqa: E501
        'product_recycled_percentage_feedstock': 'productRecycledPercentageFeedstock',  # noqa: E501
        'product_rapid_renewables_percentage_feedstock': 'productRapidRenewablesPercentageFeedstock',  # noqa: E501
        'product_virgin_percentage_feedstock': 'productVirginPercentageFeedstock',  # noqa: E501
        'product_recycled_percentage_end_of_life': 'productRecycledPercentageEndOfLife',  # noqa: E501
        'product_landfill_percentage_end_of_life': 'productLandfillPercentageEndOfLife',  # noqa: E501
        'product_incineration_percentage_end_of_life': 'productIncinerationPercentageEndOfLife',  # noqa: E501
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
    def __init__(self, product_reused_percentage_feedstock, product_reused_percentage_end_of_life, *args, **kwargs):  # noqa: E501
        """ProductCircularInformation - a model defined in OpenAPI

        Args:
            product_reused_percentage_feedstock (float): The percentage of the product's feedstock that is re-used from other sources
            product_reused_percentage_end_of_life (float): The percentage of the product that can be re-used at its end of life

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
            efficiency_percentage_recycling_feedstock (float): The efficiency of the recycling process that led to the feedstock. [optional]  # noqa: E501
            efficiency_percentage_recycling_end_of_life (float): The efficiency of the recycling process when the material reaches its end of life. [optional]  # noqa: E501
            product_recycled_percentage_feedstock (float): The percentage of the product's feedstock that comes from recycled sources. [optional]  # noqa: E501
            product_rapid_renewables_percentage_feedstock (float): The percentage of the product's feedstock that comes from rapidly renewable sources. [optional]  # noqa: E501
            product_virgin_percentage_feedstock (float): The percentage of the product's feedstock that comes from virgin sources. [optional]  # noqa: E501
            product_recycled_percentage_end_of_life (float): The percentage of the product that can be recycled at its end of life. [optional]  # noqa: E501
            product_landfill_percentage_end_of_life (float): The percentage of the product that will go to the landfill at its end of life. [optional]  # noqa: E501
            product_incineration_percentage_end_of_life (float): The percentage of the product that will be incinerated at its end of life. [optional]  # noqa: E501
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

        self.product_reused_percentage_feedstock = product_reused_percentage_feedstock
        self.product_reused_percentage_end_of_life = product_reused_percentage_end_of_life
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
