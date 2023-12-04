for x in range(1, 2):
    print (x)

arr = [1,2,3]

if any(x in arr for x in range(1,10) ):
    print("yes")
    
data = [x*2 for x in range(5)]
print (data)


data = [x in arr for x in range(1,10)]
print ("[x in arr for x in range(1,10)]: ", data)
print (1 in [1,2,3])

test_list = [2, 5, 6, 2, 3, 2]
temp = min(test_list)
res = [i for i, j in enumerate(test_list) if j == temp]
print("The Positions of minimum element : " + str(res))

for i,j in enumerate(test_list):
    print ("i: ", i, " j:",j)


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#### ITERAZCJE #####
i, j = (1, 2)
print(i, j)


for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print('k =', k, ', v =', v)