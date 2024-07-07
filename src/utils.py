import json
import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from data.config import ROOT_PATH

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
"""
Задаем конфигурацию логгера
"""

transforming_operations_logger = logging.getLogger("utils.transforming_operations")


def transforming_operations(filename):
    """
    Функцмя возвращает список транзакций в виде словарей, преобразованный из json-файла.
    """
    try:
        transforming_operations_logger.info("запуск приложения")
        with open(filename, encoding="utf-8") as file_json:
            content = file_json.read().strip()
            if not content:
                transforming_operations_logger.warning("Пустой список")
                return []
            list_dicts = json.loads(content)
            transforming_operations_logger.info("Преобразование списка в json формат")

            if not isinstance(list_dicts, list):
                transforming_operations_logger.warning("На входе не список")
                return []

            return list_dicts

    except FileNotFoundError:
        transforming_operations_logger.error("Файл не найден")
        return []
    except json.JSONDecodeError:
        transforming_operations_logger.error("Некорректный формат json")
        return []


# Применение функции
if __name__ == "__main__":
    operations_path = Path(ROOT_PATH, "operations.json")
    returned_list = transforming_operations(operations_path)
    print(returned_list)
