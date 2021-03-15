## Proj 19 python
class student:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@BKMC.TU.edu.np"
        self.salary = salary
        
    def fullData(self):
       return "The full name of the student is {} {} and email is {} and salary is {} ".format(self.first, self.last, self.email, self.salary)
        

sushil = student("sushil","Gyawali",60000)
ramakrishnan = student("ramakrishna","khan",50000)

print(sushil.fullData())
print(ramakrishnan.fullData())
