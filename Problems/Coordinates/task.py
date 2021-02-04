'''x=eval(input())
y=eval(input())
if (x > 0 and y > 0):
    print('I')
elif (x < 0 and y > 0):
    print('II')
elif(x < 0 and y < 0):
    print('III')
else:
    print('IV')'''
x = float(input())
y = float(input())
print("I" if x > 0 and y > 0
      else "II" if x < 0 < y
      else "IV" if y < 0 < x
      else "III")
