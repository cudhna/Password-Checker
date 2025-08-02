import re

def is_blank(password: str):
    """Check if password is empty or contains only spaces."""
    return not password or password.strip() == ''

def check_regex(password: str):
    """
    Return a list of basic issues (optional to include/remove any check):
    - Minimum length >= 8 characters
    - At least 1 uppercase, 1 lowercase, 1 digit, 1 special character
    """
    issues = []
    if len(password) < 8:
        issues.append("Password must be at least 8 characters.")
    if not re.search(r'[a-z]', password):
        issues.append("Missing lowercase letter (a-z).")
    if not re.search(r'[A-Z]', password):
        issues.append("Missing uppercase letter (A-Z).")
    if not re.search(r'[0-9]', password):
        issues.append("Missing digit (0-9).")
    if not re.search(r'[^a-zA-Z0-9]', password):
        issues.append("Missing special character.")
    return issues
