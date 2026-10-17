class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def check_garden_status(situation: int) -> None:
    if situation == 1:
        raise PlantError()
    elif situation == 2:
        raise WaterError("The irrigation tank is completely empty!")
    elif situation == 3:
        raise GardenError("General sensor failure in the greenhouse.")

def test_custom_error_types() -> None:
    for i in range(1, 4):
        print(f"--- Testing situation {i} ---")
        try:
            check_garden_status(i)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except GardenError as e:
            print(f"Caught general GardenError: {e}")
        print()

if __name__ == "__main__":
    test_custom_error_types()
