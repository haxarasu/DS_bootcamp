import sys

COMPANIES = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'tesla': 'TSLA',
    'nokia': 'NOK'
}
STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}


def get_argv():
    if len(sys.argv) >= 2:
        return sys.argv[1:]
    else:
        sys.exit(1)


def get_key(dict, value):
    for key, val in dict.items():
        if val == value:
            return key
    return None


def two_commas(data): 
    data_str = ' '.join(data)
    formatted_data_str = data_str.replace(' ', '')

    prev = None
    for symbol in formatted_data_str:
        if symbol == ',':
            if prev == ',':
                return False
        prev = symbol
    return formatted_data_str.split(',')


def def_data(data):
    if not two_commas(data):
        sys.exit(1)

    for item in two_commas(data):
        item_lower = item.lower()
        item_upper = item.upper()

        if item_lower in COMPANIES:
            print(f"{item} stock price is {STOCKS[COMPANIES[item_lower]]}")
        elif item_upper in STOCKS:
            print(f"{item} is a ticker symbol for {get_key(COMPANIES, item_upper)}")
        else:
            print(f"{item} is an unknown company or an unknown ticker symbol")

if __name__ == "__main__":
    def_data(get_argv())