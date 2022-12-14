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

class InlineResponse200(object):
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
        'merchant_id': 'str',
        'availability': 'list[InlineResponse200Availability]'
    }

    attribute_map = {
        'merchant_id': 'merchantId',
        'availability': 'availability'
    }

    def __init__(self, merchant_id=None, availability=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._merchant_id = None
        self._availability = None
        self.discriminator = None
        self.merchant_id = merchant_id
        self.availability = availability

    @property
    def merchant_id(self):
        """Gets the merchant_id of this InlineResponse200.  # noqa: E501

        An unique merchant id provided by partners.   # noqa: E501

        :return: The merchant_id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this InlineResponse200.

        An unique merchant id provided by partners.   # noqa: E501

        :param merchant_id: The merchant_id of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def availability(self):
        """Gets the availability of this InlineResponse200.  # noqa: E501

        An array of availabilities for a service corresponding to requested parameters. All availability segments within the requested time range and with the attributes specified in the request. If request doesn't have the attributes array, all availability segments that are available for the requested time range should be returned. If there is no availability for the requested service, an empty array or null is to be returned.   # noqa: E501

        :return: The availability of this InlineResponse200.  # noqa: E501
        :rtype: list[InlineResponse200Availability]
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this InlineResponse200.

        An array of availabilities for a service corresponding to requested parameters. All availability segments within the requested time range and with the attributes specified in the request. If request doesn't have the attributes array, all availability segments that are available for the requested time range should be returned. If there is no availability for the requested service, an empty array or null is to be returned.   # noqa: E501

        :param availability: The availability of this InlineResponse200.  # noqa: E501
        :type: list[InlineResponse200Availability]
        """
        if availability is None:
            raise ValueError("Invalid value for `availability`, must not be `None`")  # noqa: E501

        self._availability = availability

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
