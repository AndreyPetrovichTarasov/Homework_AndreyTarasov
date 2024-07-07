from unittest.mock import patch

from src.external_api import converting_payment

# @patch("requests.get")
# def test_converting_payment(mock_get):
#     mock_get.return_value.json.return_value = {"result: 1.0"}
#     assert converting_payment({'id': 441945886,
#                                 'state': 'EXECUTED',
#                                 'date': '2019-08-26T10:50:58.294041',
#                                 'operationAmount': {'amount': '1.0', 'currency': {'name': 'руб.', 'code': 'USD'}},
#                                 'description': 'Перевод организации',
#                                 'from': 'Maestro 1596837868705199',
#                                 'to': 'Счет 64686473678894779589'}) == 1.0
#     mock_get.assert_called_once_with(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1.0&apiid=ws2JCB2959nUCODmE0dTTmn1joOQV2yf")


@patch("requests.get")
def test_converting_payment(mock_get):
    mock_get.return_value.json.return_value = {"result": 1.0}
    assert (
        converting_payment(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "1.0", "currency": {"name": "руб.", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == "Платеж совершен в USD. Сумма в рублях: 1.0"
    )
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "ws2JCB2959nUCODmE0dTTmn1joOQV2yf"},
        params={"amount": "1.0", "from": "USD", "to": "RUB"},
    )
