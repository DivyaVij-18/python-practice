import string
password=input("Enter a password: ")
has_upper=False
has_lower=False
has_digit=False
has_symbol=False
for char in password:
    if char in string.ascii_uppercase:
        has_upper=True
    elif char in string.ascii_lowercase:
        has_lower=True
    elif char in string.digits:
        has_digit=True
    elif char in "!@#$%^&*()":
        has_symbol=True
if ( len(password)>= 8 and has_symbol and has_digit and has_lower and has_upper) :
    print("Strong Password")
else:
    print("Weak password: ")
if not has_upper:
    print("Missing uppercase letter")

if not has_lower:
    print("Missing lowercase letter")

if not has_digit:
    print("Missing digit")

if not has_symbol:
    print("Missing symbol")

if len(password) < 8:
    print("Password too short")