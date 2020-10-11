while True:
    print("please enter your password")
    c = input(":")
    d = "1234"
    if c == d:
        print("you are logged in")
        break
    else:
        print("you forgot your password")
        print("do you want to reset the password")
        s = input("press yes or no: ")
        if "yes":
            u = input("input only the first letter of password :")

            if u in list(d):
                print("please confirm yes/no")
                if "yes":
                    print("type new password")
                    h = input(":")
                    print("password sucessfuly changed")
                    d = h
                    continue
                else:
                    break

            else:
                break
