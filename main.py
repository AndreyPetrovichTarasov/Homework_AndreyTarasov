import logging
import re
from src.user_input import user_input, choice_status
from src.utils import transforming_operations, from_csv, from_xlsx
from src.processing import filter_by_state, sort_by_date
from src.searching import searching_description
from src.processing import format_transaction


def main():
    """
    Точка входа в программу, которая отвечает за основную логику проекта и связывает функциональности между собой.
    :return: None
    """

    greeting = """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""

    print(greeting)
    print()
    user_answer = user_input()
    if user_answer == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = transforming_operations()
    elif user_answer == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = from_csv()
    elif user_answer == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = from_xlsx()

    user_answer_status = choice_status().upper()

    transactions_sorted = filter_by_state(transactions, user_answer_status)

    print(f"Операции отфильтрованы по статусу {user_answer_status}")
    print()

    while True:
        user_answer_for_date = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if user_answer_for_date == "да":
            while True:
                user_answer_for_date_reverse = input("Отсортировать по возрастанию или по убыванию?: ").lower()
                if user_answer_for_date_reverse == "по возрастанию":
                    transactions_sorted = sort_by_date(transactions_sorted, reverse=False)
                    break
                elif user_answer_for_date_reverse == "по убыванию":
                    transactions_sorted = sort_by_date(transactions_sorted)
                    break
                else:
                    print("Ошибка ввода! Попробуйте ещё раз.")
            break
        elif user_answer_for_date == "нет":
            break
        else:
            print("Ошибка ввода! Попробуйте ещё раз.")

    while True:
        user_answer_for_currency = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if user_answer_for_currency == "да":
            transactions_sorted = [transaction for transaction in transactions_sorted if
                                   transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == "RUB"]
            break
        elif user_answer_for_currency == "нет":
            break
        else:
            print("Ошибка ввода! Попробуйте ещё раз.")

    while True:
        user_answer_for_keyword = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
        if user_answer_for_keyword == "да":
            user_keyword = input("Введите ключевое слово: ")
            transactions_sorted = searching_description(transactions_sorted, user_keyword)
            break
        elif user_answer_for_keyword == "нет":
            break
        else:
            print("Ошибка ввода! Попробуйте ещё раз.")

    print("Распечатываю итоговый список транзакций...")
    print(transactions_sorted)

    if len(transactions_sorted) > 0:
        print(f"Всего банковских операций в выборке: {len(transactions_sorted)}\n")
        # print(transactions_sorted)
        for transaction in transactions_sorted:
            print(format_transaction(transaction))
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


main()
