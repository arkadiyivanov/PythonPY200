from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Некоректный тип данных")
        if not capacity_volume > 0:
            raise ValueError("Не допустимое значение")
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Некоректный тип данных")
        if not occupied_volume > 0:
            raise ValueError
        self.occupied_volume = occupied_volume
        #  TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass_1 = Glass(500, 100)
    print(glass_1)
    glass_2 = Glass(200, 200)
    print(glass_2)# TODO инициализировать два объекта типа Glass
    glass_3 = Glass('44', sd)
    print(glass_3)# TODO попробовать инициализировать не корректные объекты
