import unittest

from bookie import arg_parser


class TestGetFileExtension(unittest.TestCase):
    def test_no_dot(self) -> None:
        """No file extension returns None."""
        # Arrange
        file_name = "foo"

        # Act
        extension = arg_parser.get_file_extension(file_name)

        # Assert
        self.assertIsNone(extension)

    def test_dot(self) -> None:
        """Passing a file with its extension
        returns the extension.
        """
        # Arrange
        file_name = "foo.csv"

        # Act
        extension = arg_parser.get_file_extension(file_name)

        # Assert
        self.assertEqual(extension, "csv")

    def test_multiple_dots(self) -> None:
        """Passing multiple extensions returns
        the last one.
        """
        # Arrange
        file_name = "foo.txt.csv.xml"

        # Act
        extension = arg_parser.get_file_extension(file_name)

        # Assert
        self.assertEqual(extension, "xml")


class TestValidateArguments(unittest.TestCase):
    def test_empty_args(self) -> None:
        """Empty argument list raises an
        exception.
        """
        # Arrange
        args = []

        # Assert  / Act
        with self.assertRaises(arg_parser.InputError):
            arg_parser.validate_arguments(args)

    def test_single_arg(self) -> None:
        # Arrange
        args = ["bar"]

        # Assert / Act
        with self.assertRaises(arg_parser.InputError):
            arg_parser.validate_arguments(args)

    def test_too_many_args(self) -> None:
        # Arrange
        args = ["foo", "bar", "fizz"]

        # Assert / Act
        with self.assertRaises(arg_parser.InputError):
            arg_parser.validate_arguments(args)

    def test_improper_file_extension(self) -> None:
        # Arrange
        args = ["name", "foo.txt"]

        # Assert / Act
        with self.assertRaises(arg_parser.InputError):
            arg_parser.validate_arguments(args)

    def test_csv_file_extension(self) -> None:
        # Arrange
        args = ["name", "foo.csv"]

        # Act
        file_name = arg_parser.validate_arguments(args)

        # Assert
        self.assertEqual(file_name, "foo.csv")
