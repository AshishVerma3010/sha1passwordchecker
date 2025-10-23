SHA-1 Password Cracker
This project implements a SHA-1 password cracker function that takes a SHA-1 hash and attempts to find the original password by comparing it against a list of the top 10,000 most common passwords. It also supports option to use known salts for enhanced cracking.

Features
Loads a list of the top 10,000 passwords from top-10000-passwords.txt

Loads known salts from known-salts.txt

Cracks SHA-1 hashed passwords by comparing hashes of passwords (with and without salts)

Returns the cracked password or indicates if password is not in the database

Files
password_cracker.py: Main code file implementing the cracking function

top-10000-passwords.txt: Text file containing top 10,000 plaintext passwords (one per line)

known-salts.txt: Text file containing plaintext salt strings (one per line)

(Optional) main.py: Example script for testing the cracker function

Usage
Clone or download this repository.

Ensure top-10000-passwords.txt and known-salts.txt are in the project directory.

Run the password_cracker.py module or import the crack_sha1_hash function into your script.

Example
python
from password_cracker import crack_sha1_hash

# Crack without salts
print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"))  # Outputs: password

# Crack with salts
print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True))  # Outputs: superman
How to Test
Use the SHA-1 hashes provided in the problem statement or your own hashes. The function returns the original password if it exists in top-10000-passwords.txt or "PASSWORD NOT IN DATABASE" otherwise.
