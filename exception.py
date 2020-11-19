lists = []
for i in range(1,10):
    try:
      inputs = int(input("input : "))
      lists.append(inputs)
    except ValueError:
        pass
print(lists)
