list_of_floats=[]

while True:
    num=input()
    if num=='.':
        break
    list_of_floats.append(float(num))

print(min(list_of_floats))
