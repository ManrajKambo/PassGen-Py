#!/usr/bin/python3 -u

import random
import string
import sys

def generate_password(length, include_special_chars):
	# Exclude characters that my cause some confusion with some fonts
	exclude_chars = '0O1liI'
	characters = ''.join(c for c in string.ascii_letters + string.digits if c not in exclude_chars)
	if include_special_chars:
		special_chars = "!$^><-+"
		characters += special_chars

	password = ''.join(random.choice(characters) for _ in range(length))

	if include_special_chars:
		# Ensure at least one special character is in the password
		special_char = random.choice(special_chars)
		password = list(password)
		random_index = random.randint(0, length - 1)
		password[random_index] = special_char
		password = ''.join(password)

	return password

def parse_arguments():
  # Default length is 32 characters
	length = 32
	include_special_chars = False

	for arg in sys.argv[1:]:
		if arg.startswith("len="):
			length = int(arg.split("=")[1])
		elif arg.isdigit():
			length = int(arg)
		elif arg == "all":
			include_special_chars = True

	return length, include_special_chars

def main():
	str = f"\n\n{'-':<5s}Options{'-':>5s}\n"
	for x in range(0,5):
		length, include_special_chars = parse_arguments()
		password = generate_password(length, include_special_chars)
		str += f"{x+1}. {password}\n"

	print(f"{str}\n")

if __name__ == "__main__":
	main()
