import sys

def get_emails():
    with open(sys.argv[1], "r") as file:
        return file.readlines()


def add_email(email):
    name = email.split('@')[0].split('.')[0].capitalize()
    surname = email.split('@')[0].split('.')[1].capitalize()

    with open("employees.tsv", "a") as file:
        file.write(f"{name}\t{surname}\t{email.strip()}\n")


def set_notepad():
    for note in get_emails():
        add_email(note)


if __name__ == "__main__":
    set_notepad()
