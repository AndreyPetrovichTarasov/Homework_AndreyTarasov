import sys
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parent.parent))
from data.config import ROOT_PATH
from src.utils import transforming_operations

ROOT_PATH2 = Path(__file__).resolve().parent.parent

env_path = ROOT_PATH2 / '.env'

load_dotenv(env_path)

API_KEY = os.getenv("API_KEY_EXCHAGE")


def converting_payment(transaction):
    """
    Функция возвращает сумму транзакции в рублях. Если платеж совершен в ЕВРО или USD, происходит конвертация в рубли.
    """
    if not transaction.get("operationAmount").get("currency").get("code"):

        return 0

    elif transaction["operationAmount"]["currency"]["code"] == "RUB":

        return f'Платеж совершен в рублях. Сумма: {transaction["operationAmount"]["amount"]}'

    elif transaction["operationAmount"]["currency"]["code"] == "USD":
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": "USD",
            "to": "RUB"
        }
        headers = {
            "apikey": API_KEY
        }
        response = requests.get(url, headers=headers, params=payload)
        result_json = response.json()

        return f'Платеж совершен в USD. Сумма в рублях: {result_json["result"]}'

    elif transaction["operationAmount"]["currency"]["code"] == "EURO":
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": "EURO",
            "to": "RUB"
        }
        headers = {
            "apikey": API_KEY
        }
        response = requests.get(url, headers=headers, params=payload)
        result_json = response.json()

        return f'Платеж совершен в ЕВРО. Сумма в рублях: {result_json["result"]}'


if __name__ == "__main__":
    operations_path = Path(ROOT_PATH, "operations.json")
    returned_list = transforming_operations(operations_path)

    for i in range(5):
        one_operation = converting_payment(returned_list[i])
        print(one_operation)
