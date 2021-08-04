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
