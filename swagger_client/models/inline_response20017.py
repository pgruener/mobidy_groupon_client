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

class InlineResponse20017(object):
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
        'products': 'list[object]',
        'purchaser_questions': 'list[InlineResponse20016PurchaserQuestions]',
        'errors': 'list[InlineResponse20016Errors]'
    }

    attribute_map = {
        'products': 'products',
        'purchaser_questions': 'purchaserQuestions',
        'errors': 'errors'
    }

    def __init__(self, products=None, purchaser_questions=None, errors=None):  # noqa: E501
        """InlineResponse20017 - a model defined in Swagger"""  # noqa: E501
        self._products = None
        self._purchaser_questions = None
        self._errors = None
        self.discriminator = None
        self.products = products
        if purchaser_questions is not None:
            self.purchaser_questions = purchaser_questions
        if errors is not None:
            self.errors = errors

    @property
    def products(self):
        """Gets the products of this InlineResponse20017.  # noqa: E501

        The individual product available segments.   # noqa: E501

        :return: The products of this InlineResponse20017.  # noqa: E501
        :rtype: list[object]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this InlineResponse20017.

        The individual product available segments.   # noqa: E501

        :param products: The products of this InlineResponse20017.  # noqa: E501
        :type: list[object]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def purchaser_questions(self):
        """Gets the purchaser_questions of this InlineResponse20017.  # noqa: E501

        Definition of localized questions that will be asked to the purchaser. These questions will be referenced from the products and their availabilities.  # noqa: E501

        :return: The purchaser_questions of this InlineResponse20017.  # noqa: E501
        :rtype: list[InlineResponse20016PurchaserQuestions]
        """
        return self._purchaser_questions

    @purchaser_questions.setter
    def purchaser_questions(self, purchaser_questions):
        """Sets the purchaser_questions of this InlineResponse20017.

        Definition of localized questions that will be asked to the purchaser. These questions will be referenced from the products and their availabilities.  # noqa: E501

        :param purchaser_questions: The purchaser_questions of this InlineResponse20017.  # noqa: E501
        :type: list[InlineResponse20016PurchaserQuestions]
        """

        self._purchaser_questions = purchaser_questions

    @property
    def errors(self):
        """Gets the errors of this InlineResponse20017.  # noqa: E501

        An array of errors with this request, see the 400 response for further details.  # noqa: E501

        :return: The errors of this InlineResponse20017.  # noqa: E501
        :rtype: list[InlineResponse20016Errors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse20017.

        An array of errors with this request, see the 400 response for further details.  # noqa: E501

        :param errors: The errors of this InlineResponse20017.  # noqa: E501
        :type: list[InlineResponse20016Errors]
        """

        self._errors = errors

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
        if issubclass(InlineResponse20017, dict):
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
        if not isinstance(other, InlineResponse20017):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
