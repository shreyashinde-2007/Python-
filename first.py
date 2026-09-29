while True:
    password = input("Enter a password (or type 'stop' to exit): ")

    if password.lower() == "stop":
        print("Program terminated.")
        break


    # Check password criteria
    has_lenght = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_lenght and has_upper and has_lower and has_digit:
        print("Strong Password")
    else:
        print("Weak Password")
        