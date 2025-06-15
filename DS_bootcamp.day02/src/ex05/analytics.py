from random import randint

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

    def file_reader(self, has_header = True):
        self.check_file_validity()
        with open(self.filepath, "r") as file:
            if has_header == True:
                raw_data = file.readlines()
                data = raw_data[1:]
            else:
                data = file.readlines()
            return [list(map(int, line.strip().split(','))) for line in data]

    class Calculation:
        def __init__(self, count_data):
            self.count_data = count_data

        def counts(self):
            count_heads = sum(line[0] for line in self.count_data if line[0] == 1)
            count_tails = sum(line[1] for line in self.count_data if line[1] == 1)
            return count_heads, count_tails
            
        def Fractions(self):
            count_head, count_tails = self.counts()
            head_fraction = (count_head / (count_head + count_tails)) * 100
            tail_fraction = (count_tails / (count_head + count_tails)) * 100
            return head_fraction, tail_fraction 
        
    class Analytics(Calculation):
        def predict_random(self, num_of_steps):
            predictions = []
            for i in range(num_of_steps):
                if randint(0, 1) == 0:
                    predictions.append([0, 1])
                else:
                    predictions.append([1, 0])
            return predictions
        

        def predict_last(self):
            return self.count_data[-1]
        
        def save_file(self, data, file_name, file_extention):
            file = f"{file_name}.{file_extention}"
            with open(file, "w") as file:
                file.write(data)