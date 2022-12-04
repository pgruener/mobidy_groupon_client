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

class InlineResponse2001(object):
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
        'bookings': 'list[AllOfinlineResponse2001BookingsItems]'
    }

    attribute_map = {
        'bookings': 'bookings'
    }

    def __init__(self, bookings=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._bookings = None
        self.discriminator = None
        self.bookings = bookings

    @property
    def bookings(self):
        """Gets the bookings of this InlineResponse2001.  # noqa: E501


        :return: The bookings of this InlineResponse2001.  # noqa: E501
        :rtype: list[AllOfinlineResponse2001BookingsItems]
        """
        return self._bookings

    @bookings.setter
    def bookings(self, bookings):
        """Sets the bookings of this InlineResponse2001.


        :param bookings: The bookings of this InlineResponse2001.  # noqa: E501
        :type: list[AllOfinlineResponse2001BookingsItems]
        """
        if bookings is None:
            raise ValueError("Invalid value for `bookings`, must not be `None`")  # noqa: E501

        self._bookings = bookings

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
