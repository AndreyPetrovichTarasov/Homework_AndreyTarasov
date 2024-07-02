import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from data.config import ROOT_PATH


def transforming_operations(filename):
    """
    Функцмя возвращает список транзакций в виде словарей, преобразованный из json-файла.
    """
    try:
        with (open(filename, encoding="utf-8") as file_json):
            content = file_json.read().strip()
            if not content:
                return []
            list_dicts = json.loads(content)

            if not isinstance(list_dicts, list):
                return []

            return list_dicts

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# Применение функции
if __name__ == "__main__":
    operations_path = Path(ROOT_PATH, "operations.json")
    returned_list = transforming_operations(operations_path)
    print(returned_list)
    print(type(returned_list))
    print(len(returned_list))
