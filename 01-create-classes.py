class Employee:
  empCount = 0 # class variable

  # constructor
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1
  
  def displayCount(self):
    print(f'Total employee is {Employee.empCount}')
  def displayEmployee(self):
    print(f'Name: {self.name}\nSalary: {self.salary}')

# create instance object
emp1 = Employee('John', 20000000)
emp2 = Employee('Reonaldo', 30000000)

# accessing attributes
emp1.displayEmployee()
emp2.displayEmployee()
print(f'Total employee are {Employee.empCount}')

# add, remove, or modify attributes of classes and objects at any time
emp1.salary = 50000000 # add 'salary' attributes
emp1.name = 'Gonzales' # modify 'name' attributes
del emp2.name # delete 'name' attributes

# access attributes
print(hasattr(emp1, 'salary')) # return true if have attributes employess virce varse
print(getattr(emp1, 'salary')) # return value of attributes salary '50000000'
setattr(emp1, 'salary', 100000000) # update value attributes salary to 100000000
print(getattr(emp1, 'salary')) # return value of attributes salary '100000000'
delattr(emp1, 'salary') # delete attributes 'salary'
print(hasattr(emp1, 'salary')) # will return false
