from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os
import numpy
import re

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
stopword = []
for line in stopword_file:
	line=line.strip()
	stopword.append(line) 

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

user_list = []

for file in os.listdir("E:\\IT\\MP\\Yelp\\restaurants\\user_item_review\\0"):
	file = open("E:\\IT\\MP\\Yelp\\restaurants\\user_item_review\\0\\"+file,"r")
	for line in file:
		
		raw= line.lower()
		
		tokens = tokenizer.tokenize(raw)
		no_stop = [i for i in tokens if not i in stopword]
		no_neg = [i for i in no_stop if not i in neg]
		no_pos = [i for i in no_neg if not i in pos]
		no_ND = [i for i in no_pos if not i in ND]
		no_l1 = [i for i in no_ND if not i in l1]
		no_l2 = [i for i in no_l1 if not i in l2]
		no_l3 = [i for i in no_l2 if not i in l3]
		no_l4 = [i for i in no_l3 if not i in l4]
		no_l5 = [i for i in no_l4 if not i in l5]
		
		user_list.append(no_l5)
dictionary = corpora.Dictionary(user_list)
    
	# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in user_list]

	# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=10, id2word = dictionary, passes=80)
print(ldamodel.print_topics(num_topics=10,num_words=4))


user_topic = open('E:\\IT\\MP\\Yelp\\restaurants\\user_topics\\0.txt','w')
for v in ldamodel.show_topics(num_topics=10,num_words=4,formatted=True):
	for word in re.compile('[a-zA-Z]+').findall(str(v[1])):
		user_topic.write(word+' ')
	#user_topic.write('\n')
	