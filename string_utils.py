def reverse(s: str) -> str:
    """Переворачивает строку."""
    return s[::-1]

def capitalize_words(s: str) -> str:
    """Делает первую букву каждого слова заглавной."""
    return s.title()

def count_words(s: str) -> int:
    """Считает количество слов."""
    return len(s.split())

def is_palindrome(s: str) -> bool:
    """Проверяет палиндром (без учёта регистра и пробелов)."""
    r = s.lower().replace(" ", "")
    return r == r[::-1]

if __name__ == "__main__":
    # напиши свои тесты
    print('тесты')
    print(reverse('qwerty'))
    print(capitalize_words('привет мир как дела'))
    print(is_palindrome('А роза упала на лапу Азора'))
    print(is_palindrome('привет мир'))
