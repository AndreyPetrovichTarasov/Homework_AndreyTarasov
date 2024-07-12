def user_input():
    while True:
        user_str = input("Введите число: ")
        if user_str in ["1", "2", "3"]:
            return user_str
        else:
            print("Ошибка ввода! Попробуйте еще.")


def choice_status():
    while True:
        user_str = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки "
                         "статусы: EXECUTED, CANCELED, PENDING: ").lower()
        if user_str in ["executed", "canceled", "pending"]:
            return user_str
        else:
            print(f"Статус операции '{user_str}' недоступен.")