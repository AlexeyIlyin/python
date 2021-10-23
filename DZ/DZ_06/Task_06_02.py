from requests import get, utils

def most_frequent(my_list):
    rez = max(set(my_list), key=my_list.count)
    rez_count = my_list.count(rez)
    return rez, rez_count

response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


#v1 решение через список

content = content.split('\n')[:-1]
pars_usr = []
spamer = []
for el in content[:]:
    el = el.split(' ')
    el = (el[0], el[5], el[6])
    #print(el)
    pars_usr.append(el)
    spamer.append(el[0])
most_spam = most_frequent(spamer)
print ('Спамер: ', most_spam[0], ', количество запросов:', most_spam[1])


#v2 решение через генератор
# def pars_nginx_logs(cont):
#     cont = cont.split('\n')[:-1]
#     for el in cont:
#         el = el.split(' ')
#         el = (el[0], el[5], el[6])
#         yield el
#
# print(*pars_nginx_logs(content))