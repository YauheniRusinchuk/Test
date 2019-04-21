#python 3.7

import requests
from bs4 import BeautifulSoup
import json
import time



def get_html(n_page):
    ''' Возврашает страницу '''
    url:str         = f'https://bukmekerskie-kontory.bet/betting/bookmakers/fonbet/addr/?page={n_page}'
    headers:dict    = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    return res.text

def write_file(data) -> None:
    ''' Запись в файл '''
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def current_data() -> None:
    ''' Производим поиск и формируем список объектов '''
    data:list = []
    for n_page in range(0,30):
        html   = get_html(n_page)
        soup   = BeautifulSoup(html, 'lxml')
        for i in soup.findAll('td', class_='left'):
            address      = i.text
            phone_nubmer = [i.find_next('td').text]
            work_hour    = i.find_next('td').find_next('td').text or "Круглосуточно",
            data.append({
                "name": "Fonbet",
                "Address": address,
                "Phone":  phone_nubmer,
                "Working hours" : work_hour,
            })

    write_file(data)






def main() -> None:
    start = time.time()
    print("start ....")
    current_data()
    print("end ....")
    print(time.time() - start)

if __name__ == '__main__':
    main()
