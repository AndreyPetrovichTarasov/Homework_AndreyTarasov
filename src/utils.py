import json
import logging
import sys
from pathlib import Path
import csv
import pandas as pd
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
    if filename.suffix == ".json":
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
    elif filename.suffix == ".csv":
        with open(filename, encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=";")
            csv_to_dict = list(reader)

            return csv_to_dict

    elif filename.suffix == ".xlsx":
        excel_data = pd.read_excel(filename)
        excel_to_dict = excel_data.to_dict(orient="records")

        return excel_to_dict


# Применение функции
if __name__ == "__main__":
    # operations_path = Path(ROOT_PATH, "operations.json")
    operations_path = Path(ROOT_PATH, "transactions.csv")
    # operations_path = Path(ROOT_PATH, "transactions_excel.xlsx")

    returned_list = transforming_operations(operations_path)
    print(returned_list)
