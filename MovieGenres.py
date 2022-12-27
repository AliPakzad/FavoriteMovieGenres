n = int(input())

dict1 = {"Horror": 0, "Romance":0, "Comedy":0, "History":0 , "Adventure":0 , "Action":0}

for i in range(n):
    string = input().split()
    dict1[string[1]] += 1
    dict1[string[2]] += 1
    dict1[string[3]] += 1

#print(dict1)

sorted_dict1 = {}
sorted_dict2 = {}

sorted_keys1 = sorted(dict1) #sort the dictionary alphabetically

for w in sorted_keys1:
    sorted_dict1[w] = dict1[w]

#sort the dictionary by value in descending order
sorted_keys2 = sorted(sorted_dict1, key=sorted_dict1.get, reverse =True)


for w in sorted_keys2:
    sorted_dict2[w] = dict1[w]

#print(sorted_dict2)

for k,v in sorted_dict2.items():
    print(f"{k} : {v}")
