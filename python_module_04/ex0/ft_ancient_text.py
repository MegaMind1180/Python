import sys

def read_file() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit()
        
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("---")
            print(content, end='')
            print("---")
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")

if __name__ == "__main__":
    read_file()
