# coding: utf-8

"""
    Groupon Connect APIs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: 3pip@groupon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import mobidy_groupon_api
from mobidy_groupon_api.api.default_api import DefaultApi  # noqa: E501
from mobidy_groupon_api.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_availability(self):
        """Test case for get_availability

        Availability  # noqa: E501
        """
        pass

    def test_get_merchant_feed(self):
        """Test case for get_merchant_feed

        Content  # noqa: E501
        """
        pass

    def test_get_reservations_id(self):
        """Test case for get_reservations_id

        Retrieve Reservation  # noqa: E501
        """
        pass

    def test_get_service_availability(self):
        """Test case for get_service_availability

        Booking Availability  # noqa: E501
        """
        pass

    def test_post_booking_availability(self):
        """Test case for post_booking_availability

        Booking Availability Check  # noqa: E501
        """
        pass

    def test_post_booking_cancellations(self):
        """Test case for post_booking_cancellations

        Booking Cancellation  # noqa: E501
        """
        pass

    def test_post_booking_creation(self):
        """Test case for post_booking_creation

        Create Booking  # noqa: E501
        """
        pass

    def test_post_products_availability(self):
        """Test case for post_products_availability

        Availability Check  # noqa: E501
        """
        pass

    def test_post_reservations(self):
        """Test case for post_reservations

        Create Reservation  # noqa: E501
        """
        pass

    def test_post_reservations_id_cancellations(self):
        """Test case for post_reservations_id_cancellations

        Cancellation  # noqa: E501
        """
        pass

    def test_post_reservations_id_fulfillments(self):
        """Test case for post_reservations_id_fulfillments

        Fulfillment  # noqa: E501
        """
        pass

    def test_webhook_bookings(self):
        """Test case for webhook_bookings

        Booking Status Update  # noqa: E501
        """
        pass

    def test_webhook_reservations(self):
        """Test case for webhook_reservations

        Status Update  # noqa: E501
        """
        pass

    def test_webhook_units(self):
        """Test case for webhook_units

        Redemption  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
