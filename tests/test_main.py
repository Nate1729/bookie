# Standard Library
import unittest
from unittest import mock
import tempfile
import importlib

# 3rd Party
import pytest

from bookie import main, arg_parser


class TestProcessFile(unittest.TestCase):
    def test_file_does_not_exist(self) -> None:
        # Arrange
        file_path = "foo.csv"

        # Act / Assert
        self.assertRaises(FileNotFoundError, main.process_file, file_path)


class TestGetCliArgs(unittest.TestCase):
    @mock.patch("bookie.main.sys.argv")
    def pull_args(self, mock_argv) -> None:
        # Arrange
        mock_argv.return_value = ["one", "two"]

        # Act
        result = main._get_cli_args()

        # Assert
        self.assertEqual(result, ["one", "two"])


class TestMain:
    @mock.patch("bookie.main.sys.argv")
    def test_too_few_arguments(self, mock_argv, capsys) -> None:
        # Arrange
        mock_argv.return_value = ["one"]

        # Act / Assert
        with pytest.raises((arg_parser.InputError, SystemExit)):
            main.main()

        stdout, _ = capsys.readouterr()
        assert "There was an issue with the inputs." in stdout

    @mock.patch("bookie.main.sys.argv")
    def test_too_many_arguments(self, mock_argv, capsys) -> None:
        # Arrange
        mock_argv.return_value = ["one", "two", "three"]

        # Act / Assert
        with pytest.raises((arg_parser.InputError, SystemExit)):
            main.main()

        stdout, _ = capsys.readouterr()
        assert "There was an issue with the inputs." in stdout

    @mock.patch("bookie.main._get_cli_args")
    def test_happy_path(self, mock_argv, capsys) -> None:
        # Arrange
        file = tempfile.NamedTemporaryFile(suffix=".csv")
        mock_argv.return_value = ["other", file.name]

        with open(file.name, "w") as f:
            f.write("date,vendor,amount\n")
            f.write("2022-11-20 11:23,Harbor Freight,21.84\n")
            f.write("2022-11-25 10:46,Harbor Freight,-11.22")

        # Act
        main.main()

        # Assert
        stdout, _ = capsys.readouterr()

        assert "$21.84" in stdout
        assert "$(11.22)" in stdout
