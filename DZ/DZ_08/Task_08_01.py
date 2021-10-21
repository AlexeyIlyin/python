# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError
import re

def email_parse (email_addr):

    try:
        username = re.search(r'[\w-]*', email_addr)
        domain = re.search(r'@[\w-]*[.]\w{2,3}',email_addr)
        result = {'username':username.group(), 'domain':domain.group()}
        return print(result)
    except AttributeError as e:
        print(f'ValueError: wrong email: {email_addr}')


email_parse('Ilyin-av@ao-rr.com')