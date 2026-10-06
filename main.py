# main.py
from math_utils import add, is_prime
from string_utils import reverse, is_palindrome, count_words
import json

print(add(5, 7))                    # 12
print(is_prime(13))                 # True
print(reverse("Python"))            # "nohtyP"
print(is_palindrome("шалаш"))       # True



data = {"name": "Аня", "age": 25, "city": "Москва"}

# Запись
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Чтение
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
print(loaded["name"])

print(count_words("hello world"))      # 2
print(count_words("hello  world"))     # 2 — двойной пробел не ломает
print(count_words("hello\tworld\nfoo")) # 3 — табы и переводы строк
print(count_words(""))                 # 0