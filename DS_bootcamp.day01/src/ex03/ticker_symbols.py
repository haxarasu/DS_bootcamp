import sys

def get_company_info(stock_symbol):
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

    if len(sys.argv) != 2:
        return 1

    stock_symbol = sys.argv[1].upper()  # Преобразуем тикер в верхний регистр

    # Получаем название компании
    company_name = [name for name, symbol in COMPANIES.items() if symbol == stock_symbol]

    if company_name:
        # Получаем цену акций
        stock_price = STOCKS.get(stock_symbol)
        print(f"{company_name[0]} {stock_price}")
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    get_company_info(sys.argv[1])