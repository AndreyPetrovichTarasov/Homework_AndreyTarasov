import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(dic2):
    assert list(filter_by_currency(dic2, "USD")) == [939719570, 142264268, 895315941]


def test_transaction_description(dic2):
    assert list(transaction_descriptions(dic2)) == ["Перевод организации",
                                                    "Перевод со счета на счет",
                                                    "Перевод со счета на счет",
                                                    "Перевод с карты на карту",
                                                    "Перевод организации"]


def test_card_number_generator():
    i = card_number_generator(1, 5)
    assert next(i) == "0000 0000 0000 0001"
    assert next(i) == "0000 0000 0000 0002"
    assert next(i) == "0000 0000 0000 0003"
    assert next(i) == "0000 0000 0000 0004"
    assert next(i) == "0000 0000 0000 0005"
