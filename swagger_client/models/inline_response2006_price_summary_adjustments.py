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

class InlineResponse2006PriceSummaryAdjustments(object):
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
        'type': 'str',
        'value': 'InlineResponse2006PriceSummaryValue'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):  # noqa: E501
        """InlineResponse2006PriceSummaryAdjustments - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._value = None
        self.discriminator = None
        self.type = type
        self.value = value

    @property
    def type(self):
        """Gets the type of this InlineResponse2006PriceSummaryAdjustments.  # noqa: E501

        Type of the adjustment to be charged over the customer price i.e price, which should be chosen from the enum. * TAX - Any tax amount to be applied on the price. * DELIVERY_FEE - Any associated delivery fee, if the item is to be shipped. * TIP - Any extra tip added by the customer for the merchant. * BOOKING_FEE - Some partners process additional cost for the booking. This fee is associated to the booking cost. * SERVICE_FEE - This is additional fee charged by merchant for providing a service.   # noqa: E501

        :return: The type of this InlineResponse2006PriceSummaryAdjustments.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2006PriceSummaryAdjustments.

        Type of the adjustment to be charged over the customer price i.e price, which should be chosen from the enum. * TAX - Any tax amount to be applied on the price. * DELIVERY_FEE - Any associated delivery fee, if the item is to be shipped. * TIP - Any extra tip added by the customer for the merchant. * BOOKING_FEE - Some partners process additional cost for the booking. This fee is associated to the booking cost. * SERVICE_FEE - This is additional fee charged by merchant for providing a service.   # noqa: E501

        :param type: The type of this InlineResponse2006PriceSummaryAdjustments.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["TAX", "DELIVERY_FEE", "TIP", "BOOKING_FEE", "SERVICE_FEE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this InlineResponse2006PriceSummaryAdjustments.  # noqa: E501


        :return: The value of this InlineResponse2006PriceSummaryAdjustments.  # noqa: E501
        :rtype: InlineResponse2006PriceSummaryValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InlineResponse2006PriceSummaryAdjustments.


        :param value: The value of this InlineResponse2006PriceSummaryAdjustments.  # noqa: E501
        :type: InlineResponse2006PriceSummaryValue
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(InlineResponse2006PriceSummaryAdjustments, dict):
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
        if not isinstance(other, InlineResponse2006PriceSummaryAdjustments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
