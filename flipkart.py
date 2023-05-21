import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name=[]
prices=[]
description=[]
reviews=[]
data={'Name':[],'Price':[],'Description':description}
for i in range(1,10):
    url="https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page="+str(i)

    r=requests.get(url)

    soup=BeautifulSoup(r.content,'html.parser')

    # print(url)
    names=soup.find_all("div",class_="_4rR01T")
    # print(names)
    #FOR NAMES
    for name in names:
        print(name.string)
        data["Name"].append(name.string)
    # print(product_name)

    #FOR PRICES
    prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")
    for price in prices:
        print(price.getText())
        data["Price"].append(price.getText())

    #FOR DESCRIPTION
    description=soup.find_all("ul",class_="_1xgFaf")
    for i in description:
        print(i.text)
        data["Description"].append(i.text)

        # print(descript.getText())

#DATAFRAME
df=pd.DataFrame.from_dict(data)
df.to_excel("data1.xlsx",index=False)
    # print(soup)
    # # while True:
    # np=soup.find("a", class_="_1LKTO3").get("href")
    # cnp="https://www.flipkart.com"+np

    
        # FOR PAGES NOT HAVE SIMILAR LINKS
        # url=cnp
        # r= requests.get(url)
        # soup=BeautifulSoup(r.content,'html.parser')
