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


def transforming_operations():
    """
    Функцмя возвращает список транзакций в виде словарей, преобразованный из json-файла.
    """

    filename = Path(ROOT_PATH, "operations.json")
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


def from_csv():
    df = pd.read_csv(Path(ROOT_PATH, "transactions.csv"), delimiter=";")

    df["operationAmount"] = df.apply(
        lambda row: {"amount": row["amount"], "currensy": {"name": row["currency_name"], "code": row["currency_code"]}},
        axis=1)

    new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
    df = df[new_col_order]
    list_of_dicts = df.to_dict(orient='records')

    return list_of_dicts


def from_xlsx():
    df = pd.read_excel(Path(ROOT_PATH, "transactions_excel.xlsx"))

    df["operationAmount"] = df.apply(
        lambda row: {"amount": row["amount"], "currensy": {"name": row["currency_name"], "code": row["currency_code"]}},
        axis=1)

    new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
    df = df[new_col_order]
    list_of_dicts = df.to_dict(orient='records')

    return list_of_dicts


# Применение функции
# if __name__ == "__main__":

# operations_path = Path(ROOT_PATH, "operations.json")
# operations_path = Path(ROOT_PATH, "transactions.csv")
# operations_path = Path(ROOT_PATH, "transactions_excel.xlsx")


list_from_json = transforming_operations()
list_from_csv = from_csv()
list_from_excel = from_xlsx()

# print(returned_list)
# print(returned_list[3:10])
