#!usr/bin/eny python
#_*_ coding: utf-8 _*_
import sys
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count <retry_limit:
	username = input('请输入您的用户名：')
	lock_check = open(lock_file,'r')

	for line in lock_check.readlines():
		line = line.split()#说这里是一个全匹配?
		if username == line[0]:
			sys.exit()


	lock_check.close()
	password = input('请输入您的密码：')
	f = open(account_file,'r')
	match_flag = False
	for line in f.readlines():

		user,passwd = line.strip('\n').split()#去掉换行符，并且以空格来区分每一列
		if username == user and password == passwd:
			print('Match',username)
			match_flag = True
			break
	f.close()
	if match_flag ==False:
		print('User unmatched!')
		retry_count +=1
	else:
		print('Welcom!')
else:
	print('Your account is locked!')
	f  =open(lock_file,'a')
	f.write(username)
	f.close()
