import numpy as np
np.random.seed(1234)

train_num = 0

fw_train = open('labeled_pima.tfidf', 'a+')
fw_train.truncate()
fw_test = open('unlabeled_pima.tfidf', 'a+')
fw_test.truncate()

fread = open('data/pima.csv', 'rb')
for line in fread.readlines():
	tmp = line.strip().split(',')
	label = tmp[-1]
	if label == '0':
		label = '-1'
	content = label
	for i in range(len(tmp)-1):
		content += ' '+ str(i+1) +':' + tmp[i]
	# print content
	if np.random.rand() < 0.8:
		fw_train.write(content+'\n')
		train_num += 1
	else:
		fw_test.write(content+'\n')


fread.close()
fw_train.close()
fw_test.close()


# fw_train_weight = open('data/train_weight.txt', 'a+')
# fw_train_weight.truncate()
# for i in range(train_num):
# 	fw_train_weight.write(str(0.5)+'\n')
# fw_train_weight.close()