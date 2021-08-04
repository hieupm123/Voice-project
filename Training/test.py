<<<<<<< HEAD
# from typing import Sequence
# import numpy as np
# import time
# from underthesea import word_tokenize
# import pickle
# import time
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.pipeline import Pipeline
# files = [];
# with open('VN.txt','r+',encoding='utf8') as f:
# 	files = f.readlines();
# sequence_id = []
# a_s = []
# ans_ = [];
# ma = {};
# def get_imformation():
# 	cnt_ = 0
# 	i = 0
# 	id = 0;
# 	while(i < len(files)):
# 		train = '';res = '';
# 		if('data_' in files[i]):
# 			files[i] = files[i].replace('data_','');
# 			files[i] = files[i].replace('\n','');
# 			id = int(files[i]);
# 			if(id in sequence_id):
# 				i += 2;
# 			else:
# 				sequence_id.append(id)
# 				ans_.append(cnt_);
# 				cnt_ += 1;
# 				i += 1;
# 				a_s.append(files[i].replace('\n','').strip());
# 				i += 1;

# get_imformation();
# print(len(ans_))
# print(len(a_s))
# # print(sequence_train)
# f = open('write.txt','a',encoding = 'utf8');
# for i in range(0,len(ans_)):
# 	f.write('_' + str(ans_[i]) + '\n');
# 	f.write(a_s[i] + '\n');

# 	f.write('_' + str(ans_[i]) + '\n');
# 	f.write(sequence_train[i] + '\n');
# 	f.write(sequence_res[i] + '\n')


files = [];
f = open('write.txt','r+',encoding = 'utf8');
files = f.readlines();
id = [];
ans = [];
func = [];
_class = [];
for i in range (0,len(files),4):
	files[i] = files[i].replace('\n','')
	id.append(int(files[i].replace('_','')));
	ans.append(files[i + 1].replace('\n',''));
	func.append(files[i + 2].replace('\n',''));
	_class.append(files[i + 3].replace('\n',''));
print(_class)
# import sqlite3
# database = sqlite3.connect('data_chuong_trinh.db')
# c = database.cursor();
# c.execute("""CREATE TABLE process(
# 	id  integer,
# 	ans  text,
# 	class  text,
# 	func  text
# 	)""")
# for i in range(0,len(ans_)):

	# c.excute()
#c.excute("""INSERT INTO process VALUES """)
# database.commit()
# database.close()
=======
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import random
import json
import pickle
import tensorflow as tf
from tensorflow.python.framework import ops

with open("intents.json",encoding="utf8") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
        if intent["tag"] not in labels:
            labels.append(intent["tag"])
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))
    labels = sorted(labels)
    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]
    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w.lower()) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
    training = numpy.array(training)
    output = numpy.array(output)
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

    ops.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        # inp = "Mua gì"
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))
        # break

chat()
>>>>>>> e678d32719d972692f9e27850fb62bd1c617d45a
