from typing import List, Dict


def filter_by_state(list_id: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Функция сортировки списка по ключу "state"."""
    sorted_list_id = [dict_id for dict_id in list_id if dict_id["state"] == state]
    return sorted_list_id


def sort_by_date(list_id: List[Dict], reverse: bool = False) -> List[Dict]:
    """Функция сортировки списка по дате (по возрастанию или убыванию)."""
    sorted_list = sorted(list_id, key=lambda dict_id: dict_id["date"], reverse=reverse)
    return sorted_list
