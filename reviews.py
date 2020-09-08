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
print("There are", len(data), "reviews in total.")
#avr = length/count (wrong)
#prit(avr) (wrong)
length = 0
for d in data:
	length = length + len(d)
print("The average length of each review is", length/len(data),".")

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("There are", len(new), "reviews longer than 100 characters.")

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print("There are", len(good), "reviews mentioned good.")

#Advanced version
Good = [d for d in data if ‘good’ in d]
print("There are", len(good), "reviews mentioned good.")

Good = [1 for d in data if ‘good’ in d]  #will print a lot of 1
Bad = [‘bad’ in d for d in data]  #will print a lot of false an true
#Output = [(number-1) for number in reference if number % 2 == 0]

