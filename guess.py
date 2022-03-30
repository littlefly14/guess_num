#產生一個隨機整數1~100(不印出來)
#使用者重複去猜
#猜錯就告訴她比較大還比較小
import random
r = random.randint(1, 100) #隨機產生數字
while True:
	num = int(input('請猜數字:'))
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print("比答案小")
		

