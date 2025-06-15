import sys

def get_data():
    if len(sys.argv) != 4:
        print("Incorrect number of arguments. Expected 3 arguments.")
        sys.exit(1)
    return sys.argv[1], sys.argv[2], int(sys.argv[3])


def check_cyrillic(text):
    if any('А' <= char <= 'я' or 'Ё' <= char <= 'ё' for char in text):
        raise ValueError("The script does not support your language yet.")


def shift_character(char, shift_value, action):
    base = ord('A') if char.isupper() else ord('a')
    if action == "encode":
        return chr((ord(char) - base + shift_value) % 26 + base)
    elif action == "decode":
        return chr((ord(char) - base - shift_value) % 26 + base)


def process(action, data, shift_value):
    result = ""
    for char in data:
        if char.isalpha():
            result += shift_character(char, shift_value, action)
        else:
            result += char
    return result


if __name__ == "__main__":
    action, data, shift_value = get_data()
    check_cyrillic(data)
    print(process(action, data, shift_value))