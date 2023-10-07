import pytest
from task1 import TwoListOfNumber

@pytest.fixture
def first_list():
    return [1, 2, 3, 4]

@pytest.fixture
def second_list():
    return [5, 6, 7, 8]

def test_class_init(first_list, second_list):
    two_list = TwoListOfNumber(first_list, second_list)
    assert two_list.list1 == first_list
    assert two_list.list2 == second_list

def test_empty_list(first_list):
    two_list = TwoListOfNumber(first_list, [])
    print(two_list.list2)
    with pytest.raises(ValueError):
        result = two_list.average_value(two_list.list2)

def test_first_avg_more(second_list, first_list, capfd):
    two_list = TwoListOfNumber(second_list, first_list)
    two_list.average_comparison()
    captured = capfd.readouterr()
    assert captured.out == 'Первый список имеет большее среднее значение\n'

def test_second_avg_more(second_list, first_list, capfd):
    two_list = TwoListOfNumber(first_list, second_list)
    two_list.average_comparison()
    captured = capfd.readouterr()
    assert captured.out == 'Второй список имеет большее среднее значение\n'

def test_avg_equal(first_list, capfd):
    two_list = TwoListOfNumber(first_list, first_list)
    two_list.average_comparison()
    captured = capfd.readouterr()
    assert captured.out == 'Средние значения равны\n'



if __name__ == '__main__':
    pytest.main(['-v'])