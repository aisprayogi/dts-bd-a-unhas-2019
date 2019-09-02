# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:06:12 2019

@author: Ahmad Husain
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d=pd.read_excel('group by location.xlsx')

d1=d.drop(d[d.total<10].index)
len(d1)

x_axis=d1['Location_sale']
y_axis=d1['total']

index = np.arange(len(x_axis))

plt.barh(x_axis,y_axis)
plt.ylabel('City', fontsize=15)
plt.xlabel('Quantity owner in city', fontsize=20)
plt.yticks(fontsize=8, rotation=30)
plt.title('Persebaran tokoh Handphone dan axesoris crawl Minggu')
plt.show()
