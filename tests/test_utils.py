from unittest.mock import mock_open, patch

from src.utils import transforming_operations


def test_successful_read_and_parse():
    with patch("builtins.open", mock_open(read_data='[{"key": "value"}]')) as mock_file:
        expected_result = [{"key": "value"}]
        result = transforming_operations("dummy_filename.json")
        assert result == expected_result
        mock_file.assert_called_once_with("dummy_filename.json", encoding="utf-8")


def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError) as mock_file:
        result = transforming_operations("non_existent_file.json")
        assert result == []
        mock_file.assert_called_once_with("non_existent_file.json", encoding="utf-8")


# Тест на случай, если файл пустой
def test_empty_file():
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        result = transforming_operations("empty_file.json")
        assert result == []
        mock_file.assert_called_once_with("empty_file.json", encoding="utf-8")


# Тест на случай, если JSON некорректен
def test_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")) as mock_file:
        result = transforming_operations("invalid_json_file.json")
        assert result == []
        mock_file.assert_called_once_with("invalid_json_file.json", encoding="utf-8")
