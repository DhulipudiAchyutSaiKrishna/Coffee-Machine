scores = input().split()
# put your python code here
incount=0
cocount=0
for score in scores:
    if score=='I':
        incount+=1
        if incount==3:
            print("Game over\n{}".format(cocount))
            break
        continue
    cocount+=1
if incount<3:
    print("You won\n{}".format(cocount))
