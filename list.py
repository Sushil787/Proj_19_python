ls = []
s = [] #empty list for even element that is use to store even value in future
g = [] # empty list for odd element that is use to store odd value in future
n = int(input("enter the no of element you want to add in list:"))
for i in range(n):
    c = input(f"input {i} element in list: ")
    ls.append(c)
print("It may contain repetative element",ls)
x = set(ls)
print("The list doesnot conatain repetative element",list(x))
#from here selecting even no from list
for i in range(len(ls)):
    #making new list
    if int(ls[i]) % 2 ==0:
        s.append(ls[i])
    else:
        g.append(ls[i])
print("The even element of list is : ", list(set(s)))
print("The odd element of list is : ", g)
