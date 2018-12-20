import bcrypt
print bcrypt.hashpw("hello123", bcrypt.gensalt(rounds=10, prefix=b"2a"))
