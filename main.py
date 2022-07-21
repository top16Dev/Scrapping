from operator import contains
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import  urljoin
import json

urls = []
nextUrls = []
totalUrls = []
thread_count = 1
indicator = 0

def isExistUrl(url):
    for link in totalUrls:
        if (url == link):
            return 0
    return 1

def isWikiUrl(url):
    slashCount = 0
    for count in range(len(url)) :
        if(slashCount == 3) :
            break
        if(url[count] == '/') :
            slashCount += 1
    localString = url[0 : count]
    if("wikipedia" in localString) :
        return 1
    return 0

def fetchLinks(url):
    global urls, nextUrls
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.find_all('a'):
        str = urljoin(url, link.get('href'))
        if isExistUrl(str) and isWikiUrl(str):
            nextUrls.append(str)
            totalUrls.append(str)
            print(str)

# def do_task():
#     global indicator
#     for cycle in range(thread_count)
#     while indicator < len(urls):
#         # print(indicator, urls[indicator])
#         url = urls[indicator]
#         indicator += 1
#         fetchLinks(url)
        

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-n', type=int, default=1)
parser.add_argument('url')
args = vars(parser.parse_args())

thread_count = args['n']
url = args['url']
# url = 'https://www.wikipedia.org/'

fetchLinks(url)
urls = nextUrls
nextUrls = []
for cycle in range(thread_count - 1) :
    while indicator < len(urls):
        # print(indicator, urls[indicator])
        url = urls[indicator]
        indicator += 1
        fetchLinks(url)
    urls = nextUrls
    nextUrls = []

dictionary = {
    "data": totalUrls
}
 
with open("result.json", "w") as outfile:
    json.dump(dictionary, outfile)
# threads = []
# for i in range(thread_count):
#     thread = threading.Thread(target=thread_task)
#     thread.start()
#     threads.append(thread)

# for i in range(thread_count):
#     threads[i].join()

