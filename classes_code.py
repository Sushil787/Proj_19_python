class Public:

    def PrintDetail(self):
        return print("Name is {} . Salary is {} and role is {}".format(self.fname,self.role,self.salary))

sushil = Public()
surendra = Public()
sushil.fname = "Sushil Gyawali"
sushil.role = "student"
sushil.salary = "$120K"

surendra.fname = "Surendra Gyawalai"
surendra.role = "Business-man"
surendra.salary = "$1000K"

sushil.PrintDetail()
surendra.PrintDetail()
