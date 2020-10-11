
import math
p = int(input("input the money the warren want to invest: "))
t = int(input("input the time: "))
r = 7.5
n = 1
i = p*(1+r/n)**(t*n)
if t == 1:
    print("The compound interest is: ", i)
elif t == 2:
    print("the compound interest is ", i)
elif t == 5:
    print("the compound interest is ", i)
elif t == 10:
    print("the interest is ",i)
