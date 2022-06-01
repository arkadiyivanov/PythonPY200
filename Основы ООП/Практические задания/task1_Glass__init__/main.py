from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not occupied_volume > 0:
            raise ValueError
        self.occupied_volume = occupied_volume
        #  TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass_1 = Glass(100, 200)
    glass_2 = Glass(1000, 300)# TODO инициализировать два объекта типа Glass

    incorrect_capacity_volume_type = ...
    incorrect_occupied_volume_value = ...
    # TODO попробовать инициализировать не корректные объекты
