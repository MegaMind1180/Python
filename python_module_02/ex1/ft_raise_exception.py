def input_temperature(temp_str: str) -> int:
	try:
		temp = int(temp_str)
	except Exception as e:
		raise
	if (temp < 0):
		raise ValueError (f"{temp}°C is to cold for plants (min 0°C)")
	elif (temp > 40):
		raise ValueError (f"{temp}°C is to hot for plants (max 40°C)")
	return(temp)

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
	print("\n")
	test_temperature("41")
	print("\n")
	test_temperature("-1")
 
if __name__ == "__main__":
	main()
