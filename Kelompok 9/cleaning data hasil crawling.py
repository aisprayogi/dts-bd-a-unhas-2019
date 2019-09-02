# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:54:55 2019

@author: Ahmad Husain
"""

import numpy as np
import pandas as pd

#import data
file=pd.read_excel('data crawl handphone 200 hal.xlsx')

#cleaning word "feedback " and persen , only take a number of feedback
file1=file['feedback_owner']
#replace "feedback" to space
file1=file1.str.replace("feedback"," ")
#replace "%"to space
file1=file1.str.replace("%"," ")
#replace "(" to space
file1=file1.str.replace("("," ")
#replace ")" to space
file1=file1.str.replace(")"," ")

#split  number of percent and number of feedback
file1=file1.str.split(expand=True,)

#delelte old column feedback owner
del file['feedback_owner']

#adding new column feedback owner
file['feedback_owner'] = file1[1]

#save to exccel
file.to_excel('data setelah cleaning.xlsx')


 
    