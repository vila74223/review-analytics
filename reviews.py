data = []
count = 0
#length = 0 (wrong)
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		#length += len(data[count]) (wrong)
		if count % 1000 == 0:
			print(len(data))
#avr = length/count (wrong)
#prit(avr) (wrong)
length = 0
for d in data:
	length = length + len(d)
	print(length/len(data))
