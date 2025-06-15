import sys
import requests
from bs4 import BeautifulSoup
import cProfile
import pstats
import httpx

def get_input():
    if len(sys.argv) != 3:
        raise Exception("Incorrect number of arguments")
    ticker = sys.argv[1]
    table_field = sys.argv[2]
    return ticker, table_field

def get_data(ticker, table_field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials/'
    
    response = httpx.get(url, headers = {"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        raise Exception("URL does not exist or cannot be researched")

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', class_='tableBody yf-9ft13')
    if not table:
        raise Exception("Financial table not found on the page.")

    rows = table.find_all('div', class_='row lv-0 yf-t22klz')

    result = None
    for row in rows:
        header = row.find('div', {'title': True})
        if header and header['title'] == table_field:
            cells = row.find_all('div', class_=['column sticky yf-t22klz',
                                                'column yf-t22klz alt',
                                                'column yf-t22klz',
                                                'column yf-t22klz alt',
                                                'column yf-t22klz',
                                                'column yf-t22klz alt'])
            result = tuple([cell.text.strip() for cell in cells])
            break

    if not result:
        raise Exception("Table field not found on the page.")
    else:
        return result

if __name__ == '__main__':
    profile = cProfile.Profile()
    profile.enable()

    ticker, table_field = get_input()
    values = get_data(ticker, table_field)

    profile.disable()
    profile.dump_stats('financial.prof')

    try:
        with open('pstats-cumulative.txt', 'w') as f:
            p = pstats.Stats('financial.prof', stream=f)
            p.sort_stats('cumulative').print_stats(5) 
    except Exception as e:
        print(f"Error while saving profiling data: {e}")

    print(values)