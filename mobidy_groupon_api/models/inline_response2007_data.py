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

class InlineResponse2007Data(object):
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
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'products': 'list[InlineResponse2006Products]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'products': 'products'
    }

    def __init__(self, id=None, status=None, created_at=None, updated_at=None, products=None):  # noqa: E501
        """InlineResponse2007Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._products = None
        self.discriminator = None
        self.id = id
        self.status = status
        if created_at is not None:
            self.created_at = created_at
        self.updated_at = updated_at
        self.products = products

    @property
    def id(self):
        """Gets the id of this InlineResponse2007Data.  # noqa: E501

        The partner-generated id for this reservation. This id must be unique across all reservations.  # noqa: E501

        :return: The id of this InlineResponse2007Data.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2007Data.

        The partner-generated id for this reservation. This id must be unique across all reservations.  # noqa: E501

        :param id: The id of this InlineResponse2007Data.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this InlineResponse2007Data.  # noqa: E501

        The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.   # noqa: E501

        :return: The status of this InlineResponse2007Data.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2007Data.

        The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.   # noqa: E501

        :param status: The status of this InlineResponse2007Data.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["reserved", "fulfilling", "fulfilled", "cancelling", "cancelled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2007Data.  # noqa: E501

        A datetime representing when the reservation was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :return: The created_at of this InlineResponse2007Data.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2007Data.

        A datetime representing when the reservation was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :param created_at: The created_at of this InlineResponse2007Data.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse2007Data.  # noqa: E501

        A datetime representing when the reservation was last updated. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :return: The updated_at of this InlineResponse2007Data.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse2007Data.

        A datetime representing when the reservation was last updated. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :param updated_at: The updated_at of this InlineResponse2007Data.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def products(self):
        """Gets the products of this InlineResponse2007Data.  # noqa: E501

        An array of products involved with this reservation  # noqa: E501

        :return: The products of this InlineResponse2007Data.  # noqa: E501
        :rtype: list[InlineResponse2006Products]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this InlineResponse2007Data.

        An array of products involved with this reservation  # noqa: E501

        :param products: The products of this InlineResponse2007Data.  # noqa: E501
        :type: list[InlineResponse2006Products]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

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
        if issubclass(InlineResponse2007Data, dict):
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
        if not isinstance(other, InlineResponse2007Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
