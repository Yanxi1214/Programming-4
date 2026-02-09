"""
Реализации последовательности Фибоначчи с использованием различных подходов.

Этот модуль предоставляет три различных способа генерации чисел Фибоначчи:
1. Упрощённый итератор с использованием только метода __getitem__
2. Стандартный итератор с использованием методов __iter__ и __next__
3. Сопрограмма (асинхронный генератор)

Теоретическое примечание: различия между генераторами и сопрограммами
-----------------------------------------------------------------------
1. Генератор (Generator):
   - Определяется через `def` + `yield`
   - Используется для ленивой генерации значений
   - Однонаправленный поток данных (только через yield)

2. Сопрограмма (Coroutine):
   - Определяется через `async def`
   - Может содержать `await` для ожидания асинхронных операций
   - Предназначена для асинхронного программирования

3. Асинхронный генератор (Async Generator):
   - Определяется через `async def` + `yield`
   - Комбинация сопрограммы и генератора
   - Используется с `async for` для асинхронной итерации
   - Именно эта конструкция реализована в функции fibonacci_coroutine()

Все реализации включают аннотации типов, документацию (PEP-257) и тесты.
"""

from typing import AsyncGenerator
import asyncio


class SimplifiedFibonacci:
    """
    Упрощённый итератор Фибоначчи, использующий только метод __getitem__.
    
    Эта реализация позволяет получать числа Фибоначчи по индексу,
    не реализуя полный протокол итератора (__iter__, __next__).
    
    Примеры:
        >>> fib = SimplifiedFibonacci()
        >>> fib[0]
        0
        >>> fib[1]
        1
        >>> fib[10]
        55
    """
    
    def __getitem__(self, index: int) -> int:
        """Возвращает число Фибоначчи по заданному индексу."""
        if index < 0:
            raise IndexError("Индекс должен быть неотрицательным")
        
        if index == 0:
            return 0
        elif index == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, index + 1):
            a, b = b, a + b
        return b


class StandardFibonacci:
    """
    Стандартный итератор Фибоначчи с использованием методов __iter__ и __next__.
    
    Эта реализация следует полному протоколу итератора и может использоваться
    в циклах for и других контекстах, ожидающих итераторы.
    
    Примеры:
        >>> fib = StandardFibonacci()
        >>> iterator = iter(fib)
        >>> next(iterator)
        0
        >>> next(iterator)
        1
        >>> [next(iterator) for _ in range(3)]
        [1, 2, 3]
    """
    
    def __init__(self) -> None:
        """Инициализирует итератор Фибоначчи."""
        self.current = 0
        self.next_val = 1
    
    def __iter__(self) -> 'StandardFibonacci':
        """Возвращает сам объект итератора."""
        return self
    
    def __next__(self) -> int:
        """Возвращает следующее число Фибоначчи в последовательности."""
        result = self.current
        self.current, self.next_val = self.next_val, self.current + self.next_val
        return result


async def fibonacci_coroutine() -> AsyncGenerator[int, None]:
    """
    Сопрограмма (асинхронный генератор), генерирующая числа Фибоначчи.
    
    Это асинхронный генератор, который поочерёдно выдаёт числа Фибоначчи.
    Может использоваться в асинхронных циклах с помощью `async for`.
    
    Примеры:
        >>> async def example():
        ...     async for num in fibonacci_coroutine():
        ...         if num > 10:
        ...             break
        ...         print(num)
        >>> # Выведет: 0, 1, 1, 2, 3, 5, 8
    """
    current, next_val = 0, 1
    while True:
        yield current
        current, next_val = next_val, current + next_val


# Тестовые случаи
if __name__ == "__main__":
    import unittest
    
    class TestFibonacciImplementations(unittest.TestCase):
        """Тестовые случаи для всех реализаций Фибоначчи."""
        
        def test_simplified_fibonacci(self):
            """Тест упрощённой реализации Фибоначчи."""
            fib = SimplifiedFibonacci()
            
            # Проверка первых чисел Фибоначчи
            expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
            for i, expected_val in enumerate(expected):
                self.assertEqual(fib[i], expected_val)
            
            # Проверка отрицательного индекса
            with self.assertRaises(IndexError):
                fib[-1]
        
        def test_standard_fibonacci(self):
            """Тест стандартного итератора Фибоначчи."""
            fib = StandardFibonacci()
            iterator = iter(fib)
            
            # Проверка первых чисел Фибоначчи
            expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
            actual = [next(iterator) for _ in range(len(expected))]
            self.assertEqual(actual, expected)
        
        def test_fibonacci_coroutine(self):
            """Тест сопрограммы Фибоначчи."""
            async def collect_fibonacci(n: int) -> list[int]:
                """Собирает первые n чисел Фибоначчи из сопрограммы."""
                result = []
                count = 0
                async for num in fibonacci_coroutine():
                    if count >= n:
                        break
                    result.append(num)
                    count += 1
                return result
            
            # Запуск асинхронного теста
            expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            actual = asyncio.run(collect_fibonacci(10))
            self.assertEqual(actual, expected)
        
        def test_consistency_between_implementations(self):
            """Проверка согласованности результатов всех реализаций."""
            simplified = SimplifiedFibonacci()
            standard = StandardFibonacci()
            standard_iter = iter(standard)
            
            async def get_coroutine_values(n: int) -> list[int]:
                result = []
                count = 0
                async for num in fibonacci_coroutine():
                    if count >= n:
                        break
                    result.append(num)
                    count += 1
                return result
            
            n = 15
            simplified_values = [simplified[i] for i in range(n)]
            standard_values = [next(standard_iter) for _ in range(n)]
            coroutine_values = asyncio.run(get_coroutine_values(n))
            
            self.assertEqual(simplified_values, standard_values)
            self.assertEqual(standard_values, coroutine_values)
    
    # Запуск тестов
    unittest.main(verbosity=2)
