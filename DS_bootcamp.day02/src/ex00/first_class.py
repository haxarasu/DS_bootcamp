class Must_read:
    file = "data.csv"
    with open(file, "r") as file:
        print(file.read())


if __name__ == "__main__":
    try:
        Must_read()
    except ValueError as e:
        print(f"Error: {e}")