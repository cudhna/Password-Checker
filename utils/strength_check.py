# utils/strength_check.py
import math
import requests
import hashlib
from utils.suggestion_password import suggest_password

def calc_entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for c in password): charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

def check_strength(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if password.islower() or password.isupper():
        suggestions.append("Mix uppercase and lowercase letters.")
    if password.isalpha():
        suggestions.append("Add numbers or special characters to make it stronger.")
    entropy = calc_entropy(password)
    if entropy < 28:
        strength = "Very Weak"
        level = 1
    elif entropy < 36:
        strength = "Weak"
        level = 2
    elif entropy < 60:
        strength = "Fair"
        level = 3
    else:
        strength = "Very Strong"
        level = 4
    # Suggest a sample password if not very strong yet
    if level < 4:
        suggestions.append(f"Suggested password: <code>{suggest_password(password, 12)}</code>")
    return strength, suggestions, entropy, level

pwned_cache = {}
def check_pwned(password):
    if password in pwned_cache:
        return pwned_cache[password]
    if len(password) < 8:
        pwned_cache[password] = 0
        return 0
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    for line in res.text.splitlines():
        sfx, count = line.split(':')
        if sfx == suffix:
            pwned_cache[password] = int(count)
            return int(count)
    pwned_cache[password] = 0
    return 0
