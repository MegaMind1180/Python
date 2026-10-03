class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def track_grow(self):
            self._grow_calls += 1

        def track_age(self):
            self._age_calls += 1

        def track_show(self):
            self._show_calls += 1

        def display(self):
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show", end="")

    def __init__(self, name: str, height: float = 0.0, age: int = 0):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.stats = self.Stats()
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age

    def get_age(self) -> int:
        return self._age

    def grow(self, cm: float) -> None:
        self.stats.track_grow()
        if cm > 0:
            self.set_height(self.get_height() + cm)

    def age(self, days: int) -> None:
        self.stats.track_age()
        if days > 0:
            self.set_age(self.get_age() + days)

    def show(self) -> None:
        self.stats.track_show()
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls(name="Unknown plant", height=0.0, age=0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def track_shade(self):
            self._shade_calls += 1

        def display(self):
            super().display()
            print(f"\n{self._shade_calls} shade", end="")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.stats.track_shade()
        print(f"Tree {self.name} now produces a shade of {self.get_height()}cm long and {self.trunk_diameter}cm wide.")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, seeds_count: int = 0):
        super().__init__(name, height, age, color)
        self.seeds_count = seeds_count

    def bloom(self) -> None:
        super().bloom()
        if self.seeds_count == 0:
            self.seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


def display_plant_analytics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()
    print()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("\n")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_analytics(rose)
    print("\n")

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_analytics(rose)
    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_analytics(oak)
    print("\n")

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_analytics(oak)
    print("\n")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("\n")

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_analytics(sunflower)
    print("\n")

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_analytics(anon)
