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

class InlineResponse40010(object):
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
        'errors': 'list[InlineResponse40010Errors]',
        'http_code': 'int'
    }

    attribute_map = {
        'errors': 'errors',
        'http_code': 'httpCode'
    }

    def __init__(self, errors=None, http_code=None):  # noqa: E501
        """InlineResponse40010 - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._http_code = None
        self.discriminator = None
        self.errors = errors
        self.http_code = http_code

    @property
    def errors(self):
        """Gets the errors of this InlineResponse40010.  # noqa: E501

        List of errors from the request.  # noqa: E501

        :return: The errors of this InlineResponse40010.  # noqa: E501
        :rtype: list[InlineResponse40010Errors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse40010.

        List of errors from the request.  # noqa: E501

        :param errors: The errors of this InlineResponse40010.  # noqa: E501
        :type: list[InlineResponse40010Errors]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def http_code(self):
        """Gets the http_code of this InlineResponse40010.  # noqa: E501

        The HTTP status code for this error.  # noqa: E501

        :return: The http_code of this InlineResponse40010.  # noqa: E501
        :rtype: int
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        """Sets the http_code of this InlineResponse40010.

        The HTTP status code for this error.  # noqa: E501

        :param http_code: The http_code of this InlineResponse40010.  # noqa: E501
        :type: int
        """
        if http_code is None:
            raise ValueError("Invalid value for `http_code`, must not be `None`")  # noqa: E501

        self._http_code = http_code

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
        if issubclass(InlineResponse40010, dict):
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
        if not isinstance(other, InlineResponse40010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
