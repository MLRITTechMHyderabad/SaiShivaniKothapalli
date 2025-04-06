import re
passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@$!%*?&#]', password):
        return False
    return True
for pwd in passwords:
    print(f"{pwd} -> {'Valid' if is_strong_password(pwd) else 'Invalid'}")
