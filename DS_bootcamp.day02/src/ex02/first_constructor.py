import sys

class Research:
    def __init__(self, filepath):
        self.filepath = filepath

    def check_file_validity(self):
        try:
            with open(self.filepath, "r") as file:
                data = file.readlines()
                header = data[0].strip()
                if not header or len(header.split(',')) != 2:
                    raise ValueError(f"invalid header format in file {self.filepath}")

                for line in data[1:]:
                    line = line.strip()
                    if len(line.split(',')) != 2:
                        raise ValueError(f"invalid line format in file {self.filepath}")
                    if not all(part in ('0', '1') for part in line.split(',')):
                        raise ValueError(f"Each value in line must be either '0' or '1'. Invalid line: {line}")
        except FileNotFoundError:
            raise ValueError(f"{self.filepath} file not found")

    def file_reader(self):
        self.check_file_validity()
        with open(self.filepath, "r") as file:
            return file.read()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: No file path provided or too many arguments provided.")
        sys.exit(1)

    fileargv = sys.argv[1]
    try:
        research_instance = Research(fileargv)
        print(research_instance.file_reader())
    except ValueError as e:
        print(f"Error: {e}")