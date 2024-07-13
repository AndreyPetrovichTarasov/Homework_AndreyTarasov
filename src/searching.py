import re
from typing import List, Dict, Any
from collections import defaultdict, Counter
from src.utils import list_from_json


def searching_description(list_transactions: List[Dict[str, Any]], user_str: str) -> List[Dict[str, Any]]:
    """
    Ищет банковские операции, в описании которых содержится заданная строка.
    :param list_transactions: список словарей с данными о банковских операциях.
    :param user_str: строка поиска.
    :return: список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(user_str), re.IGNORECASE)

    result = [transaction for transaction in list_transactions if pattern.search(transaction.get("description", ""))]

    return result


def searching_category(list_transactions: List[Dict[str, Any]], list_category: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.
    :param list_transactions: список словарей с данными о банковских операциях.
    :param list_category: список категорий операций.
    :return: словарь, где ключи — названия категорий, а значения — количество операций в каждой категории.
    """

    category_count = Counter()

    for transaction in list_transactions:
        description = str(transaction.get("description", ""))
        for category in list_category:
            if category in description:
                category_count[category] += 1

    return dict(category_count)


if __name__ == "__main__":
    # categories = ["Перевод с карты на карту", "Открытие вклада", "Перевод организации"]
    # # categories = ["Перевод с карты на карту"]
    # print(searching_category(list_from_json, categories))

    user_string = "перевод"
    print(searching_description(list_from_json, user_string))
