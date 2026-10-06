# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b

def is_prime(n: int) -> bool:
    """Проверяет, простое ли число."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Тестовый блок
if __name__ == "__main__":
    print("Тестируем math_utils")
    print(add(2, 3))          # 5
    print(subtract(10, 4))    # 6
    print(multiply(3, 4))     # 12
    print(divide(10, 2))      # 5.0
    print(is_prime(7))        # True
    print(is_prime(10))       # False