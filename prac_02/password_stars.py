MIN_LENGTH = 8


def main():
    password = get_password()
    show_password(password)


def show_password(password):
    print('*' * len(password))


def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least 8 characters long. Please try again.")
        password = input("Enter your password: ")
    return password


main()
