def friends():
	active_users = open("E:\\IT\\MP\\Yelp\\active\\users.txt","r")
	rest_users = open("E:\\IT\\MP\\Yelp\\restaurants\\users.txt","r")
	another_list = []
	friends_list = [[] for x in xrange(0,5327)]
	final_friends_list = [[] for x in xrange(0,5327)]
	for row in active_users:
		line = row.strip().split(':')
		user_index = int(line[0])
		friends_list[user_index].append(line[1])
	for row in rest_users:
		line = row.strip().split(':')
		user_index = int(line[0])
		friends_list[user_index].append(line[1])
	
	for user in xrange(0,5327):
		if user < 2000:
			for i in range(0,2):
			
				leng = len(friends_list[user][i])
				sliced = friends_list[user][i][1:leng-2]
				list = [int(s) for s in sliced.split(',') if s.isdigit()]
				if i==0:
					another_list = list
					another_list.insert(0,user)
				if i==1:
					another_list = another_list + list
		else:
				leng = len(friends_list[user][0])
				sliced = friends_list[user][0][1:leng-2]
				list = [int(s) for s in sliced.split(',') if s.isdigit()]
				another_list = list
				another_list.insert(0,user)
						
		final_friends_list[user].append(another_list)
	
	return final_friends_list

