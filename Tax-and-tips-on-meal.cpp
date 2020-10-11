#for calculating tax and tips
cost = int(input("input the cost of meal excluding tax and tips:"))
tax = (10/100)*cost
print("The 10% tax of meal is:",tax)
tips = tax*(15/100)
print("The tips including 10% is :",tips)
print(f"The actual cost is {cost} without including tax and tips.The cost of meal is {cost+tax+tips} including 10% i.e {tax} and 15% of tips i.e.{tips}")


