def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты и возвращает ее маску."""
    if type(card_number) is int and len(str(card_number)) == 16:
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"
    else:
        return "Некорректный номер"


def get_mask_account(account: int) -> str:
    """Функция принимает номер счета и возвращает его маску."""
    if type(account) is int:
        return f"**{str(account)[-4:]}"
    else:
        return "Некорректный номер"
