def validate_input(new_text):
    """
    validation = root.register(validate_input)\n
    entry = tk.Entry(root, validate="key", validatecommand=(validation, '%P'))
    """
    if not new_text:
        return True
    try:
        float(new_text)
        return True
    except ValueError:
        return False
