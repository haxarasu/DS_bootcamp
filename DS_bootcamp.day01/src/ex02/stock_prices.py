import sys

def get_stock_price(company_name):
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

    # Проверяем, что передан ровно один аргумент
    if len(sys.argv) != 2:
        return 1

    company_name = sys.argv[1].lower()  # Преобразуем название компании в нижний регистр

    # Получаем символ компании
    stock_symbol = COMPANIES.get(company_name)

    if stock_symbol:
        # Получаем цену акций
        stock_price = STOCKS.get(stock_symbol)
        print(stock_price)
    else:
        print("Unknown company")

if __name__ == '__main__':
    get_stock_price(sys.argv[1])