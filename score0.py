from nltk.tokenize import RegexpTokenizer
import os
from math import exp
tokenizer = RegexpTokenizer(r'\w+')


neg_file = open("Sentiment Dictionaries/SD/neg-words.txt","r")
pos_file = open("E:\IT\MP\Sentiment Dictionaries\SD\pos-words.txt","r")
ND_file = open("E:\IT\MP\Sentiment Dictionaries\ND.txt","r")
l1_file = open("E:\IT\MP\Sentiment Dictionaries\SDD\level-1.txt","r")
l2_file = open("E:\IT\MP\Sentiment Dictionaries\SDD\level-2.txt","r")
l3_file = open("E:\IT\MP\Sentiment Dictionaries\SDD\level-3.txt","r")
l4_file = open("E:\IT\MP\Sentiment Dictionaries\SDD\level-4.txt","r")
l5_file = open("E:\IT\MP\Sentiment Dictionaries\SDD\level-5.txt","r") 
stopword_file = open("E:\IT\MP\Sentiment Dictionaries\stopwordlist.txt","r")


if not os.path.exists("E:\\IT\\MP\\Yelp\\user_score"):
    	os.makedirs("E:\\IT\\MP\\Yelp\\user_score")

stopword = []
for line in stopword_file:
	line=line.strip()
	stopword.append(line) 

friend_0 = [0,4562,4684,587,2353,674,1100,2015,1998,891,1892,680,2207,655,1737,1720,2109,1692,977,318,1938,1715,285,1852,730,1416,1850,75,1538,196,1620,2265,518,2561,2031,122,961,3275,2446,3663,133,1125,1907,17,628,612,669,1317,1115,1400,194,1089,1153,41,869,794,1260,351,12]
friend_0 = set(friend_0)

list_of_cat = ["active","beautysvc","homeservices","hotelstravel","nightlife","pets","restaurants","shopping"]
neg = []
for line in neg_file:
	line=line.strip()
	neg.append(line) 

pos= []
for line in pos_file:
	line=line.strip()
	pos.append(line)

ND= []
for line in ND_file:
	line=line.strip()
	ND.append(line) 

l1 = []
for line in l1_file:
	line=line.strip()
	l1.append(line) 
l2 = []
for line in l2_file:
	line=line.strip()
	l2.append(line) 
l3 = []
for line in l3_file:
	line=line.strip()
	l3.append(line) 
l4 = []
for line in l4_file:
	line=line.strip()
	l4.append(line) 
l5 = []
for line in l5_file:
	line=line.strip()
	l5.append(line)  


for folder in list_of_cat:
	for friend in friend_0:
		friend = str(friend)
		if os.path.exists("E:\\IT\\MP\\Yelp\\"+folder+"\\user_item_review\\"+friend):
			for file in os.listdir("E:\\IT\\MP\\Yelp\\"+folder+"\\user_item_review\\"+friend):
				open_file = open("E:\\IT\\MP\\Yelp\\"+folder+"\\user_item_review\\"+friend+"\\"+file,"r")
				clauses = []
				score = 0
				for line in open_file:
					raw= line.lower().strip()
					as_well_as = raw.find("as well as")
					clauses = raw.split('.')
					clauses = filter(None,clauses)
					for clause in clauses:
						sum=0
			
				
						tokens = tokenizer.tokenize(clause)
				
				
						words = set(pos) |set(neg) |set(ND) |set(l1) |set(l2) |set(l3) |set(l4) |set(l5)
						words = set(words)
						words = set(stopword) - set(words)
						no_stop = [k for k in tokens if not k in words]
					
						all_l = set(l1) |set(l2) |set(l3) |set(l4) |set(l5) 
						pos = set(pos) - set(all_l)
						for i in no_stop:
							product = 0
							ind = no_stop.index(i)
						
							if ind >=0:
								if no_stop[ind] in neg:
									product = -1
								if no_stop[ind] in pos:
									product = 1
							if ind-1 >=0:
								if no_stop[ind-1] in l1:
									product = product*5
								if no_stop[ind-1] in l2:
									product = product*4
								if no_stop[ind-1] in l3:
									product = product*2
								if no_stop[ind-1] in l4:
									product = product*0.5
								if no_stop[ind-1] in l5:
									product = product*0.25
							if ind-2>=0:
								if no_stop[ind-2] in ND:
									product = product*-1
							if ind-3>=0:
								if no_stop[ind-3] in ND:
									product = product*-1
				
						
							sum = sum + product
						
						score = score + sum
				if len(clauses)==0:
					score=0
				else:	
					score =float(score)/len(clauses)
			
				norm = 10/(1 + exp(-score)) - 5
				#print len(clauses),clauses
				#print 'Norm:',norm
				
				user_file = open("E:\\IT\\MP\\Yelp\\user_score\\"+friend+".txt","a")
				user_file.write(folder+' '+file+' '+str(norm)+'\n')
		else:
			user_file = open("E:\\IT\\MP\\Yelp\\user_score\\"+friend+".txt","a+")
			user_file.write(folder+' '+"null"+' '+"0"+'\n')

			
	
