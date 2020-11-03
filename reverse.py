def varReverse(value):
    if type(value) == list or type(value) == str:
     reverse = l[::-1]
     print(reverse)
    else:
        changed = str(value)
        reverse = changed[::-1]
        print(reverse)
varReverse(1232)
