import numpy as np
import os
import statistics
from friends import friends

def cos_sim(a, b):
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

list_of_cat = ["active","restaurants"]
user_cat_matrix = []

if not os.path.exists("E:\\IT\\MP\\Yelp\\user_cos"):
    	os.makedirs("E:\\IT\\MP\\Yelp\\user_cos")

friends_list = friends()		

for user in os.listdir("E:\\IT\\MP\\Yelp\\user_score"):
		cos_file = open("E:\\IT\\MP\\Yelp\\user_cos\\"+user+".txt","a")

		friend_user = friends_list[int(user)][0]
		friend_user = set(friend_user)
		friend_user = list(friend_user)
		for friend in friend_user:
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
			if len(cat_mean_list)!=2:
				print 'friend',friend
			user_cat_matrix.append(cat_mean_list)	


		cos_list_user = []
		num_friends = len(friend_user)
		print 'num_friends',num_friends-1
		for i in range(1,num_friends):
			user1= np.array(user_cat_matrix[0]) 
			user2= np.array(user_cat_matrix[i])
			cos = cos_sim(user1,user2)
			#print 'cos',cos
			cos_list_user.append(cos)
		print 'cos',len(cos_list_user)
		sum_of_cos = sum(cos_list_user)

		c=0
		for i in  range(0,num_friends-1):
			norm_cos_0 = cos_list_user[i]/sum_of_cos
			#print 'Normalized Cosine: ',norm_cos_0
			print friend_user[i+1]
			cos_file.write(str(friend_user[i+1])+' '+str(norm_cos_0)+'\n')
			c=c+1
		print 'c',c

