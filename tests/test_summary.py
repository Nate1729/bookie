from datetime import datetime
import unittest
from unittest import mock

from bookie import summary, models

class TestSummary(unittest.TestCase):
    def test_calculate_total(self) -> None:
        # Arrange
        receipts = [
            models.Receipt(date=datetime.utcnow(), vendor='Foo', amount_in_cents=25),
            models.Receipt(date=datetime.utcnow(), vendor='Foo', amount_in_cents=50),
            models.Receipt(date=datetime.utcnow(), vendor='Foo', amount_in_cents=75),
        ]

        # Act
        total = summary.calculate_total(receipts)

        # Assert
        self.assertEqual(total, 150)

    def test_find_purchases(self) -> None:
        # Arrange
        receipts = [
            models.Receipt(date=datetime.utcnow(), vendor='Foo', amount_in_cents=25),
            models.Receipt(date=datetime.utcnow(), vendor='Bar', amount_in_cents=-50),
            models.Receipt(date=datetime.utcnow(), vendor='Fiz', amount_in_cents=75),
        ]

        # Act
        purchases = summary.find_purchases(receipts)

        # Assert
        self.assertEqual(len(purchases), 2)
        self.assertIn(receipts[0], purchases)
        self.assertIn(receipts[2], purchases)

    def test_find_returns(self) -> None:
        # Arrange
        receipts = [
            models.Receipt(date=datetime.utcnow(), vendor='Foo', amount_in_cents=25),
            models.Receipt(date=datetime.utcnow(), vendor='Bar', amount_in_cents=-50),
            models.Receipt(date=datetime.utcnow(), vendor='Fiz', amount_in_cents=75),
            models.Receipt(date=datetime.utcnow(), vendor='Buzz', amount_in_cents=-60),
        ]

        # Act
        returns = summary.find_returns(receipts)

        # Assert
        self.assertEqual(len(returns), 2)
        self.assertIn(receipts[1], returns)
        self.assertIn(receipts[3], returns)

    @mock.patch('builtins.print')
    def test_print_formatted_line(self, mock_print) -> None:
        # Arrange
        label = "Foo"
        value = 10

        # Act
        summary.print_formatted_line(label, value)

        # Assert
        mock_print.assert_called_with("Foo             10") # 13 spaces

    @mock.patch('bookie.summary.print')
    def test_summarize(self, mock_print) -> None:
        # Arrange
        receipts = [
            models.Receipt(date=datetime.utcnow(), vendor='Foo', amount_in_cents=25),
            models.Receipt(date=datetime.utcnow(), vendor='Bar', amount_in_cents=-50),
            models.Receipt(date=datetime.utcnow(), vendor='Fiz', amount_in_cents=75),
            models.Receipt(date=datetime.utcnow(), vendor='Buzz', amount_in_cents=-60),
        ]

        # Act
        summary.summarize(receipts)

        # Assert
        mock_print.assert_has_calls([
            mock.call('----------------'),
            mock.call('Purchases        2'),
            mock.call('Total        $1.00'),
            mock.call('\n'),
            mock.call('Returns          2'),
            mock.call('Total      $(1.10)')
        ])
