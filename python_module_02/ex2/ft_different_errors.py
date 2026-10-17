def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        temp = int("abc")
    elif operation_number == 1:
        temp = 1 / 0
    elif operation_number == 2:
        temp = open("mich_gibts_nicht;).txt")
    elif operation_number == 3:
        print(1 + "str")
    elif operation_number == 4:
        print("Operation completed successfully")

def test_error_types() -> None:
    for n in range(4):
        print(f"Testing operation {n}!")
        try:
            garden_operations(n)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        except Exception as e:
            print(f"Caught Error: {e}")
        print()

if __name__ == "__main__":
    test_error_types()
		
