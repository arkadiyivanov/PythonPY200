class Glass:
    def __init__(self, material: str):
        self.material = material

    def get_material(self):
        return self.material # TODO написать класс Glass согласно условию


if __name__ == "__main__":
    glass_1 = Glass(100)
    print(glass_1.material)


