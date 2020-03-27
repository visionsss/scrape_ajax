"""
开发者工具->Netword->XHR
Headers里面的 Request URL就是AJAX请求
"""
import requests
import logging
import json
from os import makedirs
from os.path import exists
import multiprocessing


def scrape_api(url):
    """url：AJAX请求"""
    logging.info(f'scraping {url}')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error(f'scraping {url} status code error')
    except requests.RequestException:
        logging.error(f'scraping {url} error')


def scrape_index(page):
    LIMIT = 10
    OFFSET = LIMIT*(page-1)
    url = f'https://dynamic1.scrape.cuiqingcai.com/api/movie/?limit={LIMIT}&offset={OFFSET}'
    return scrape_api(url)


def scrape_detail(num):
    url = f'https://dynamic1.scrape.cuiqingcai.com/api/movie/{num}/'
    return scrape_api(url)


def save_data(data):
    name = data.get('name')
    data_path = f'./results/{name}.json'
    if not exists('./results'):
        makedirs('./results')
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main(page):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s-%(levelname)s:%(message)s')
    index_data = scrape_index(page)
    for item in index_data.get('results'):
        num = item.get('id')
        detail_data = scrape_detail(num)
        save_data(detail_data)
        logging.info(f'detail data{detail_data}')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, 11)
    pool.map(main, pages)
    pool.close()
    pool.join()