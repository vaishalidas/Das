import numpy as np
import os
import statistics

def cos_sim(a, b):
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

friend_0 = [0,4562,4684,587,2353,674,1100,2015,1998,891,1892,680,2207,655,1737,1720,2109,1692,977,318,1938,1715,285,1852,730,1416,1850,75,1538,196,1620,2265,518,2561,2031,122,961,3275,2446,3663,133,1125,1907,17,628,612,669,1317,1115,1400,194,1089,1153,41,869,794,1260,351,12]
friend_0 = set(friend_0)
friend_0 = list(friend_0)

list_of_cat = ["active","beautysvc","homeservices","hotelstravel","nightlife","pets","restaurants","shopping"]
user_cat_matrix = []

if not os.path.exists("E:\\IT\\MP\\Yelp\\user_cos"):
    	os.makedirs("E:\\IT\\MP\\Yelp\\user_cos")


cos_file = open("E:\\IT\\MP\\Yelp\\user_cos\\0.txt","a")
only0=[0]
for friend in friend_0:
	friend = str(friend)
	cat_mean_list = []			#vector
	user_file = open("E:\\IT\\MP\\Yelp\\user_score\\"+friend+".txt","r")
	counter=0
	norm = 0
	temp=''
	for line in user_file:
			#print line
		
			list=line.split()
			if counter==0 and temp=='':
				norm = norm + float(list[2])
				temp = list[0]
				
				counter = counter +1
			else:
				if temp==list[0]:
					norm = norm + float(list[2])
					counter = counter +1
				
				else:
					temp = list[0]
					mean_of_a_cat = norm / counter
					#print counter
					cat_mean_list.append(mean_of_a_cat)
					norm = float(list[2])
					counter = 1
	#print counter
	mean_of_a_cat = norm / counter
	cat_mean_list.append(mean_of_a_cat)
	if len(cat_mean_list)!=8:
		print friend
	user_cat_matrix.append(cat_mean_list)	


cos_list_0 = []
num_friends = len(friend_0)
print 'num_friends',num_friends-1
for i in range(1,num_friends):
	user1= np.array(user_cat_matrix[0]) 
	user2= np.array(user_cat_matrix[i])
	cos = cos_sim(user1,user2)
	#print 'cos',cos
	cos_list_0.append(cos)
print 'cos',len(cos_list_0)
sum_of_cos = sum(cos_list_0)

c=0
for i in  range(0,num_friends-1):
	norm_cos_0 = cos_list_0[i]/sum_of_cos
	#print 'Normalized Cosine: ',norm_cos_0
	cos_file.write(str(friend_0[i+1])+' '+str(norm_cos_0))
	c=c+1
print 'c',c

