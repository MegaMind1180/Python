import sys

def read_file() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("---")
            print(content, end='')
            print("---")
            lines = content.splitlines(keepends=True)
            
        print(f"File '{filename}' closed.\n")
        print(f"Changing file {filename}")
        
        new_lines = []
        for line in lines:
            stripped = line.rstrip('\r\n')
            new_lines.append(stripped + "#\n")
            
        new_content = "".join(new_lines)
        print(f"Changed file {filename}:\n{new_content}")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    new_filename = input("Enter new filename or leave empty for no changes: ").strip()
    
    if new_filename:
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(new_content)
        print(f"Preservation protocol complete. Saved to '{new_filename}'.")
    else:
        print("Save skipped. No file name provided.")

if __name__ == "__main__":
    read_file()
