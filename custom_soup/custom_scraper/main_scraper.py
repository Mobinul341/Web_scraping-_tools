from bs4 import BeautifulSoup as bfs
import os
from useful import *
import requests


def main_scrp(url, directory):
    create_dirs(directory)
    sites = requests.get(url)
    sites_text = sites.text
    soup = bfs(sites_text,"html.parser")
    #print(soup)
    products = soup.find_all("div",{"class":"product"})
    for product in products:
        #print(div)
        img_tag = product.find("a").find("img").get("src")
        a_tag = product.find("a").get("href")
        p_tag = product.find("p").text
        price_tag = product.find("p",{"class":"price"}).text

        print("Price" + price_tag.strip())


def page_scrp(url):
    sites = requests.get(url)
    soup = bfs(sites.text, "html.parser")
    pages = soup.find('ul',{'class':'a-pagination'})

    if not pages.find('li', {'class':'a-disabled a-last'}):
        locate = 'site url here' + str(pages.find('li',{'class':'a-last'}).find('a')['href'])
        return locate
    else:
        return
    


main_scrp("https://www.thegreatcookie.com/collections/great-cookie-of-the-month-club", "CookieClub")

