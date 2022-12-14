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

class Grouponv1bookingsAvailability(object):
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
        'available_at': 'datetime',
        'available_until': 'datetime',
        'service_id': 'str',
        'attribute_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'available_at': 'availableAt',
        'available_until': 'availableUntil',
        'service_id': 'serviceId',
        'attribute_ids': 'attributeIds'
    }

    def __init__(self, id=None, available_at=None, available_until=None, service_id=None, attribute_ids=None):  # noqa: E501
        """Grouponv1bookingsAvailability - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._available_at = None
        self._available_until = None
        self._service_id = None
        self._attribute_ids = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.available_at = available_at
        self.available_until = available_until
        self.service_id = service_id
        if attribute_ids is not None:
            self.attribute_ids = attribute_ids

    @property
    def id(self):
        """Gets the id of this Grouponv1bookingsAvailability.  # noqa: E501

        ID of the availability slot. See in ingestion availability spec *availability[].id*   # noqa: E501

        :return: The id of this Grouponv1bookingsAvailability.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Grouponv1bookingsAvailability.

        ID of the availability slot. See in ingestion availability spec *availability[].id*   # noqa: E501

        :param id: The id of this Grouponv1bookingsAvailability.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def available_at(self):
        """Gets the available_at of this Grouponv1bookingsAvailability.  # noqa: E501

        The start time and date of the availability slot/segment to be booked.   # noqa: E501

        :return: The available_at of this Grouponv1bookingsAvailability.  # noqa: E501
        :rtype: datetime
        """
        return self._available_at

    @available_at.setter
    def available_at(self, available_at):
        """Sets the available_at of this Grouponv1bookingsAvailability.

        The start time and date of the availability slot/segment to be booked.   # noqa: E501

        :param available_at: The available_at of this Grouponv1bookingsAvailability.  # noqa: E501
        :type: datetime
        """
        if available_at is None:
            raise ValueError("Invalid value for `available_at`, must not be `None`")  # noqa: E501

        self._available_at = available_at

    @property
    def available_until(self):
        """Gets the available_until of this Grouponv1bookingsAvailability.  # noqa: E501

        The end time and date of the availability slot/segment to be booked.   # noqa: E501

        :return: The available_until of this Grouponv1bookingsAvailability.  # noqa: E501
        :rtype: datetime
        """
        return self._available_until

    @available_until.setter
    def available_until(self, available_until):
        """Sets the available_until of this Grouponv1bookingsAvailability.

        The end time and date of the availability slot/segment to be booked.   # noqa: E501

        :param available_until: The available_until of this Grouponv1bookingsAvailability.  # noqa: E501
        :type: datetime
        """
        if available_until is None:
            raise ValueError("Invalid value for `available_until`, must not be `None`")  # noqa: E501

        self._available_until = available_until

    @property
    def service_id(self):
        """Gets the service_id of this Grouponv1bookingsAvailability.  # noqa: E501

        The IDs of the specific service to book.   # noqa: E501

        :return: The service_id of this Grouponv1bookingsAvailability.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Grouponv1bookingsAvailability.

        The IDs of the specific service to book.   # noqa: E501

        :param service_id: The service_id of this Grouponv1bookingsAvailability.  # noqa: E501
        :type: str
        """
        if service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def attribute_ids(self):
        """Gets the attribute_ids of this Grouponv1bookingsAvailability.  # noqa: E501

        Reference to the attribute values that this availability slot has.   # noqa: E501

        :return: The attribute_ids of this Grouponv1bookingsAvailability.  # noqa: E501
        :rtype: list[str]
        """
        return self._attribute_ids

    @attribute_ids.setter
    def attribute_ids(self, attribute_ids):
        """Sets the attribute_ids of this Grouponv1bookingsAvailability.

        Reference to the attribute values that this availability slot has.   # noqa: E501

        :param attribute_ids: The attribute_ids of this Grouponv1bookingsAvailability.  # noqa: E501
        :type: list[str]
        """

        self._attribute_ids = attribute_ids

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
        if issubclass(Grouponv1bookingsAvailability, dict):
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
        if not isinstance(other, Grouponv1bookingsAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
