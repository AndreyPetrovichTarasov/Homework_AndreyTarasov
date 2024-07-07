import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске
"""
Задаем конфигурацию логгера
"""

get_mask_card_logger = logging.getLogger("masks.get_mask_card_number")
get_mask_account_logger = logging.getLogger("masks.get_mask_account")


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты и возвращает ее маску."""
    if type(card_number) is int and len(str(card_number)) == 16:
        get_mask_card_logger.info("Создание маски для номера карты")
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"
    else:
        get_mask_card_logger.warning("Неверный формат номера карты")
        return "Некорректный номер"


def get_mask_account(account: int) -> str:
    """Функция принимает номер счета и возвращает его маску."""
    if type(account) is int:
        get_mask_account_logger.info("Создание маски для номера счета")
        return f"**{str(account)[-4:]}"
    else:
        get_mask_account_logger.warning("Неверный формат номера счета")
        return "Некорректный номер"


if __name__ == "__main__":
    print(get_mask_card_number(4534534678765433))
    print(get_mask_card_number(45345765433))
    print(get_mask_account(65435676434345676543))
    print(get_mask_account("654356543"))
