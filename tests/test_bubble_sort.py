import pytest
from lib import sort


class TestBubbleSort:

    # Параметризованный тест для различных входных данных
    @pytest.mark.parametrize("input_data, expected_result", [
        ([], []),
        ([5], [5]),
        ([4, 3, 2, 6, 12], [2, 3, 4, 6, 12]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
    ])
    def test_bubble_sort(self, input_data, expected_result):
        actual_result = sort(input_data)
        assert actual_result == expected_result

    # Тест для попытки сортировки списка, содержащего некорректные значения
    @pytest.mark.parametrize("input_data", [(4, 3, None, 6, 12), (4, 3, "2", 6, 12)])
    def test_bubble_sort_with_invalid_input(self, input_data):
        with pytest.raises(TypeError):
            sort(list(input_data))