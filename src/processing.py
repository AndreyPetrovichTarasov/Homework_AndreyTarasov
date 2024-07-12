import math
from dateutil.parser import parse
from typing import Dict, List
from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_data
from src.utils import list_from_csv
from src.widget import mask_account_card


def filter_by_state(list_id: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция сортировки списка по ключу "state"."""
    sorted_list_id = [dict_id for dict_id in list_id if dict_id.get("state", "") == state]
    return sorted_list_id


def sort_by_date(list_id: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция сортировки списка по дате (по возрастанию или убыванию)."""
    sorted_list = sorted(list_id, key=lambda dict_id: dict_id["date"], reverse=reverse)
    return sorted_list


def format_transaction(transaction):
    date_str = transaction.get("date", "N/A")
    if date_str != "N/A":
        date_str = parse(date_str).strftime("%d.%m.%Y")

    description = transaction.get("description", "N/A")

    amount_info = transaction.get("operationAmount", {})
    amount = amount_info.get("amount", "N/A")
    if isinstance(amount, str) and amount.replace(".", "").isdigit():
        amount = float(amount)
        amount = round(amount)
    elif isinstance(amount, float) and not math.isnan(amount):
        amount = round(amount)
    else:
        amount = "N/A"

    currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "N/A")

    from_field = transaction.get("from", {})
    to_field = transaction["to"]
    from_account = mask_account_card(from_field)
    to_account = mask_account_card(to_field)
    from_card = mask_account_card(from_field)
    to_card = mask_account_card(to_field)

    if transaction["description"] == "Перевод с карты на карту":

        return f"{date_str} {description}\n{from_card} -> {to_card}\nСумма: {amount} {currency}\n"

    elif transaction["description"] == "Перевод со счета на счет":

        return f"{date_str} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n"

    elif transaction["description"] == "Перевод организации":

        return f"{date_str} {description}\n{from_card} -> {to_account}\nСумма: {amount} {currency}\n"

    elif transaction["description"] == "Открытие вклада":

        return f"{date_str} {description}\n{to_account}\nСумма: {amount} {currency}\n"

    else:

        return f"{date_str} {description}\nСчет {to_account}\nСумма: {amount} {currency}\n"


if __name__ == "__main__":
    print(list_from_csv)
    for transaction in list_from_csv:
        print(format_transaction(transaction))
