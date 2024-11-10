
"""Основной модуль для запуска всех функций и демонстрации обработки исключений."""

from functions import (
    validate_email,
    validate_no_cyrillic,
    safe_text_length,
    safe_get_substring,
    validate_email_and_cyrillic,
    validate_non_empty_text,
    validate_text_content,
    validate_non_empty_no_cyrillic,
    get_upper_text,
    find_character,
    check_email_domain
)


def run_all() -> None:
    """Запускает все функции для проверки обработки исключений."""
    print("Проверка email:", validate_email("agashkina@mail.com"))
    print("Проверка отсутствия кириллицы:", validate_no_cyrillic("My4thLab"))
    safe_text_length("")
    safe_get_substring("Самый крутой текст", 0, 5)
    validate_email_and_cyrillic("agashkina@mail.com", "Hello")
    validate_non_empty_text("Not_empty_at_all")
    validate_text_content("agashkina@mail.com", "Hello")
    validate_non_empty_no_cyrillic("Hello")
    print("Верхний регистр текста:", get_upper_text("hello"))
    print("Индекс символа:", find_character("example", "e"))
    print("Проверка домена email:", check_email_domain("agashkina@mail.com", "@mail.com"))


if __name__ == "__main__":
    run_all()
