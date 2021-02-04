phrase=input()
res=''
for letter in phrase:
    if letter.isupper():
        res+='_'+letter.lower()
    else:
        res+=letter
print(res)
