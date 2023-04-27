import random

def main():
    available_numbers = "0123456789"
    available_lowercase = "abcdefghijklmnopqrstuvwxyz"
    available_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    available_symbols = "!@#$%^&*()/?"

    password = ""

    length = input("Enter the password length: ")

    if not length.isdigit():
        print("Invalid response.")
        return

    length = int(length)

    wants_numbers = input("Do you want numbers in the password? (y, n): ")
    wants_numbers = wants_numbers.lower()

    if wants_numbers not in ["y", "n"]:
        print("Invalid response.")
        return

    wants_lowercase = input("Do you want lowercase letters in the password? (y, n): ")
    wants_lowercase = wants_lowercase.lower()

    if wants_lowercase not in ["y", "n"]:
        print("Invalid response.")
        return

    wants_uppercase = input("Do you want uppercase letters in the password? (y, n): ")
    wants_uppercase = wants_uppercase.lower()

    if wants_uppercase not in ["y", "n"]:
        print("Invalid response.")
        return

    wants_symbols = input("Do you want symbols in the password? (y, n): ")
    wants_symbols = wants_symbols.lower()

    if wants_symbols not in ["y", "n"]:
        print("Invalid response.")
        return

    amount = input("Enter the amount of passwords: ")

    if not amount.isdigit():
        print("Invalid response.")
        return

    amount = int(amount)

    char_sets = []

    if wants_numbers == "y":
        char_sets.append(available_numbers)

    if wants_lowercase == "y":
        char_sets.append(available_lowercase)

    if wants_uppercase == "y":
        char_sets.append(available_uppercase)

    if wants_symbols == "y":
        char_sets.append(available_symbols)

    if not char_sets:
        print("Must select at least one character set.")
        return

    for i in range(amount):
        password = "".join(random.choices("".join(char_sets), k = length))

        if amount == 1:
            print(f"Password: {password}")
        else:
            print(f"Password #{i+1}: {password}\n")


        save_file = input("Do you want to save the password to a file? (y, n): ")
        save_file = save_file.lower()

        if save_file not in ["y", "n"]:
            print("Invalid response.")
            return

        if save_file == "y":
            file_name = input("Enter the desired file name: ")

            with open(f"{file_name}.txt", "a") as file:
                if amount == 1:
                    file.write(f"Password: {password}")
                else:
                    file.write(f"Password #{i+1}: {password}\n")
        else:
            continue

if __name__ == "__main__":
    main()
