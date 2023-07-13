#!/home/vadim/workspaces/python/parsers/.venv/bin/python

import requests
from lxml import etree
import uuid
import os
from tinytag import TinyTag
import argparse

from concurrent.futures import ThreadPoolExecutor






def rename_file(path, old_name):
    tag = TinyTag.get(path)
    title = str(tag.title)

    print(f"Меняет названия на {title}")

    old_file = os.path.join(f"{PATH}/", f"{old_name}")
    new_file = os.path.join(f"{PATH}/", f"{title}.mp3")

    print(f"old {old_file} new {new_file}")

    os.rename(old_file, new_file)




def download(url):

    print(f"Пошол запрос")
    response = requests.get(url) 
   
    gen_random_name = f'{uuid.uuid1()}.mp3'
    path_to_file = f"{PATH}/{gen_random_name}"

    with open(path_to_file, 'wb') as f:
        print(f"Записан как: {path_to_file}")
        f.write(response.content)


    print(response.status_code)
    print(response.headers['content-type'])
    print(response.encoding)
    print("Фаил успешно скачен")


    rename_file(path_to_file, gen_random_name)



if __name__ == "__main__":


    


    parser = argparse.ArgumentParser(description='Программа для скачивания музыки')
    parser.add_argument("url", help="./musikaadow url")
    args = parser.parse_args()
    print(args.url)


    url = args.url
    page = requests.get(url)
    html_code = page.content.decode('utf-8')  
    tree = etree.HTML(html_code)
    receved_urls = tree.xpath("//html/body/main/div/div/div/div/ul/li/div/div/a/@href")

    PATH = "/home/vadim/Music"
   
   
   
   
   
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(download, receved_urls)


    def sh(script):
        os.system("bash -c '%s'" % script)

    sh('libnotify -t 0 "Медиа файлы скаченны!!"')
    
     
     
     
     
     
