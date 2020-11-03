import random
def generatePassword(Length = 8):
    l = ['@','#','$','%','&']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(1)
    digits = random.randint(10000,999999)
    password = upper+lower+special+str(digits)
    l = random.sample(password,Length)
    password = ("").join(l)
    return password

result = generatePassword(5)
print(result)
