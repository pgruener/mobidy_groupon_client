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

class InlineResponse2008ReservationProducts(object):
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
        'product_id': 'str',
        'unit_id': 'str',
        'status': 'str',
        'expires_at': 'datetime',
        'bookings': 'list[InlineResponse2008ReservationBookings]'
    }

    attribute_map = {
        'product_id': 'productId',
        'unit_id': 'unitId',
        'status': 'status',
        'expires_at': 'expiresAt',
        'bookings': 'bookings'
    }

    def __init__(self, product_id=None, unit_id=None, status=None, expires_at=None, bookings=None):  # noqa: E501
        """InlineResponse2008ReservationProducts - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._unit_id = None
        self._status = None
        self._expires_at = None
        self._bookings = None
        self.discriminator = None
        self.product_id = product_id
        if unit_id is not None:
            self.unit_id = unit_id
        self.status = status
        self.expires_at = expires_at
        if bookings is not None:
            self.bookings = bookings

    @property
    def product_id(self):
        """Gets the product_id of this InlineResponse2008ReservationProducts.  # noqa: E501

        The Partner supplied id for the product.  # noqa: E501

        :return: The product_id of this InlineResponse2008ReservationProducts.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this InlineResponse2008ReservationProducts.

        The Partner supplied id for the product.  # noqa: E501

        :param product_id: The product_id of this InlineResponse2008ReservationProducts.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def unit_id(self):
        """Gets the unit_id of this InlineResponse2008ReservationProducts.  # noqa: E501

        The Partner supplied id for the reserved unit. This id will be passed into reserve and subsequent calls of the purchase. This id must be unique across all units of all reservations.   # noqa: E501

        :return: The unit_id of this InlineResponse2008ReservationProducts.  # noqa: E501
        :rtype: str
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this InlineResponse2008ReservationProducts.

        The Partner supplied id for the reserved unit. This id will be passed into reserve and subsequent calls of the purchase. This id must be unique across all units of all reservations.   # noqa: E501

        :param unit_id: The unit_id of this InlineResponse2008ReservationProducts.  # noqa: E501
        :type: str
        """

        self._unit_id = unit_id

    @property
    def status(self):
        """Gets the status of this InlineResponse2008ReservationProducts.  # noqa: E501

        The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.   # noqa: E501

        :return: The status of this InlineResponse2008ReservationProducts.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2008ReservationProducts.

        The current status for this reservation. This represents the current state of the reservation in the reservation lifecycle state machine.   # noqa: E501

        :param status: The status of this InlineResponse2008ReservationProducts.  # noqa: E501
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
    def expires_at(self):
        """Gets the expires_at of this InlineResponse2008ReservationProducts.  # noqa: E501

        A datetime representing when the reservation was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :return: The expires_at of this InlineResponse2008ReservationProducts.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this InlineResponse2008ReservationProducts.

        A datetime representing when the reservation was created. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :param expires_at: The expires_at of this InlineResponse2008ReservationProducts.  # noqa: E501
        :type: datetime
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

    @property
    def bookings(self):
        """Gets the bookings of this InlineResponse2008ReservationProducts.  # noqa: E501

        segments being booked in the request.  # noqa: E501

        :return: The bookings of this InlineResponse2008ReservationProducts.  # noqa: E501
        :rtype: list[InlineResponse2008ReservationBookings]
        """
        return self._bookings

    @bookings.setter
    def bookings(self, bookings):
        """Sets the bookings of this InlineResponse2008ReservationProducts.

        segments being booked in the request.  # noqa: E501

        :param bookings: The bookings of this InlineResponse2008ReservationProducts.  # noqa: E501
        :type: list[InlineResponse2008ReservationBookings]
        """

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
        if issubclass(InlineResponse2008ReservationProducts, dict):
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
        if not isinstance(other, InlineResponse2008ReservationProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
