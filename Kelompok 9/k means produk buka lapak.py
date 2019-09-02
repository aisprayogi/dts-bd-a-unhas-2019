# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 07:49:48 2019

@author: Ahmad Husain
"""

import pandas as pd
import numpy as np

#import data
d=pd.read_excel('data setelah cleaning.xlsx')

#take variabel product, price and feedback
product=d['Name of product']
price=d['Price_of_product']
feedback=d['feedback_owner']
location=d['Location_sale']

#groupby location
loc_owner = d.groupby('Location_sale').size()
loc_owner1=pd.DataFrame(loc_owner)
 
loc_owner1.to_excel('group by location.xlsx')

#convert type data string to integer 
price1=price.str.replace(r'.','')
price= price1.astype(int)
d['Price_of_product']=price

#plot price vs feedback
import matplotlib.pyplot as plt
plt.plot(feedback,price ,'ro', label='d')

max(feedback)
max(price)

# Initialize the centroids
#centroid feedback vs price
c1 = (1000,1000000)
c2 = (1000,10000000)
c3 = (19000,100000)

cent_gbg=(c1,c2,c3)
cent_gbg=pd.DataFrame(list(cent_gbg))


#plot
plt.scatter(feedback, price)   
plt.scatter(cent_gbg[0], cent_gbg[1], c='red', marker='x')


# points and the centroids

def calculate_distance(centroid, X, Y):
    distances = []
        
    # Unpack the x and y coordinates of the centroid
    c_x, c_y = centroid
        
    # Iterate over the data points and calculate the distance using the           # given formula
    for x, y in list(zip(X, Y)):
        root_diff_x = (x - c_x) ** 2
        root_diff_y = (y - c_y) ** 2
        distance = np.sqrt(root_diff_x + root_diff_y)
        distances.append(distance)
        
    return distances

#calculate distance from 4 centroid
d[0] = calculate_distance(c1, feedback, price)
d[1] = calculate_distance(c2, feedback, price)
d[2] = calculate_distance(c3, feedback, price)

d['Cluster'] = d[[0,1,2]].apply(np.argmin, axis =1)

#save first k means
d.to_excel('data k means pertama.xlsx')

# Calculate the coordinates of the new centroid from cluster 1
feedback_new_centroid1 = d[d['Cluster']=='c1_distance']['feedback_owner'].mean()
price_new_centroid1 = d[d['Cluster']=='c1_distance']['Price_of_product'].mean()

# Calculate the coordinates of the new centroid from cluster 2
feedback_new_centroid2 =  d[d['Cluster']=='c2_distance']['feedback_owner'].mean()
price_new_centroid2 =  d[d['Cluster']=='c2_distance']['Price_of_product'].mean()

# Calculate the coordinates of the new centroid from cluster 3
feedback_new_centroid3 =  d[d['Cluster']=='c3_distance']['feedback_owner'].mean()
price_new_centroid3 =  d[d['Cluster']=='c3_distance']['Price_of_product'].mean()

c1_kedua = (feedback_new_centroid1,price_new_centroid1)
c2_kedua = (feedback_new_centroid2,price_new_centroid2)
c3_kedua = (feedback_new_centroid3,price_new_centroid3)

cent_gbg1=(c1_kedua,c2_kedua,c3_kedua)
cent_gbg1=pd.DataFrame(list(cent_gbg1))


#plot
plt.scatter(feedback, price, c=d['Cluster'].astype(float))   
plt.scatter(cent_gbg1[0], cent_gbg1[1], c='red', marker='x')

#iterasi kedua
#calculate distance from 4 centroid
d[0] = calculate_distance(c1_kedua, feedback, price)
d[1] = calculate_distance(c2_kedua, feedback, price)
d[2] = calculate_distance(c3_kedua, feedback, price)

d['Cluster_kedua'] = d[[0,1,2]].apply(np.argmin, axis =1)
#save second k means
d.to_excel('data k means kedua.xlsx')

# Calculate the coordinates of the new centroid from cluster 1
feedback_new_centroid1_2 = d[d['Cluster_kedua']==0]['feedback_owner'].mean()
price_new_centroid1_2 = d[d['Cluster_kedua']==0]['Price_of_product'].mean()

# Calculate the coordinates of the new centroid from cluster 2
feedback_new_centroid2_2 = d[d['Cluster_kedua']==1]['feedback_owner'].mean()
price_new_centroid2_2 =  d[d['Cluster_kedua']==1]['Price_of_product'].mean()

# Calculate the coordinates of the new centroid from cluster 3
feedback_new_centroid3_2 =  d[d['Cluster_kedua']==2]['feedback_owner'].mean()
price_new_centroid3_2 =  d[d['Cluster_kedua']==2]['Price_of_product'].mean()

c1_ketiga = (feedback_new_centroid1_2,price_new_centroid1_2)
c2_ketiga = (feedback_new_centroid2_2,price_new_centroid2_2)
c3_ketiga = (feedback_new_centroid3_2,price_new_centroid3_2)

cent_gbg2=(c1_ketiga,c2_ketiga,c3_ketiga,c3_ketiga)
cent_gbg2=pd.DataFrame(list(cent_gbg2))

#plot
plt.scatter(feedback, price, c=d['Cluster'].astype(float))   
plt.scatter(cent_gbg2[0], cent_gbg2[1], c='red', marker='x')


#iterasi ketiga
#calculate distance from 4 centroid
d[0] = calculate_distance(c1_ketiga, feedback, price)
d[1] = calculate_distance(c2_ketiga, feedback, price)
d[2] = calculate_distance(c3_ketiga, feedback, price)

d['Cluster_ketiga'] = d[[0,1,2]].apply(np.argmin, axis =1)
#save second k means
d.to_excel('data k means ketiga.xlsx')

# Calculate the coordinates of the new centroid from cluster 2
feedback_new_centroid1_3 = d[d['Cluster_ketiga']==0]['feedback_owner'].mean()
price_new_centroid1_3 = d[d['Cluster_ketiga']==0]['Price_of_product'].mean()

# Calculate the coordinates of the new centroid from cluster 2
feedback_new_centroid2_3 = d[d['Cluster_ketiga']==1]['feedback_owner'].mean()
price_new_centroid2_3 =  d[d['Cluster_ketiga']==1]['Price_of_product'].mean()

# Calculate the coordinates of the new centroid from cluster 3
feedback_new_centroid3_3 =  d[d['Cluster_ketiga']==2]['feedback_owner'].mean()
price_new_centroid3_3 =  d[d['Cluster_ketiga']==2]['Price_of_product'].mean()

c1_ketiga = (feedback_new_centroid1_3,price_new_centroid1_3)
c2_ketiga = (feedback_new_centroid2_3,price_new_centroid2_3)
c3_ketiga = (feedback_new_centroid3_3,price_new_centroid3_3)

cent_gbg3=(c1_ketiga,c2_ketiga,c3_ketiga)
cent_gbg3=pd.DataFrame(list(cent_gbg3))

#plot
plt.scatter(feedback, price, c=d['Cluster'].astype(float))   
plt.scatter(cent_gbg3[0], cent_gbg3[1], c='red', marker='x')


from sklearn.cluster import KMeans

X=d.loc[:,["Price_of_product","feedback_owner"]]
    
# Specify the number of clusters (3) and fit the data X
kmeans = KMeans(n_clusters=3, random_state=4).fit(X)
kmeans.cluster_centers_
kmeans.labels_

#plot
plt.scatter(feedback, price, c=kmeans.labels_.astype(float))   
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 0], c='red', marker='x')

# Calculate silhouette_score
from sklearn.metrics import silhouette_score

print(silhouette_score(X, kmeans.labels_))

# Import the KElbowVisualizer method 
from yellowbrick.cluster import KElbowVisualizer

# Instantiate the KElbowVisualizer with the number of clusters and the metric 
visualizer = KElbowVisualizer(kmeans, k=(2,12), metric='silhouette', timings=False)

# Fit the data and visualize
visualizer.fit(X)    
visualizer.poof()   

