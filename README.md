# PassGen-Py
Python Password Generator


## Overview

`gen_pwd.py` is a Python script for generating random passwords. It allows users to specify the desired length of the password and whether or not to include special characters. By default, the password generator excludes ambiguous characters that may be difficult to distinguish (e.g., `0`, `O`, `1`, `l`, `I`), ensuring passwords are both secure and user-friendly.


## Features

- **Random Password Generation**: Generate strong, random passwords.
- **Customizable Length**: Specify the length of the password (default: 32 characters).
- **Special Characters Option**: Optionally include special characters in the password for additional security.
- **Multiple Passwords**: Generates five random passwords each time the script is run.


## Use Cases

1. **Personal Use**: Generate secure passwords for personal accounts, such as online banking, social media, or email accounts.
2. **System Administration**: System administrators can use the script to create strong passwords for user accounts or services.
3. **Development and Testing**: Developers can use the script to generate secure passwords for use in application testing or database configurations.
4. **Cybersecurity**: Enhance security by generating strong, non-guessable passwords that include special characters.


## Installation & Requirements

- Python 3.x
- No external dependencies are required.


## Usage

You can run the script directly from the command line. It accepts two optional arguments:
- **`<length>`** OR **`len=<length>`**: Specify the length of the password (default is 32)
- **`all`**: Include special characters like `!$^><-+`


### Basic Usage

1. To generate five random passwords with the default length of 32 characters:
   ```bash
   python3 gen_pwd.py
   ```

2. To specify a custom length (e.g., 16 characters):
   ```bash
   python3 gen_pwd.py 16
   ```
   OR:
   ```bash
   python3 gen_pwd.py len=16
   ```

3. To generate passwords with special characters:
   ```bash
   python3 gen_pwd.py all
   ```

4. To combine both options (e.g., 20 characters with special characters):
   ```bash
   python3 gen_pwd.py 20 all
   ```
   OR:
   ```bash
   python3 gen_pwd.py len=20 all
   ```


### Output Example

Running the script with default settings:
```bash
-    Options    -
1. KTSUMB7KkRpcpWJdjWdfqZQMY7sLVGvV
2. YbRnz9RNUEcQQu9vTHgmhoKwftMxEDuC
3. ft6WsFZkVSotBJ7Wpf2NTrkCd4YxpYfp
4. rSTcjWpZKnPukekJ7LBdM6Kj5HskwBKp
5. RjdN3rCgkzh3KJV9Q7gzf4tDZ4PGj4kr
```

Running the script with special characters:
```bash
-    Options    -
1. wxJLX3Grp9Nf^q3o<ZFMh<Y4L$<$po2y
2. bVdQRof!drGL+2BuCT^hVkBun9q>>FkL
3. DbXBskPzZyEm3+$cVcnbmkeuLP!Rwr^e
4. mPVMXn5JaRtgeBDYf7W234-3qF4V$m<V
5. CPVzTb+LWqyGHsfCzhwvkLx4Y9<A4wJP
```


## Functionality Overview

- **`generate_password(length, include_special_chars)`**: Generates a random password of the specified length. If `include_special_chars` is set to `True`, it ensures that at least one special character is included in the password.
- **`parse_arguments()`**: Parses command-line arguments to get the desired password length and whether or not to include special characters.
- **`main()`**: Generates and prints five random passwords based on the parsed arguments.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
