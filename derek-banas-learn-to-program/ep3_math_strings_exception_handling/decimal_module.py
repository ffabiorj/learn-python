from decimal import Decimal as D
sum = D(0)
sum += D('0.1')
sum += D('0.1')
sum += D('0.1')
sum -= D('0.3')

print("Sum =", sum)
