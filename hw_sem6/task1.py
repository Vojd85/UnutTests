class TwoListOfNumber:
    def __init__(self, list_1: list[int|float], list_2:[int|float]):
        self.list1 = list_1
        self.list2 = list_2

    def average_value(self, lst: list[int|float]):
        if len(lst):
            return sum(lst) / len(lst)
        else:
            raise ValueError
        
    def average_comparison(self):
        if self.average_value(self.list1) > self.average_value(self.list2):
            print('Первый список имеет большее среднее значение')
        elif self.average_value(self.list2) > self.average_value(self.list1):
            print('Второй список имеет большее среднее значение')
        elif self.average_value(self.list2) == self.average_value(self.list1):
            print('Средние значения равны')

        