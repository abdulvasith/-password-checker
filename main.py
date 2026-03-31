import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Include at least one special character.")

    if strength == 5:
        return "Strong ✅", remarks
    elif strength >= 3:
        return "Medium ⚠️", remarks
    else:
        return "Weak ❌", remarks


password = input("Enter your password: ")
result, feedback = check_password_strength(password)

print("\nPassword Strength:", result)

if feedback:
    print("Suggestions:")
    for f in feedback:
        print("-", f)