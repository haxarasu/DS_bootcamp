from random import randint
import logging 
from config import TG_TOKEN, TG_CHAT_ID
import requests

class Research:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def send_tg_message(self, message):
        logging.info(f"Sending Telegram message: {message}")
        try:
            url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
            payload = {
                "chat_id": TG_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            }
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                logging.info("Message successfully sent to Telegram")
            else:
                logging.error(f"Failed to send message to Telegram. Response: {response.text}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error while sending message to Telegram: {e}")


    def check_file_validity(self):
        logging.info(f"Checking file validity for {self.filepath}")
        try:
            with open(self.filepath, "r") as file:
                data = file.readlines()
                header = data[0].strip()
                if not header or len(header.split(',')) != 2:
                    logging.error(f"Invalid header format in file {self.filepath}")
                    raise ValueError(f"Invalid header format in file {self.filepath}")

                for line in data[1:]:
                    line = line.strip()
                    if len(line.split(',')) != 2:
                        logging.error(f"Invalid line format in file {self.filepath}")
                        raise ValueError(f"Invalid line format in file {self.filepath}")
                    if not all(part in ('0', '1') for part in line.split(',')):
                        logging.error(f"Each value in line must be either '0' or '1'. Invalid line: {line}")
                        raise ValueError(f"Each value in line must be either '0' or '1'. Invalid line: {line}")
                    
                logging.info(f"File {self.filepath} is valid")

        except FileNotFoundError:
            logging.error(f"{self.filepath} file not found")
            raise ValueError(f"{self.filepath} file not found")

    def file_reader(self, has_header = True):
        logging.info(f"Reading file {self.filepath}")
        self.check_file_validity()
        with open(self.filepath, "r") as file:
            if has_header == True:
                raw_data = file.readlines()
                data = raw_data[1:]
            else:
                data = file.readlines()
            logging.info(f"File {self.filepath} read successfully")
            return [list(map(int, line.strip().split(','))) for line in data]

    class Calculation:
        def __init__(self, count_data):
            self.count_data = count_data

        def counts(self):
            logging.info(f"Counting heads and tails in count_data")
            count_heads = sum(line[0] for line in self.count_data if line[0] == 1)
            count_tails = sum(line[1] for line in self.count_data if line[1] == 1)
            logging.info (f"Counted heads: {count_heads}, tails: {count_tails}")
            return count_heads, count_tails
            
        def Fractions(self):
            logging.info(f"Calculating head and tail fractions")
            count_heads = sum(line[0] for line in self.count_data if line[0] == 1)
            count_tails = sum(line[1] for line in self.count_data if line[1] == 1)
            head_fraction = (count_heads / (count_heads + count_tails)) * 100
            tail_fraction = (count_tails / (count_heads + count_tails)) * 100
            logging.info(f"Head fraction: {head_fraction}, tail fraction: {tail_fraction}")
            return head_fraction, tail_fraction 
        
    class Analytics(Calculation):
        def predict_random(self, num_of_steps):
            logging.info(f"Predicting random values for {num_of_steps} steps")
            predictions = []
            for i in range(num_of_steps):
                if randint(0, 1) == 0:
                    predictions.append([0, 1])
                else:
                    predictions.append([1, 0])
            logging.info(f"Predicted random values for {num_of_steps} steps")
            return predictions
        

        def predict_last(self):
            logging.info(f"Predicting last value")
            logging.info(f"Predicted last value")
            return self.count_data[-1]
        
        def save_file(self, data, file_name, file_extension):
            logging.debug(f"Calling save_file with data={data}, file_name={file_name}, file_extension={file_extension}")
            file_path = f"{file_name}.{file_extension}"
            try:
                with open(file_path, "w") as file:
                    file.write(data)
                logging.info(f"Data saved successfully to {file_path}")

            except Exception as e:
                logging.error(f"Failed to save data to {file_path}: {e}")
                print(f"Error: {e}")