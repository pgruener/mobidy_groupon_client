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

class AllOfinlineResponse20015OffersProductsItems(object):
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
        'primary_category_id': 'str',
        'categories': 'list[object]',
        'purchase_url': 'str',
        'iframe_url': 'str',
        'expires_at': 'datetime',
        'expires_in_days_from_purchase': 'int',
        'pricing': 'object',
        'redemption_locations': 'list[object]',
        'points_of_interest': 'list[object]',
        'writeups': 'list[object]',
        'fulfillment_type': 'str',
        'restrictions': 'object',
        'performers': 'list[object]'
    }

    attribute_map = {
        'primary_category_id': 'primaryCategoryId',
        'categories': 'categories',
        'purchase_url': 'purchaseUrl',
        'iframe_url': 'iframeUrl',
        'expires_at': 'expiresAt',
        'expires_in_days_from_purchase': 'expiresInDaysFromPurchase',
        'pricing': 'pricing',
        'redemption_locations': 'redemptionLocations',
        'points_of_interest': 'pointsOfInterest',
        'writeups': 'writeups',
        'fulfillment_type': 'fulfillmentType',
        'restrictions': 'restrictions',
        'performers': 'performers'
    }

    def __init__(self, primary_category_id=None, categories=None, purchase_url=None, iframe_url=None, expires_at=None, expires_in_days_from_purchase=None, pricing=None, redemption_locations=None, points_of_interest=None, writeups=None, fulfillment_type=None, restrictions=None, performers=None):  # noqa: E501
        """AllOfinlineResponse20015OffersProductsItems - a model defined in Swagger"""  # noqa: E501
        self._primary_category_id = None
        self._categories = None
        self._purchase_url = None
        self._iframe_url = None
        self._expires_at = None
        self._expires_in_days_from_purchase = None
        self._pricing = None
        self._redemption_locations = None
        self._points_of_interest = None
        self._writeups = None
        self._fulfillment_type = None
        self._restrictions = None
        self._performers = None
        self.discriminator = None
        self.primary_category_id = primary_category_id
        if categories is not None:
            self.categories = categories
        if purchase_url is not None:
            self.purchase_url = purchase_url
        if iframe_url is not None:
            self.iframe_url = iframe_url
        if expires_at is not None:
            self.expires_at = expires_at
        if expires_in_days_from_purchase is not None:
            self.expires_in_days_from_purchase = expires_in_days_from_purchase
        self.pricing = pricing
        if redemption_locations is not None:
            self.redemption_locations = redemption_locations
        if points_of_interest is not None:
            self.points_of_interest = points_of_interest
        self.writeups = writeups
        if fulfillment_type is not None:
            self.fulfillment_type = fulfillment_type
        if restrictions is not None:
            self.restrictions = restrictions
        if performers is not None:
            self.performers = performers

    @property
    def primary_category_id(self):
        """Gets the primary_category_id of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The primary categorization for this product. This field is a uuid and the only acceptable values are the provided categorization uuids (please see the section on Categorization).   # noqa: E501

        :return: The primary_category_id of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: str
        """
        return self._primary_category_id

    @primary_category_id.setter
    def primary_category_id(self, primary_category_id):
        """Sets the primary_category_id of this AllOfinlineResponse20015OffersProductsItems.

        The primary categorization for this product. This field is a uuid and the only acceptable values are the provided categorization uuids (please see the section on Categorization).   # noqa: E501

        :param primary_category_id: The primary_category_id of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: str
        """
        if primary_category_id is None:
            raise ValueError("Invalid value for `primary_category_id`, must not be `None`")  # noqa: E501

        self._primary_category_id = primary_category_id

    @property
    def categories(self):
        """Gets the categories of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The list of additional categorization for this product.   # noqa: E501

        :return: The categories of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: list[object]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this AllOfinlineResponse20015OffersProductsItems.

        The list of additional categorization for this product.   # noqa: E501

        :param categories: The categories of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: list[object]
        """

        self._categories = categories

    @property
    def purchase_url(self):
        """Gets the purchase_url of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The URL used to link out to an external purchase page. This field is optional, and only used for link out offers which leave the Groupon site when the user clicks the buy button.   # noqa: E501

        :return: The purchase_url of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: str
        """
        return self._purchase_url

    @purchase_url.setter
    def purchase_url(self, purchase_url):
        """Sets the purchase_url of this AllOfinlineResponse20015OffersProductsItems.

        The URL used to link out to an external purchase page. This field is optional, and only used for link out offers which leave the Groupon site when the user clicks the buy button.   # noqa: E501

        :param purchase_url: The purchase_url of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: str
        """

        self._purchase_url = purchase_url

    @property
    def iframe_url(self):
        """Gets the iframe_url of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The URL used to render iframe content when this offer is using iframe transactions. This field is optional, and only used for iframe transactions.  A parameter called ???grouponOpportunityId??? will be appended to this URL with Groupon???s opportunity id for tracking purposes.   # noqa: E501

        :return: The iframe_url of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: str
        """
        return self._iframe_url

    @iframe_url.setter
    def iframe_url(self, iframe_url):
        """Sets the iframe_url of this AllOfinlineResponse20015OffersProductsItems.

        The URL used to render iframe content when this offer is using iframe transactions. This field is optional, and only used for iframe transactions.  A parameter called ???grouponOpportunityId??? will be appended to this URL with Groupon???s opportunity id for tracking purposes.   # noqa: E501

        :param iframe_url: The iframe_url of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: str
        """

        self._iframe_url = iframe_url

    @property
    def expires_at(self):
        """Gets the expires_at of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The datetime which specifies when the product expires. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :return: The expires_at of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AllOfinlineResponse20015OffersProductsItems.

        The datetime which specifies when the product expires. The format is ISO-8601 combined date and time with timezone (also known as Internet date/time format: https://tools.ietf.org/html/rfc3339#section-5).   # noqa: E501

        :param expires_at: The expires_at of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def expires_in_days_from_purchase(self):
        """Gets the expires_in_days_from_purchase of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        Specifies the number of days relative from purchase which the product expires. This allows non-fixed expiration based on the purchase date by a user. This is used to signal to the user that the product expires a certain number of days from the date of purchase.   # noqa: E501

        :return: The expires_in_days_from_purchase of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: int
        """
        return self._expires_in_days_from_purchase

    @expires_in_days_from_purchase.setter
    def expires_in_days_from_purchase(self, expires_in_days_from_purchase):
        """Sets the expires_in_days_from_purchase of this AllOfinlineResponse20015OffersProductsItems.

        Specifies the number of days relative from purchase which the product expires. This allows non-fixed expiration based on the purchase date by a user. This is used to signal to the user that the product expires a certain number of days from the date of purchase.   # noqa: E501

        :param expires_in_days_from_purchase: The expires_in_days_from_purchase of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: int
        """

        self._expires_in_days_from_purchase = expires_in_days_from_purchase

    @property
    def pricing(self):
        """Gets the pricing of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501


        :return: The pricing of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: object
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this AllOfinlineResponse20015OffersProductsItems.


        :param pricing: The pricing of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: object
        """
        if pricing is None:
            raise ValueError("Invalid value for `pricing`, must not be `None`")  # noqa: E501

        self._pricing = pricing

    @property
    def redemption_locations(self):
        """Gets the redemption_locations of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The list of locations at which this product can be redeemed.   # noqa: E501

        :return: The redemption_locations of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: list[object]
        """
        return self._redemption_locations

    @redemption_locations.setter
    def redemption_locations(self, redemption_locations):
        """Sets the redemption_locations of this AllOfinlineResponse20015OffersProductsItems.

        The list of locations at which this product can be redeemed.   # noqa: E501

        :param redemption_locations: The redemption_locations of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: list[object]
        """

        self._redemption_locations = redemption_locations

    @property
    def points_of_interest(self):
        """Gets the points_of_interest of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        A list of locations that will show up in a map to give more context to the purchaser. For example this can be used for locations that a tour will visit. If pointsOfInterest aren't present, we will show the redemptionLocations on the map.   # noqa: E501

        :return: The points_of_interest of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: list[object]
        """
        return self._points_of_interest

    @points_of_interest.setter
    def points_of_interest(self, points_of_interest):
        """Sets the points_of_interest of this AllOfinlineResponse20015OffersProductsItems.

        A list of locations that will show up in a map to give more context to the purchaser. For example this can be used for locations that a tour will visit. If pointsOfInterest aren't present, we will show the redemptionLocations on the map.   # noqa: E501

        :param points_of_interest: The points_of_interest of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: list[object]
        """

        self._points_of_interest = points_of_interest

    @property
    def writeups(self):
        """Gets the writeups of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The text which describes the specific items or services being offered.   # noqa: E501

        :return: The writeups of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: list[object]
        """
        return self._writeups

    @writeups.setter
    def writeups(self, writeups):
        """Sets the writeups of this AllOfinlineResponse20015OffersProductsItems.

        The text which describes the specific items or services being offered.   # noqa: E501

        :param writeups: The writeups of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: list[object]
        """
        if writeups is None:
            raise ValueError("Invalid value for `writeups`, must not be `None`")  # noqa: E501

        self._writeups = writeups

    @property
    def fulfillment_type(self):
        """Gets the fulfillment_type of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The type of fulfillment for this product. This indicates how the user will receive the product after purchase.  `Pickup` indicates the purchaser must go and pick up their product, such as \"will call\" for tickets.  `Shipped` indicates that the product will be shipped to the purchaser.  `Electronic` indicates that the purchaser will receive their product electronically, such as a PDF version of a ticket or voucher. Please note that this means that the `data.products[].reservedUnits[].details.voucherUrl` attribute on the reservation in the transactional endpoints needs to be set when the purchase is fulfilled.   # noqa: E501

        :return: The fulfillment_type of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, fulfillment_type):
        """Sets the fulfillment_type of this AllOfinlineResponse20015OffersProductsItems.

        The type of fulfillment for this product. This indicates how the user will receive the product after purchase.  `Pickup` indicates the purchaser must go and pick up their product, such as \"will call\" for tickets.  `Shipped` indicates that the product will be shipped to the purchaser.  `Electronic` indicates that the purchaser will receive their product electronically, such as a PDF version of a ticket or voucher. Please note that this means that the `data.products[].reservedUnits[].details.voucherUrl` attribute on the reservation in the transactional endpoints needs to be set when the purchase is fulfilled.   # noqa: E501

        :param fulfillment_type: The fulfillment_type of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["pickup", "shipped", "electronic"]  # noqa: E501
        if fulfillment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fulfillment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fulfillment_type, allowed_values)
            )

        self._fulfillment_type = fulfillment_type

    @property
    def restrictions(self):
        """Gets the restrictions of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The restrictions associated with this product.  # noqa: E501

        :return: The restrictions of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: object
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this AllOfinlineResponse20015OffersProductsItems.

        The restrictions associated with this product.  # noqa: E501

        :param restrictions: The restrictions of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: object
        """

        self._restrictions = restrictions

    @property
    def performers(self):
        """Gets the performers of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501

        The performers or artists associated with this product.   # noqa: E501

        :return: The performers of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :rtype: list[object]
        """
        return self._performers

    @performers.setter
    def performers(self, performers):
        """Sets the performers of this AllOfinlineResponse20015OffersProductsItems.

        The performers or artists associated with this product.   # noqa: E501

        :param performers: The performers of this AllOfinlineResponse20015OffersProductsItems.  # noqa: E501
        :type: list[object]
        """

        self._performers = performers

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
        if issubclass(AllOfinlineResponse20015OffersProductsItems, dict):
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
        if not isinstance(other, AllOfinlineResponse20015OffersProductsItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
