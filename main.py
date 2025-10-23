import hashlib
from hashlib import sha1
# --- Load the files ONCE ---
# It's much more efficient to read the files into lists
# when the script first starts, rather than reading them
# every time the function is called.

try:
    # Read all passwords and strip the newline character ('\n')
    with open('top-10000-passwords.txt', 'r') as f:
        top_passwords = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: 'top-10000-passwords.txt' not found.")
    top_passwords = []

try:
    # Read all salts and strip the newline character
    with open('known-salts.txt', 'r') as f:
        known_salts = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: 'known-salts.txt' not found.")
    known_salts = []


def crack_sha1_hash(hash_to_check, use_salts=False):
    """
    Cracks a SHA-1 hash by checking against a list of common passwords
    and optionally checking with known salts.
    """

    # --- 1. Check passwords without any salt ---
    for password in top_passwords:
        # Hash the password
        hashed_pass = hashlib.sha1(password.encode()).hexdigest()

        # Compare with the target hash
        if hashed_pass == hash_to_check:
            return password  # Found it!

    # --- 2. If not found and use_salts is True, check with salts ---
    if use_salts:
        for password in top_passwords:
            for salt in known_salts:

                # Test 1: Prepend the salt (salt + password)
                salted_pass_prepend = salt + password
                hashed_prepend = hashlib.sha1(
                    salted_pass_prepend.encode()).hexdigest()
                if hashed_prepend == hash_to_check:
                    return password  # Found it!

                # Test 2: Append the salt (password + salt)
                salted_pass_append = password + salt
                hashed_append = hashlib.sha1(
                    salted_pass_append.encode()).hexdigest()
                if hashed_append == hash_to_check:
                    return password  # Found it!

    # --- 3. If we get through all loops and find nothing ---
    return "PASSWORD NOT IN DATABASE"


print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"))  # 'password'
print(crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec", True))  # 'superman'



