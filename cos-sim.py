import numpy as np
import os
import statistics

def cos_sim(a, b):
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

friend_0 = [4562,4684,587,2353,674,1100,2015,1998,891,1892,680,2207,655,1737,1720,2109,1692,977,318,1938,1715,285,1852,730,1416,1850,75,1538,196,1620,2265,518,2561,2031,122,961,3275,2446,3663,133,1125,1907,17,628,612,669,1317,1115,1400,194,1089,1153,41,869,794,1260,351,12,]

list_of_cat = ["active","beautysvc","homeservices","hotelstravel","nightlife","pets","restaurants","shopping"]

user_cat_matrix = []

for file in os.listdir("E:\\IT\\MP\\Yelp\\user_score"):
	cat_mean_list = []			#vector
	user_file = open("E:\\IT\\MP\\Yelp\\user_score\\"+file,"r")
	for cat in list_of_cat:
		norm_list = [0]
		for line in user_file:
			list=line.split()	#list[0]=cat list[1]=rid list[2]=norm
			if list[0]==cat:
				list[2] = float(list[2])
				norm_list.append(list[2])
		#print norm_list
		mean_of_a_cat = statistics.mean(norm_list)
		cat_mean_list.append(mean_of_a_cat)

user1= np.array(user_cat_matrix[0]) 
user2= np.array(user_cat_matrix[10])

print(cos_sim(user1,user2))