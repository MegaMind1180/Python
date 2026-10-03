class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant.name}: {plant.get_height()}cm, {plant.get_age()} days old")

    plant.set_height(25.0)
    print(f"Height updated: {int(plant.get_height())}cm")

    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days")

    plant.set_height(-5.0)
    plant.set_age(-10)

    print(f"Current state: {plant.name}: {plant.get_height()}cm, {plant.get_age()} days old")
