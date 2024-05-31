bill_amount = float(input('Enter your bill amount: '))
if bill_amount < 100:
    print('no discount')
elif 500 < bill_amount >= 100:
    discount = bill_amount * 10/100
    print(discount)
elif bill_amount >= 500:
    discount = bill_amount * 20/100
    print(discount)