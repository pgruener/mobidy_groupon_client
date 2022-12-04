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

class Grouponv1reservationsreservationIdunitscancellationsData(object):
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
        'reserved_units': 'list[Grouponv1reservationsreservationIdunitscancellationsDataReservedUnits]'
    }

    attribute_map = {
        'reserved_units': 'reservedUnits'
    }

    def __init__(self, reserved_units=None):  # noqa: E501
        """Grouponv1reservationsreservationIdunitscancellationsData - a model defined in Swagger"""  # noqa: E501
        self._reserved_units = None
        self.discriminator = None
        self.reserved_units = reserved_units

    @property
    def reserved_units(self):
        """Gets the reserved_units of this Grouponv1reservationsreservationIdunitscancellationsData.  # noqa: E501

        An array of reserved units to be cancelled in a reservation.   # noqa: E501

        :return: The reserved_units of this Grouponv1reservationsreservationIdunitscancellationsData.  # noqa: E501
        :rtype: list[Grouponv1reservationsreservationIdunitscancellationsDataReservedUnits]
        """
        return self._reserved_units

    @reserved_units.setter
    def reserved_units(self, reserved_units):
        """Sets the reserved_units of this Grouponv1reservationsreservationIdunitscancellationsData.

        An array of reserved units to be cancelled in a reservation.   # noqa: E501

        :param reserved_units: The reserved_units of this Grouponv1reservationsreservationIdunitscancellationsData.  # noqa: E501
        :type: list[Grouponv1reservationsreservationIdunitscancellationsDataReservedUnits]
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
        if issubclass(Grouponv1reservationsreservationIdunitscancellationsData, dict):
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
        if not isinstance(other, Grouponv1reservationsreservationIdunitscancellationsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other