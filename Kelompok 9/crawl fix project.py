# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:54:51 2019

@author: Ahmad Husain
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 07:46:55 2019

@author: Ahmad Husain
"""
from bs4 import BeautifulSoup
from requests import get
#

name_of_product=[]
price_of_product=[]
location_sale=[]
feedback_owner=[]

for i in range(1,10):
    url1='https://www.bukalapak.com/diskon/handphone?from=category_home&page='+str(i)+'&sizes%5Bgeneral%5D='
    response1=get(url1)
    soup1=BeautifulSoup(response1.text, 'html.parser')
    hp_containers=soup1.find_all('li',class_='col-12--2')
    
    
    for x in hp_containers:
        name=x.h3.find('a',class_='product__name line-clamp--2 js-tracker-product-link qa-list').text
        price=x.div.find('span',class_='amount positive').text
        location=x.div.find('span',class_='user-city__txt').text
        feedback=x.div.find('a',class_='user-feedback-summary').text
        name_of_product.append(name)
        price_of_product.append(price)
        location_sale.append(location)
        feedback_owner.append(feedback)


data={'Name of product':name_of_product,'Price_of_product':price_of_product,'Location_sale':location_sale,'feedback_owner':feedback_owner}
import pandas as pd
df=pd.DataFrame(data)
#df.to_excel('data crawl handphone 500 hal.xlsx')


