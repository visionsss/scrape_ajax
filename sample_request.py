"""
简单的用request爬取https://dynamic1.scrape.cuiqingcai.com/
发现返回的html无详细信息
"""
import requests


if __name__ == '__main__':
    url = 'https://dynamic1.scrape.cuiqingcai.com/'
    url = 'https://dynamic1.scrape.cuiqingcai.com/detail/27'
    html = requests.get(url).text
    print(html)
