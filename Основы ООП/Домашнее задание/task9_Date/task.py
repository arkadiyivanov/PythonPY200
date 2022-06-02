class Data:
    def __init__(self, day: int, manth: int, year: int):
        if not isinstance(day, int):
            raise TypeError
        if day < 10:
            day = '0' + str(day)
        self.day = day
        if not isinstance(manth, int):
            raise TypeError
        if manth < 10:
            manth = '0' + str(manth)
        elif manth > 12:
            raise ValueError
        self.manth = manth
        if not isinstance(year, int):
            raise TypeError
        self.year = year

    def __repr__(self) -> str:
        return f"Data({self.day}, {self.manth}, {self.year})"

    def __str__(self) -> str:
        return f"{self.day}/{self.manth}/{self.year}"


if __name__ == '__main__':
    print("Введите дату своего рождения")
    d = int(input("Число"))
    m = int(input("Месяц"))
    y = int(input("Год"))

    data_1 = Data(d, m, y)
    data_2 = Data(11, 12, 1981)
    data_3 = Data(2,1,1981)

    print(data_1)
    print(data_2)
    print(data_3)
