import statistics
import os

friend_0 = [4562,4684,587,2353,674,1100,2015,1998,891,1892,680,2207,655,1737,1720,2109,1692,977,318,1938,1715,285,1852,730,1416,1850,75,1538,196,1620,2265,518,2561,2031,122,961,3275,2446,3663,133,1125,1907,17,628,612,669,1317,1115,1400,194,1089,1153,41,869,794,1260,351,12]
friend_0 = set(friend_0)
friend_0 = list(friend_0)
list_of_var = []

if not os.path.exists("E:\\IT\\MP\\Yelp\\user_var"):
    	os.makedirs("E:\\IT\\MP\\Yelp\\user_var")

var_file = open("E:\\IT\\MP\\Yelp\\user_var\\0.txt","a")


for friend in friend_0:
	friend = str(friend)
	norm_list = []
	user_file = open("E:\\IT\\MP\\Yelp\\user_score\\"+friend+".txt","r")
	for line in user_file:
		list = line.split()
		norm_list.append(float(list[2]))

	variance = statistics.pvariance(norm_list)
	list_of_var.append(variance)

sum_of_var = sum(list_of_var)

num_friends = len(friend_0)

for i in  range(0,num_friends):
	norm_var_0 = list_of_var[i]/sum_of_var
	print 'Normalized Variance for user 0 with friend',i+1,':',norm_var_0
	var_file.write(str(friend_0[i])+' '+str(norm_var_0)+'\n')