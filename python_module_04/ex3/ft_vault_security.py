def secure_archive(filename: str, action: str | int = 'read', content_to_write: str = "") -> tuple[bool, str]:
    try:
        if action == 'read' or action == 1:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return (True, content)
        elif action == 'write' or action == 2:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content_to_write)
            return (True, content_to_write)
        else:
            return (False, "Unknown action specified.")
    except Exception as e:
        return (False, str(e))
