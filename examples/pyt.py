import re

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
    
    
lista = []
lista.extend([1,2,3])
lista.extend(range(1,5))
print(lista)

lista=[x for x in range(1,5)]
print(lista)

ss = [1,1,1,2,3]
print (set(ss))

lista = {1}
lista.update([1,2,34])
print(lista)

# x = 2276375722
# y = 160148132
# list = {x for x in range (x,x+y)}

# x1 = 3424292843
# y1 = 82110297
# list2 = {x for x in range (x1,x1+y1)}

# list.update(list2)
# print (len(list))


lista = [1,2,3]
print(lista)
print(lista[1:])


def test():
    return 1,2

i,j = test()
print (i)
print(j)


test = [[x*y for x in range(10)] for y in range (4)]
print (test)



x = [[] for x in range(5)] 
x[1].append("test")
print (x)


x = [[],[1,2],[3]]
print(x)
z=[]
for sublist  in x:
    for item  in sublist:
        z.append(item)
print(z)

print([item for sublist in x for item in sublist])

alphabet = "zbafmxpv"
a = ['af', 'zx', 'am', 'ab', 'zvpmf']
l= sorted(a, key=lambda word: [alphabet.index(c) for c in word])
print(l)


alphabet = "zbafmxpv"
a = ['af', 'ax', 'am', 'ab', 'zvpmf']
order = dict(zip(alphabet, range(len(alphabet))))
#order = { ch : i for i, ch in enumerate(alphabet) }
d = sorted(a, key=lambda word: [order[c] for c in word])

print (d)

strength_of_cards  = {"A":0, "K":1, "Q":2, "J":3, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12}
order = dict(zip(strength_of_cards, range(len(strength_of_cards))))
lista = [['555JT', 684, 'T55J5'], ['QQQAJ', 483, 'QQQJA']]
print (order)
d = sorted(lista, key=lambda word: [strength_of_cards[c] for c in word[0]])
print (d)



list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

sxx = zip(list1,list2)
print ( list(sxx))


dd = [1,2,3,4,5,6]

if any (d==2 for d in dd):
        print("yes")
        
        
moj_set = {1,2,3,4,5}
moj_set.add(1)
print (moj_set)
moj_set.pop()
print (moj_set)
moj_set.add(1)
print (moj_set)



linia = ["B","X","S"]
if "S" in linia:
    print(linia.index("S"))
    
    
    
 # Przykładowa dwuwymiarowa tablica
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Odwrócenie kolejności wierszy
reversed_matrix = list(reversed(matrix))

# Wyświetlenie odwróconej tablicy
for row in reversed_matrix:
    print(row)
    
    
# Przykładowa dwuwymiarowa tablica
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Odwrócenie kolejności wierszy
reversed_matrix = matrix[::-1]

# Wyświetlenie odwróconej tablicy
for row in reversed_matrix:
    print(row)


print("0")


# Przykładowa dwuwymiarowa tablica
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Odwrócenie kolejności elementów w każdym wierszu
reversed_matrix = [list(reversed(row)) for row in matrix]

# Wyświetlenie odwróconej tablicy
for row in reversed_matrix:
    print(row)


print()

# Przykładowa dwuwymiarowa tablica
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpozycja macierzy
rotated_matrix = [list(row) for row in zip(*matrix)]

print (list(zip(*matrix)))

# Wyświetlenie obroconej tablicy
for row in rotated_matrix:
    print(row)
    
    
zakres = (5,1)    
print (sorted(zakres))



row_indexes = [1,3,6]
x1 = 7
x2 = 1

common = set([x for x in range(min(x1,x2), max(x1,x2))]).intersection(row_indexes)

print( common)






def get_patten(nums,match_start = False, match_end = False, ):
    pattern= "[\?*#{0,x}\?*]{x}[^#]*"
    res = "" if not match_start else "^[^#]*"
    for i in nums:
        res +=pattern.replace("x",str(i))
    if match_end:
        res+="\?*$"
    return (res)


print()
nums = [1,1,1,4,2]
txt = "??#????#?"
print("txt: ", txt)
print("search: ", nums)

pattern = get_patten(nums,False, True)
print(pattern)
res = re.findall(pattern, txt)

print ("xx " , res)



x1=0
offset = 0
for i in nums:
    pattern = get_patten([i],False, False)
    print("search: ", i)
    print("pattern:", pattern )
    res = re.findall(pattern, txt[x1:])
    print("res: " ,res)
    print("off:", offset)
    print()
    #x1=res.regs[0][1]
    #offset+=x1
    print(x1)



text = "...##...???"

i = len([x for x in text if x in ["#","?"] ])
print (i)

teble = [1,2,3,4]

print(sum(teble[7:]))


tablica = [
    "#....#...",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "c..##..###",
    "#....#..#",
]

def czy_odbicie_lustrzane_gora_dol(tablica):
    polowa_dlugosci = len(tablica) // 2
    gora = tablica[:polowa_dlugosci]
    dol = tablica[polowa_dlugosci:][2]  # Odbicie lustrzane dolnej części

    return gora == dol

if czy_odbicie_lustrzane_gora_dol(tablica):
    print("Górna część tablicy jest odbiciem dolnej.")
else:
    print("Górna część tablicy nie jest odbiciem dolnej.")
    
#for i in len(teble):
    index = [i for i in range(len(tablica)-1) if tablica[i+1].count(tablica[i])>0 ]
    
    ind = index[0]
    
    tablica1=tablica[:ind+1][::-1]
    tablica2=tablica[ind+1:]
    
    count=0
    min_dlugosc = min(len(tablica1), len(tablica2))
    for i in range(min_dlugosc):
        if tablica1[i] != tablica2[i]:
            break
        count+=1
    print (count)
    
    
    liczba_identycznych_wierszy = next((i for i, (w1, w2) in enumerate(zip(tablica1, tablica2)) if w1 != w2), None)
    print (count)
    
    print ()
    print ()
    
    #liczba_identycznych_wierszy = sum(a == b for a, b in zip(tablica1, tablica2))

    #count = len([i for i in range(min(len(tab1),len(tab2))) if tab1[i] == tab2[i] ])
    #print (liczba_identycznych_wierszy)
    # for i in range(len(tablica)-index[0]):
    #     print (i)
    #     if (tablica[index[0]-i]==tablica[index[0]+1+i]):
    #         count+=1
    # count = [i for i in range(index+1, len(tablica)) if index ]
    # print("count: ", count)
    # print(index)



xxx = [1,2,3]
print(xxx[0:1])

xxx = {(1,2), (2,3)}
print (xxx)