import re

print("=" * 40)
print("   PASSWORD COMPLEXITY CHECKER")
print("=" * 40)

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
else:
    print("❌ Password should be at least 8 characters long.")

if re.search("[A-Z]", password):
    score += 1
else:
    print("❌ Add at least one uppercase letter.")

if re.search("[a-z]", password):
    score += 1
else:
    print("❌ Add at least one lowercase letter.")

if re.search("[0-9]", password):
    score += 1
else:
    print("❌ Add at least one number.")

if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    print("❌ Add at least one special character.")

common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "admin",
    "qwerty"
]

if password.lower() in common_passwords:
    print("❌ This is a common password. Choose another one.")
else:
    score += 1

print("\nScore:", score, "/6")

if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Moderate")
else:
    print("Strength: Strong")
