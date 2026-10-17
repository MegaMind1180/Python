class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def water_plant(plant_name: str) -> None:
    temp = plant_name.capitalize()
    if temp != plant_name:
        raise PlantError(f"PlantError: Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")

def test_watering_system(plant_list: list) -> None:
    print("Opening water system!")
    try:
        for name in plant_list:
            water_plant(name)
    except Exception as e:
        print(f"Caught {e}")
        return
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    print("Testing valid inputs\n")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid inputs\n")
    test_watering_system(["Tomato", "lettuce", "carrots"])
