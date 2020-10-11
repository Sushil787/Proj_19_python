
ls = []
n = int(input("enter the no of element you want to add in list:"))
for i in range(n):
    c = input(f"input {i} element in list: ")
    ls.append(c)
print("It may contain repetative element",ls)
x = set(ls)
print("The list doesnot conatain repetative element",list(x))
