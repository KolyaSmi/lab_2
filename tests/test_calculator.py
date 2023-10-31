import pytest
from lib import calculator


class TestCalculator:

    # Параметризованный тест для различных операций и ожидаемых результатов
    @pytest.mark.parametrize("a, b, operation, expected_result", [
        (4, 5, '+', 9),
        (10, 3, '-', 7),
        (6, 2, '*', 12),
        (8, 2, '/', 4),
    ])
    def test_calculator_positive(self, a, b, operation, expected_result):
        actual_result = calculator(a, b, operation)
        assert actual_result == expected_result

    # Тест для неподдерживаемой операции
    def test_calculator_invalid_operation(self):
        with pytest.raises(ValueError):
            calculator(4, 5, '%')

    # Тест для деления на ноль
    def test_calculator_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator(4, 0, '/')
