import statistics
import os
from friends import friends

list_of_var = []

if not os.path.exists("E:\\IT\\MP\\Yelp\\user_var"):
    	os.makedirs("E:\\IT\\MP\\Yelp\\user_var")

friends_temporary_list = friends()		

for user in os.listdir("E:\\IT\\MP\\Yelp\\user_score"):
		var_file = open("E:\\IT\\MP\\Yelp\\user_var\\"+user,"a")
		user = user.split('.')
		friend_user = friends_temporary_list[int(user[0])][0]
		friend_user = set(friend_user)
		friend_user = list(friend_user)
		friend_user = friend_user[1:]
		for friend in friend_user:
			friend = str(friend)
			norm_list = []
			user_file = open("E:\\IT\\MP\\Yelp\\user_score\\"+friend+".txt","r")
			for line in user_file:
				temp_list = line.split()
				norm_list.append(float(temp_list[2]))

			variance = statistics.pvariance(norm_list)
			list_of_var.append(variance)

		sum_of_var = sum(list_of_var)
		num_friends = len(friend_user)

		for i in  range(0,num_friends):
			norm_var_0 = list_of_var[i]/sum_of_var
			var_file.write(str(friend_user[i])+' '+str(norm_var_0)+'\n')

