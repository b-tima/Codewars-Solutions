def alphanumeric(password):
    return all(c.lower() in "abcdefghijklmnopqrstuvwxyz0123456789" for c in password) if len(password) > 0 else False