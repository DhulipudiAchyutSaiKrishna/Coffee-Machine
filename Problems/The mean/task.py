numb,count = 0,0
while True:
    num = input()
    if num == ".":
        break
    numb += int(num)
    count += 1
print(numb / count)
