def currency_rates(rate):
    search_rate = rate.upper()
    from requests import get, utils
    from datetime import date

    date_now = date.today()

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')

    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    currency = {}
    content = content.split('<Valute ')    #Парсим на сторки валют
    for i in range(len(content)):    # парсим строки на элементы
        content[i] = content[i].replace('>','<').split('<')
        val=content[i]
        for pl in val:    # наполняем словарь
            if pl=='CharCode':
                char_code = (val[val.index(pl)+1]).upper()    # получаем валюту
            elif pl=='Value':
                val_char = float((val[val.index(pl)+1]).replace(',', '.'))    #получаем курс
                currency [char_code] = val_char

    result = (currency.get(search_rate), search_rate, date_now)
    return result

    #return print (currency.get(search_rate), date_now)

print(currency_rates('usd'))