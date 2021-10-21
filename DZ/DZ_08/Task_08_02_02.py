import re
from requests import get, utils

def pars_nginx_logs(raw):

    remote_addr = re.compile (r'(\d{1,3}.){3}\d{1,3}')
    request_datetime = re.compile(r'[ []\d{1,2}/\w{3,8}/\d{4}(:\d{2}){3}\s[+]\d{4}[]]')
    request_type = re.compile(r'"[A-Z]{3,4}')
    requested_resource = re.compile(r'/[a-z]*/[a-z]*[_]\d{1}')
    response_code = re.compile(r'\d{1}["]\s\d{3}')
    #response_size = re.compile(r'\d*\s"-"')
    response_size = re.compile(r'\d{1}["]\s\d{3}\s\d*')

    parsed_raw = (remote_addr.search(raw).group(),
                  request_datetime.search(raw).group(),
                  request_type.search(raw).group()[1:],
                  requested_resource.search(raw).group(),
                  response_code.search(raw).group()[-3:],
                  response_size.search(raw).group().split(' ')[-1]
                  )
    return parsed_raw

response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
content = content.split('\n')[:-1]

for cont in content:

    print(pars_nginx_logs(cont))
