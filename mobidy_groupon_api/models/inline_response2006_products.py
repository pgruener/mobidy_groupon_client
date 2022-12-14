# coding: utf-8

"""
    Groupon Connect APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: 3pip@groupon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2006Products(object):
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
        'category_id': 'str',
        'quantity': 'int',
        'price_summary': 'InlineResponse2006PriceSummary',
        'accounting_details': 'InlineResponse2006AccountingDetails',
        'reserved_units': 'list[AllOfinlineResponse2006ProductsReservedUnitsItems]'
    }

    attribute_map = {
        'id': 'id',
        'category_id': 'categoryId',
        'quantity': 'quantity',
        'price_summary': 'priceSummary',
        'accounting_details': 'accountingDetails',
        'reserved_units': 'reservedUnits'
    }

    def __init__(self, id=None, category_id=None, quantity=None, price_summary=None, accounting_details=None, reserved_units=None):  # noqa: E501
        """InlineResponse2006Products - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._category_id = None
        self._quantity = None
        self._price_summary = None
        self._accounting_details = None
        self._reserved_units = None
        self.discriminator = None
        self.id = id
        if category_id is not None:
            self.category_id = category_id
        if quantity is not None:
            self.quantity = quantity
        self.price_summary = price_summary
        if accounting_details is not None:
            self.accounting_details = accounting_details
        self.reserved_units = reserved_units

    @property
    def id(self):
        """Gets the id of this InlineResponse2006Products.  # noqa: E501

        The Partner supplied id for the product.  # noqa: E501

        :return: The id of this InlineResponse2006Products.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2006Products.

        The Partner supplied id for the product.  # noqa: E501

        :param id: The id of this InlineResponse2006Products.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def category_id(self):
        """Gets the category_id of this InlineResponse2006Products.  # noqa: E501

        The categorization for this product.  This field is a uuid and the only acceptable values are the provided categorization uuids.   # noqa: E501

        :return: The category_id of this InlineResponse2006Products.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this InlineResponse2006Products.

        The categorization for this product.  This field is a uuid and the only acceptable values are the provided categorization uuids.   # noqa: E501

        :param category_id: The category_id of this InlineResponse2006Products.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def quantity(self):
        """Gets the quantity of this InlineResponse2006Products.  # noqa: E501

        The quantity of this product being reserved. This isn't used if bookings are present.  # noqa: E501

        :return: The quantity of this InlineResponse2006Products.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InlineResponse2006Products.

        The quantity of this product being reserved. This isn't used if bookings are present.  # noqa: E501

        :param quantity: The quantity of this InlineResponse2006Products.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def price_summary(self):
        """Gets the price_summary of this InlineResponse2006Products.  # noqa: E501


        :return: The price_summary of this InlineResponse2006Products.  # noqa: E501
        :rtype: InlineResponse2006PriceSummary
        """
        return self._price_summary

    @price_summary.setter
    def price_summary(self, price_summary):
        """Sets the price_summary of this InlineResponse2006Products.


        :param price_summary: The price_summary of this InlineResponse2006Products.  # noqa: E501
        :type: InlineResponse2006PriceSummary
        """
        if price_summary is None:
            raise ValueError("Invalid value for `price_summary`, must not be `None`")  # noqa: E501

        self._price_summary = price_summary

    @property
    def accounting_details(self):
        """Gets the accounting_details of this InlineResponse2006Products.  # noqa: E501


        :return: The accounting_details of this InlineResponse2006Products.  # noqa: E501
        :rtype: InlineResponse2006AccountingDetails
        """
        return self._accounting_details

    @accounting_details.setter
    def accounting_details(self, accounting_details):
        """Sets the accounting_details of this InlineResponse2006Products.


        :param accounting_details: The accounting_details of this InlineResponse2006Products.  # noqa: E501
        :type: InlineResponse2006AccountingDetails
        """

        self._accounting_details = accounting_details

    @property
    def reserved_units(self):
        """Gets the reserved_units of this InlineResponse2006Products.  # noqa: E501

        An array of reserved units. This section may also be used for iframe bookings to pass details from the partner back to Groupon about the reservation. If quantity is specified in the request, the size of this array should match the quantity in the request.   # noqa: E501

        :return: The reserved_units of this InlineResponse2006Products.  # noqa: E501
        :rtype: list[AllOfinlineResponse2006ProductsReservedUnitsItems]
        """
        return self._reserved_units

    @reserved_units.setter
    def reserved_units(self, reserved_units):
        """Sets the reserved_units of this InlineResponse2006Products.

        An array of reserved units. This section may also be used for iframe bookings to pass details from the partner back to Groupon about the reservation. If quantity is specified in the request, the size of this array should match the quantity in the request.   # noqa: E501

        :param reserved_units: The reserved_units of this InlineResponse2006Products.  # noqa: E501
        :type: list[AllOfinlineResponse2006ProductsReservedUnitsItems]
        """
        if reserved_units is None:
            raise ValueError("Invalid value for `reserved_units`, must not be `None`")  # noqa: E501

        self._reserved_units = reserved_units

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
        if issubclass(InlineResponse2006Products, dict):
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
        if not isinstance(other, InlineResponse2006Products):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
