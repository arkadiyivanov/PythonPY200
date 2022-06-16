class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self):
        """Проверяет, является ли год високосным"""
        if self.year % 4 == 0 or self.year % 100 == 0 and self.year % 400 != 0:
            return True
        else:
            return False # TODO

    def get_max_day(self):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year():
            return Date.DAY_OF_MONTH[1][self.month - 1]
        else:
            return Date.DAY_OF_MONTH[0][self.month - 1]


    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""




if __name__ == "__main__":

    data1 = Date(1, 5, 1981)
