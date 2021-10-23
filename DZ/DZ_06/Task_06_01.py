from requests import get, utils


response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
# print(type(content), len(content))
# content = response.text
# print(content)


#v1 решение через список

# content = content.split('\n')[:-1]
# pars_usr = []
# for el in content[:]:
#     el = el.split(' ')
#     el = (el[0], el[5], el[6])
#     #print(el)
#     pars_usr.append(el)
# print(pars_usr)
# #print(pars_usr[0])
# #print(pars_usr[51461])
# print(len(pars_usr))

# el = (el.split(' ') for el in content[:])
# print(*el)


#v2 решение через генератор

def pars_nginx_logs(cont):
    cont = cont.split('\n')[:-1]
    for el in cont:
        el = el.split(' ')
        el = (el[0], el[5], el[6])
        yield el

print(*pars_nginx_logs(content))


