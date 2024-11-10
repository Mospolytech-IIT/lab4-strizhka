
"""Модуль для функций, демонстрирующих обработку исключений разного типа."""

from typing import Union
import re
from exceptions import InvalidEmailError, CyrillicCharactersError, EmptyStringError


# Задание 1. Функции принимают параметр
def validate_email(email: str) -> bool:
    """Проверяет корректность email. Генерирует исключение при неверном формате."""
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise InvalidEmailError("Неверный формат email")
    return True


def validate_no_cyrillic(text: str) -> bool:
    """Проверяет отсутствие ккириллицы в строке. Генерирует исключение при наличии."""
    if re.search(r"[а-яА-ЯёЁ]", text):
        raise CyrillicCharactersError("Строка содержит кириллические символы")
    return True


# Задание 2. Функция с общим обработчиком исключений
def safe_text_length(text: str) -> Union[int, None]:
    """Возвращает длину строки. Генерирует исключение для пустой строки."""
    try:
        if not text:
            raise EmptyStringError("Строка не должна быть пустой")
        return len(text)
    except Exception as error:  # Перехват всех ошибок для обработки специфичных ситуаций
        print("Ошибка:", error)
        return None


# Задание 3. Функция с блоком finally
def safe_get_substring(text: str, start: int, end: int) -> Union[str, None]:
    """Возвращает подстроку, обработка ошибки при выходе за границы строки."""
    try:
        return text[start:end]
    except Exception as error:
        print("Ошибка:", error)
        return None
    finally:
        print("Функция завершена")


# Задание 4. Функции с обработкой разных типов исключений
def validate_email_and_cyrillic(email: str, text: str) -> Union[bool, None]:
    """Проверяет email и отсутствие кириллицы с разными обработчиками исключений."""
    try:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidEmailError("Неверный формат email")
        if re.search(r"[а-яА-ЯёЁ]", text):
            raise CyrillicCharactersError("Текст содержит кириллические символы")
        return True
    except InvalidEmailError as error:
        print("Ошибка email:", error)
    except CyrillicCharactersError as error:
        print("Ошибка кириллицы:", error)
    finally:
        print("Проверка завершена")


def validate_non_empty_text(text: str) -> Union[str, None]:
    """Проверяет текст на пустоты. Обработка ошибок для пустого текста и пробелов."""
    try:
        if not text:
            raise EmptyStringError("Строка не должна быть пустой")
        if " " in text:
            raise ValueError("Строка не должна содержать пробелов")
        return text
    except EmptyStringError as error:
        print("Ошибка пустой строки:", error)
    except ValueError as error:
        print("Ошибка пробела:", error)
    finally:
        print("Проверка завершена")


# Задание 5. Генерация и обработка исключений
def validate_text_content(email: str, text: str) -> None:
    """Генерирует исключения для проверки email и кириллицы."""
    try:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidEmailError("Неверный формат email")
        if not text:
            raise EmptyStringError("Строка не должна быть пустой")
        if re.search(r"[а-яА-ЯёЁ]", text):
            raise CyrillicCharactersError("Текст содержит кириллические символы")
    except InvalidEmailError as error:
        print("Ошибка email:", error)
    except EmptyStringError as error:
        print("Ошибка пустой строки:", error)
    except CyrillicCharactersError as error:
        print("Ошибка кириллицы:", error)
    finally:
        print("Валидация завершена")


# Задание 7. Функция с пользовательским исключением
def validate_non_empty_no_cyrillic(text: str) -> None:
    """Генерирует исключение, если строка пуста или содержит кириллицу."""
    try:
        if not text:
            raise EmptyStringError("Строка не должна быть пустой")
        if re.search(r"[а-яА-ЯёЁ]", text):
            raise CyrillicCharactersError("Текст содержит кириллические символы")
    except (EmptyStringError, CyrillicCharactersError) as error:
        print("Пользовательское исключение:", error)
    finally:
        print("Завершение валидации строки")


# Задание 8. Дополнительные функции
def get_upper_text(text: str) -> str:
    """Преобразует текст в верхний регистр. Проверяет, что строка не пуста."""
    if not text:
        raise EmptyStringError("Строка не должна быть пустой")
    return text.upper()


def find_character(text: str, char: str) -> int:
    """Находит индекс символа в строке. Проверяет, что символ присутствует."""
    if char not in text:
        raise ValueError(f"Символ '{char}' не найден")
    return text.index(char)


def check_email_domain(email: str, domain: str) -> bool:
    """Проверяет, что email содержит указанный домен."""
    if not email.endswith(domain):
        raise InvalidEmailError(f"Email должен заканчиваться на '{domain}'")
    return True
