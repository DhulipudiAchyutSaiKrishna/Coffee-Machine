# put your python code here
sum_of_ele,sum_of_squares = 0,0
while True:
    try:
        ele = int(input())
        sum_of_ele = sum_of_ele + ele
        sum_of_squares = sum_of_squares + (ele * ele)
        if sum_of_ele == 0:
            break

    except:
        break

print(sum_of_squares)
