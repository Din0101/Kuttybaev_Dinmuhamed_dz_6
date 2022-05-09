import requests
file_1 = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text = file_1.text
some_text = []
with open('log.txt', 'w+', encoding='utf-8') as fw:
    print(text, file=fw)
    fw.seek(0)
    # for line in fw:
    #     some_text.append(fw.readline().splitlines())
    for line in fw:
        some_text.extend(line.splitlines())
#print(some_text)



#print(text)
#text = ['2600:3c01::f03c:91ff:fe70:9ee0 - - [25/May/2015:16:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 206 13864207 "http://www.elasticsearch.org/overview/elkdownloads/" "Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"']


def parse_log_line(log_line: str):
    if len(log_line) < 1:
        return '0'
    else:
        ip_address, log_line = log_line.split(' - - ')
        date, log_line = log_line.split('] ')

    # Удаление символа [ из строки даты
        date = date.lstrip('[')
        try:
            request, other_info = log_line.rsplit(' "-" ')
        except Exception:
            try:
                request, other_info = log_line.rsplit(' 200 ')
            except Exception:
                request, other_info = log_line.rsplit(' 206 ')

       # Удаление символа " из строки прочей информации
        other_info = other_info.strip('"')

    # Удаление символа " из строки запроса
        request = request.replace('"', '').split(' ')

        return ip_address, date, *request, other_info


print(parse_log_line(some_text[0]))





