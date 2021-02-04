'''income=int(input())
if income<=15527:
    print('The tax for {} is 0%. That is 0 dollars! '.format(income))
elif (income>15527 and income<=42707):
    print('The tax for {} is 15%. That is {} dollars! '.format(income,round(income*0.15)))
elif(income>42707 and income<=132406):
    print('The tax for {} is 25%. That is {} dollars! '.format(income, round(income * 0.25)))
else:
    print('The tax for {} is 28%. That is {} dollars! '.format(income, round(income * 0.28)))
'''
value = int(input())
tax = 0
if value <= 15527:
    tax = 0
elif 15528 <= value <= 42707:
    tax = 15
elif 42708 <= value <= 132406:
    tax = 25
elif value >= 132407:
    tax = 28

print('The tax for {income} is {percent}%. That is {calculated_tax} dollars!'.format(income=value, percent=tax, calculated_tax=round(value * tax / 100)))
