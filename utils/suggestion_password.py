import random
import string

def suggest_password(password, length=12):
    base = password.capitalize()
    num = str(random.randint(10, 99))
    specials = '!@#$%^&*()'
    special = random.choice(specials)
    extra = ''
    if not any(c.isupper() for c in base):
        extra += random.choice(string.ascii_uppercase)
    if not any(c.islower() for c in base):
        extra += random.choice(string.ascii_lowercase)
    suggestion = (base + extra + num + special)
    while len(suggestion) < length:
        suggestion += random.choice(string.ascii_letters + string.digits + specials)
    return suggestion[:length]