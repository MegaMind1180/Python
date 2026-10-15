def input_temperature(temp_str: str) -> int:
	return int(temp_str)

def test_temperature(test_str: str) -> None:
	try:
		temp_var = input_temperature(test_str)
		print(f"Input data is '{temp_var}'")
		print(f"Temperature is now {temp_var}°C")
	except Exception as e:
		print(f"Caught input_temperature error: {e}")
	print("All tests completed - program didn't crash!")

def main() -> None:
	print("=== Garden Temperature ===\n")
	test_temperature("25")
	print("\n")
	test_temperature("abc")
 
if __name__ == "__main__":
	main()
		
		
		

	
