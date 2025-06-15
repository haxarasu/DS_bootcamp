import sys
import pytest
from unittest.mock import patch
from financial import get_data
from financial import get_input # файл financial.py из ex03 нужно перетащить в ex05 чтобы заработало

TEST_TICKER = 'AAPL'
TEST_TABLE_FIELD = 'Total Revenue'

@patch('financial.requests.get')
def test_get_data_success(mock_get):
    class MockResponse:
        status_code = 200
        text = '<div class="tableBody yf-9ft13"><div class="row lv-0 yf-t22klz">' \
               '<div title="Total Revenue" class="column sticky yf-t22klz">100B</div>' \
               '<div class="column yf-t22klz">2021</div>' \
               '<div class="column yf-t22klz">2020</div>' \
               '</div></div>'

    mock_get.return_value = MockResponse()
    
    result = get_data(TEST_TICKER, TEST_TABLE_FIELD)
    assert result == ('100B', '2021', '2020')


@patch('financial.requests.get')
def test_get_data_return_type(mock_get):
    class MockResponse:
        status_code = 200
        text = '<div class="tableBody yf-9ft13"><div class="row lv-0 yf-t22klz">' \
               '<div title="Total Revenue" class="column sticky yf-t22klz">100B</div>' \
               '<div class="column yf-t22klz">2021</div>' \
               '<div class="column yf-t22klz">2020</div>' \
               '</div></div>'

    mock_get.return_value = MockResponse()
    
    result = get_data(TEST_TICKER, TEST_TABLE_FIELD)
    assert isinstance(result, tuple)


@patch('financial.requests.get')
def test_get_data_invalid_ticker(mock_get):
    class MockResponse:
        status_code = 404

    mock_get.return_value = MockResponse()
    
    with pytest.raises(Exception, match="URL does not exist or cannot be researched"):
        get_data('INVALID_TICKER', TEST_TABLE_FIELD)


@patch('financial.requests.get')
def test_get_data_invalid_table_field(mock_get):
    class MockResponse:
        status_code = 200
        text = '<div class="tableBody yf-9ft13"><div class="row lv-0 yf-t22klz">' \
               '<div title="Total Revenue" class="column sticky yf-t22klz">100B</div>' \
               '<div class="column yf-t22klz">2021</div>' \
               '<div class="column yf-t22klz">2020</div>' \
               '</div></div>'

    mock_get.return_value = MockResponse()
    
    with pytest.raises(Exception, match="Table field not found on the page."):
        get_data(TEST_TICKER, 'Invalid Field')


def test_get_input_success():
    test_args = ['financial.py', 'AAPL', 'Total Revenue']
    with patch.object(sys, 'argv', test_args):
        ticker, table_field = get_input()
        assert ticker == 'AAPL'
        assert table_field == 'Total Revenue'


def test_get_input_too_few_arguments():
    test_args = ['financial.py', 'AAPL']
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(Exception, match="Incorrect number of arguments"):
            get_input()


def test_get_input_too_many_arguments():
    test_args = ['financial.py', 'AAPL', 'Total Revenue', 'Extra Argument']
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(Exception, match="Incorrect number of arguments"):
            get_input()

if __name__ == '__main__':
    pytest.main()