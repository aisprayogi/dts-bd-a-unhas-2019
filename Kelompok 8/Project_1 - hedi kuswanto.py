# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:23:39 2019

@author: DEVTEK.ID
"""
import pandas as pd

df = pd.read_csv("Data_project.csv")

filter1 = df.query('status_obesitas==("obesitas","normal")')
filter2 = filter1.query('hamil==("Laki-Laki","Tidak")')
data_obes = filter2


#Contingency Table
contingency_table=pd.crosstab(data_obes["status_obesitas"],data_obes["x4"])
#print('contingency_table :-\n',contingency_table)

Observed_Values = contingency_table.values 
#print("Observed Values :-\n",Observed_Values)

import scipy.stats
b=scipy.stats.chi2_contingency(contingency_table)
Expected_Values = b[3]
#print("Expected Values :-\n",Expected_Values)

#Degree of Freedom
no_of_rows=len(contingency_table.iloc[0:2,0])
no_of_columns=len(contingency_table.iloc[0,0:2])
df=(no_of_rows-1)*(no_of_columns-1)
#print("Degree of Freedom:-",df)

from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
chi_square_statistic=chi_square[0]+chi_square[1]
#print("chi-square statistic:-",chi_square_statistic)

#critical_value
alpha = 0.05
#critical_value=chi2.ppf(q=1-alpha,df=df)
#print('critical_value:',critical_value)

#p-value
p_value=1-chi2.cdf(x=chi_square_statistic,df=df)
print('p-value:',p_value)

print('Significance level: ',alpha)
print('Degree of Freedom: ',df)
print('chi-square statistic:',chi_square_statistic)
#print('critical_value:',critical_value)
print('p-value:',p_value)

#if chi_square_statistic>=critical_value:
#    print("H0 ditolak, artinya terdapat hubungan 2 variabel")
#else:
#    print("H0 diterima, artinya tidak terdapat hubungan 2 variabel")
    
if p_value<=alpha:
    print("H0 ditolak, artinya terdapat hubungan 2 variabel")
else:
    print("H0 diterima, artinya tidak terdapat hubungan 2 variabel")
# take a look at the dataset
#df.head()