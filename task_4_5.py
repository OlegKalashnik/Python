from requests import get, utils


def currency_rates(argv):
    program, carr = argv
    RATES_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = get(RATES_URL)
    encodings = utils.get_encoding_from_headers(response.headers)
    answer = response.content.decode(encoding=encodings)
    carr_wrap_1 = '<CharCode>'
    carr_wrap_2 = '</CharCode>'
    date_wrap_1 = 'Date="'
    date_wrap_2 = '" name="'
    nominal_wrap_1 = '<Nominal>'
    nominal_wrap_2 = '</Nominal>'
    val_wrap_1 = '<Value>'
    val_wrap_2 = '</Value>'

    if answer.find(carr_wrap_1 + carr.upper() + carr_wrap_2) < 0:
        return None
    date = answer[answer.find(date_wrap_1) + len(date_wrap_1): answer.find(date_wrap_2)]
    nominal = answer[answer.find(nominal_wrap_1) + len(nominal_wrap_1): answer.find(nominal_wrap_2)]
    val = answer[answer.find(val_wrap_1) + len(val_wrap_1): answer.find(val_wrap_2)].replace(',', '.')
    print(f'Курс {carr.upper()} на {date} = {nominal} к {val}')


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))
