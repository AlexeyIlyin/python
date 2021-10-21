import re

# raw ='93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
raw = '54.171.169.20 - - [17/May/2015:17:05:28 +0000] "GET /downloads/product_3 HTTP/1.1" 200 1074411 "-" "Chef Client/11.16.4 (ruby-1.9.3-p547; ohai-7.4.0; x86_64-linux; +http://opscode.com)"'
# raw = '194.76.107.17 - - [17/May/2015:18:05:07 +0000] "HEAD /downloads/product_2 HTTP/1.1" 200 0 "-" "Wget/1.13.4 (linux-gnu)"'

# remote_addr = re.search(r'(\d{1,3}.){3}\d{1,3}', raw)
# pars_raw = (remote_addr.group())
# print(pars_raw)


remote_addr = re.compile (r'(\d{1,3}.){3}\d{1,3}')
request_datetime = re.compile(r'[ []\d{1,2}/\w{3,8}/\d{4}(:\d{2}){3}\s[+]\d{4}[]]')
request_type = re.compile(r'"[A-Z]{3,4}')
requested_resource = re.compile(r'/[a-z]*/[a-z]*[_]\d{1}')
response_code = re.compile(r'\d{1}["]\s\d{3}')
response_size = re.compile(r'\d*\s"-"')

parsed_raw = (remote_addr.search(raw).group(),
              request_datetime.search(raw).group(),
              request_type.search(raw).group()[1:],
              requested_resource.search(raw).group(),
              response_code.search(raw).group()[-3:],
              response_size.search(raw).group().split(' ')[0]
              )
print(parsed_raw)



