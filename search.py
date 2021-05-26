# 字典查找、文字計數

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了！總共有', len(data), '筆資料')

wc = {} # word count
for d in data: # d是字串, data是清單
	words = d.split(' ') # d用空白鍵切割才可拿到每個單字
	for word in words:
		if word in wc: # 如果此自在字典裡有出現
			wc[word] += 1 # 在wc中查找word(word是key)每次+1
		else:
			wc[word] = 1 # 在wc中新增key(word)，次數為1
for word in wc:
	if wc[word] > 1000000: # 超過1000000次的才印
		print(word, wc[word]) # 印出key(word)也印出查找出來的次數

print(wc['Allen']) # 查找字典裡有沒有Elly

while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有在字典裡ㄛ！')
print('感謝使用本查詢功能')
