import unittest

from bookie import currency


class TestConvertDollarStringToCents(unittest.TestCase):
    def test_valid_amount_with_dot(self) -> None:
        # Arrange
        amount = "10.30"

        # Act
        result = currency.convert_dollar_string_to_cents(amount)

        # Assert
        self.assertEqual(result, 1030)

    def test_custom_cent_separator(self) -> None:
        # Arrange
        amount = "10,20"

        # Act
        result = currency.convert_dollar_string_to_cents(amount, ",")

        # Assert
        self.assertEqual(result, 1020)

    def test_cents_too_short(self) -> None:
        # Arrange
        amount = "10.0"

        # Act / Assert
        self.assertRaises(ValueError, currency.convert_dollar_string_to_cents, amount)

    def test_cents_too_long(self) -> None:
        # Arrange
        amount = "10.000"

        # Act / Assert
        self.assertRaises(ValueError, currency.convert_dollar_string_to_cents, amount)

    def test_no_cents(self) -> None:
        amount = "10000"

        # Act
        result = currency.convert_dollar_string_to_cents(amount)

        # Assert
        self.assertEqual(result, 10_000)


class TestApplySign(unittest.TestCase):
    def test_positive_amount(self) -> None:
        # Arrange
        amount = "12"
        is_negative = False

        # Act
        result = currency._apply_sign(amount, is_negative)

        # Arrange
        self.assertEqual(result, amount)

    def test_negative_amount(self) -> None:
        # Arrange
        amount = "12"
        is_negative = True

        # Act
        result = currency._apply_sign(amount, is_negative)

        # Assert
        self.assertEqual(result, "(12)")


class TestConvertCentsToDollarString(unittest.TestCase):
    def test_less_than_a_dollar(self) -> None:
        # Arrange
        cents = 10

        # Act
        result = currency.convert_cents_to_dollar_string(cents)

        # Assert
        self.assertEqual(result, "$0.10")

    def test_single_digit_cents(self) -> None:
        # Arrange
        cents = 1

        # Act
        result = currency.convert_cents_to_dollar_string(cents)

        # Assert
        self.assertEqual(result, "$0.01")

    def test_dollars_and_cents(self) -> None:
        # Arrange
        cents = 10035

        # Act
        result = currency.convert_cents_to_dollar_string(cents)

        # Assert
        self.assertEqual(result, "$100.35")

    def test_negative_dollars_and_cents(self) -> None:
        # Arrange
        cents = -212156

        # Act
        result = currency.convert_cents_to_dollar_string(cents)

        # Assert
        self.assertEqual(result, "$(2121.56)")
