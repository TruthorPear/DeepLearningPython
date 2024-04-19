data = []

#add numbers 1-100 to data
for i in range(101):
    data.append(i)

batches = [
    data[k:k+10] 
    for k in range(0, 50, 10)]

#so this will make a batches:
#it has 50/10 elements
#those elements are their own lists with:
#elements from 0 to 10

print(batches)