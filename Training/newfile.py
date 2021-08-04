import os
all_txt_files = os.listdir(r'D:\Project\Training\file hieu')
os.chdir(r'D:\Project\Training\file hieu')
cnt = 0;
ans = {''}
os.chdir(r'D:\Project\Training')
fo = open('write.txt','a',encoding = 'utf8');
os.chdir(r'D:\Project\Training\file hieu')
for file in all_txt_files:
	f = open(file,'r+',encoding = 'utf8');
	a = f.readlines();
	for i in range(0,len(a)):
		if('- -' in a[i] and (a[i].replace('-','').strip() + '\n' not in ans)):
			fo.write('_' + str(cnt) + '\n');
			fo.write(a[i].replace('-','').strip() + '\n');
			ans.add(a[i].replace('-','').strip() + '\n')
			i += 1;
			cnt += 1;
			while(i < len(a) and '- -' not in a[i]):
				fo.write(a[i].replace('-','').strip() + '\n');
				i += 1;





