import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(cards):
    assert get_mask_card_number(cards) == "7000 79** **** 6361"


@pytest.mark.parametrize("wrong_cards", [234,
                                         "535455",
                                         [2342, 23423],
                                         {123: 1234}])
def test_get_mask_card_number_wrong_card(wrong_cards):
    assert get_mask_card_number(wrong_cards) == "Некорректный номер"


@pytest.mark.parametrize("wrong_accounts", ["34.4",
                                            "535455",
                                            [2342, 23423],
                                            {123: 1234}])
def test_get_mask_card_number_wrong_account(wrong_accounts):
    assert get_mask_account(wrong_accounts) == "Некорректный номер"


def test_get_mask_account(accounts):
    assert get_mask_account(accounts) == "**4305"


def test_get_mask_card_number_empty():
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_account_empty():
    with pytest.raises(TypeError):
        get_mask_account()
