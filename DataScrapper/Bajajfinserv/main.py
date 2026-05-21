import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
# requests → Downloading HTML pages
# BeautifulSoup → Parsing HTML
# re → Handling regex for rating extraction
# pandas → Storing scraped data in CSV

list_of_data=[]
for i in range(1,5):
        resp =requests.get("https://books.toscrape.com/catalogue/page-"+str(i)+".html")
        page_source = resp.content
        print(page_source)
        # serverside application
        # client side application

        jsoup = BeautifulSoup(page_source)
        articles = jsoup.findAll('article')
        for article in articles:
            # print(article)
            title = article.find('h3')
            title = title.text if title else title
            print("title: ", title)
            price=article.find('p', attrs={'class' : 'price_color'})
            price = price.text if price else price
            print('Price: ', price)

            stock = article.find('p', attrs={'class': 'instock availability'})
            stock = stock.text.strip() if stock else stock
            print('Stock: ', stock.strip())

            rating = article.find('p', attrs={'class': re.compile(r'star-rating.+')})
            rating = rating.get('class')[-1] if rating else None
            print(rating)
            print('Stock ', stock.strip())

            #i need to create a dataframe now but want to store data as list of dictionaries

            data = {'Title':title, 'Price': price, 'Stock': stock, 'Rating':rating}

            list_of_data.append(data)

            df = pd.DataFrame(list_of_data)
            df.to_csv('Books.csv', index=False)

            break

print(list_of_data)

