class Research:
    def file_reader(self):
        file = "../ex00/data.csv"
        try:
            with open(file, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise ValueError(f"{file} file not found")


if __name__ == "__main__":
    try:
        print(Research().file_reader())
    except ValueError as e:
        print(f"Error: {e}")