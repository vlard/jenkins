import bcrypt
import sys
password = sys.argv[1]
print bcrypt.hashpw(password, bcrypt.gensalt(rounds=10, prefix=b"2a"))
