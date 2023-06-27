import unittest
from unittest import mock

from bookie import models


class TestReceiptFromDict(unittest.TestCase):
    def test_missing_date(self) -> None:
        """A missing `date` key should raise
        an exception.
        """
        # Arrange
        data = {"vendor": mock.Mock, "amount": mock.Mock}

        # Act / Assert
        self.assertRaises(models.MissingDataException, models.receipt_from_dict, data)

    def test_missing_vender(self) -> None:
        """A missing `amount` key should raise
        an exception.
        """
        # Arrange
        data = {"date": mock.Mock, "amount": mock.Mock}

        # Act / Assert
        self.assertRaises(models.MissingDataException, models.receipt_from_dict, data)

    def test_missing_amount(self) -> None:
        """A missing `amount` key should raise
        an exception.
        """
        # Arrange
        data = {"vendor": mock.Mock, "date": mock.Mock}

        # Act / Assert
        self.assertRaises(models.MissingDataException, models.receipt_from_dict, data)
