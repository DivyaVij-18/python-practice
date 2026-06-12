import secrets 
import string
password= [ 
    secrets.choice(string.ascii_uppercase),
    secrets.choice(string.ascii_lowercase),
    secrets.choice(string.digits),
    secrets.choice("!@#$%^&*()")
]
alphabet = (
    string.ascii_letters +
    string.digits +
    "!@#$%^&*()"
)

for _ in range(12):
    password.append(secrets.choice(alphabet))
secrets.SystemRandom().shuffle(password)
print(''.join(password))
