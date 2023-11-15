import msvcrt
import csv
import bcrypt


def check_password(stored_hashed_password, stored_salt, entered_password):
    # Verify if the entered password matches the stored hashed password with the provided salt
    hashed_password = bcrypt.hashpw(entered_password.encode('utf-8'), stored_salt.encode('utf-8'))
    return hashed_password == stored_hashed_password.encode('utf-8')

def getpass(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        key = msvcrt.getch()
        key = key.decode('utf-8')

        if key == '\r' or key == '\n':
            print()
            break
        elif key == '\b':
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += key
            print('*', end='', flush=True)

    return password

def login(username, password):
    file_path = "login_details.csv"

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                stored_hashed_password = row["hash_pass"]
                stored_salt = row["salt"]
                if check_password(stored_hashed_password, stored_salt, password):
                    return True

    return False