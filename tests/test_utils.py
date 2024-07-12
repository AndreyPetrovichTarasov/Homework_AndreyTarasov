import pytest
import pandas as pd
from unittest.mock import mock_open, patch

from src.utils import transforming_operations, from_csv, from_xlsx


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


@pytest.fixture
def mock_csv_data():
    return pd.DataFrame({
        'id': [1, 2],
        'state': ['EXECUTED', 'CANCELLED'],
        'date': ['2023-01-01', '2023-01-02'],
        'amount': [100.0, 200.0],
        'currency_name': ['USD', 'EUR'],
        'currency_code': ['USD', 'EUR'],
        'description': ['Payment 1', 'Payment 2'],
        'from': ['Account 1', 'Account 2'],
        'to': ['Account 3', 'Account 4']
    })


@pytest.fixture
def mock_xlsx_data():
    return pd.DataFrame({
        'id': [1, 2],
        'state': ['EXECUTED', 'CANCELLED'],
        'date': ['2023-01-01', '2023-01-02'],
        'amount': [100.0, 200.0],
        'currency_name': ['USD', 'EUR'],
        'currency_code': ['USD', 'EUR'],
        'description': ['Payment 1', 'Payment 2'],
        'from': ['Account 1', 'Account 2'],
        'to': ['Account 3', 'Account 4']
    })


@patch('src.utils.pd.read_csv')
def test_from_csv(mock_read_csv, mock_csv_data):
    mock_read_csv.return_value = mock_csv_data

    result = from_csv()

    expected_result = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2023-01-01',
            'operationAmount': {'amount': 100.0, 'currensy': {'name': 'USD', 'code': 'USD'}},
            'description': 'Payment 1',
            'from': 'Account 1',
            'to': 'Account 3'
        },
        {
            'id': 2,
            'state': 'CANCELLED',
            'date': '2023-01-02',
            'operationAmount': {'amount': 200.0, 'currensy': {'name': 'EUR', 'code': 'EUR'}},
            'description': 'Payment 2',
            'from': 'Account 2',
            'to': 'Account 4'
        }
    ]

    assert result == expected_result


@patch('src.utils.pd.read_excel')
def test_from_xlsx(mock_read_excel, mock_xlsx_data):
    mock_read_excel.return_value = mock_xlsx_data

    result = from_xlsx()

    expected_result = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2023-01-01',
            'operationAmount': {'amount': 100.0, 'currensy': {'name': 'USD', 'code': 'USD'}},
            'description': 'Payment 1',
            'from': 'Account 1',
            'to': 'Account 3'
        },
        {
            'id': 2,
            'state': 'CANCELLED',
            'date': '2023-01-02',
            'operationAmount': {'amount': 200.0, 'currensy': {'name': 'EUR', 'code': 'EUR'}},
            'description': 'Payment 2',
            'from': 'Account 2',
            'to': 'Account 4'
        }
    ]

    assert result == expected_result
