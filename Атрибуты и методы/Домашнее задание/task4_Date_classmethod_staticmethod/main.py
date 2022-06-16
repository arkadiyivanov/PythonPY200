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

    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""

        if (self.year % 4 == 0) and (self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        else:
            return False




    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year=True):
            self.month = Date.DAY_OF_MONTH[0]
        else:
            self.month = Date.DAY_OF_MONTH[1]

        

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


data1 = Date(1,5,1981)
data1.get_max_day(5,1982)





