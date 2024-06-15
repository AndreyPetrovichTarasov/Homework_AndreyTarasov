import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("card_account, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                    ("Счет 64686473678894779589", "Счет **9589")])
def test_mask_account_card(card_account, expected):
    assert mask_account_card(card_account) == expected


def test_mask_account_card_wrong_card(cards):
    with pytest.raises(TypeError):
        mask_account_card(cards)


def test_get_data():
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_get_data_wrong_str():
    with pytest.raises(ValueError):
        get_data("data")
