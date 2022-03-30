#產生一個隨機整數1~100(不印出來)
#使用者重複去猜
#猜錯就告訴她比較大還比較小
import random
start = int(input("請決定隨機數字範圍開始值:"))
end = int(input('請決定隨機數字範圍結束值:'))

r = random.randint(start, end) #隨機產生數字
count = 0
while True:
	count = count + 1 #count += 1
	num = int(input('請猜數字:'))
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print("比答案小")
	print('這是你猜的第', count, '次')



