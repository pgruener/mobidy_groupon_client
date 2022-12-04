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

class InlineResponse2008(object):
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
        'schema_version': 'str',
        'reservation': 'InlineResponse2008Reservation'
    }

    attribute_map = {
        'schema_version': 'schemaVersion',
        'reservation': 'reservation'
    }

    def __init__(self, schema_version=None, reservation=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501
        self._schema_version = None
        self._reservation = None
        self.discriminator = None
        self.schema_version = schema_version
        self.reservation = reservation

    @property
    def schema_version(self):
        """Gets the schema_version of this InlineResponse2008.  # noqa: E501

        The version of the schema being used for the available segments feed.  This is used to allow compatibility between multiple schema versions.   # noqa: E501

        :return: The schema_version of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this InlineResponse2008.

        The version of the schema being used for the available segments feed.  This is used to allow compatibility between multiple schema versions.   # noqa: E501

        :param schema_version: The schema_version of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if schema_version is None:
            raise ValueError("Invalid value for `schema_version`, must not be `None`")  # noqa: E501
        allowed_values = ["v2.0"]  # noqa: E501
        if schema_version not in allowed_values:
            raise ValueError(
                "Invalid value for `schema_version` ({0}), must be one of {1}"  # noqa: E501
                .format(schema_version, allowed_values)
            )

        self._schema_version = schema_version

    @property
    def reservation(self):
        """Gets the reservation of this InlineResponse2008.  # noqa: E501


        :return: The reservation of this InlineResponse2008.  # noqa: E501
        :rtype: InlineResponse2008Reservation
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this InlineResponse2008.


        :param reservation: The reservation of this InlineResponse2008.  # noqa: E501
        :type: InlineResponse2008Reservation
        """
        if reservation is None:
            raise ValueError("Invalid value for `reservation`, must not be `None`")  # noqa: E501

        self._reservation = reservation

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
        if issubclass(InlineResponse2008, dict):
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
