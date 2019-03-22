class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent Attributes : ", Parent.parentAttr)


class Parent2:
    parent2Attr = 500

    def __init__(self):
        print("Calling parent 2 constructor")

    def parent2Method(self):
        print("Calling parent2 method")

    def setAttr2(self, attr):
        Parent2.parent2Attr = attr

    def getAttr2(self):
        print(f'Parent2 Attributes: {Parent2.parent2Attr}')


class Child(Parent):
    def __init__(self):
        print("Calling child attributes")

    def childMethod(self):
        print('Calling child method')


class Child2(Parent):
    pass


class Child3(Parent, Parent2):  # subclass of Parent and Parent2
    pass


print('== C1 ==')
c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

print('\n\n\n== C2 ==')
c2 = Child2()
c2.getAttr()  # call parent's method

print('\n\n\n== C3 ==')
c3 = Child3()
print(issubclass(Child3, Parent2)) # will print True, if Parent2 parent of Child3 or Child3 is indeed a subclass of superclass Parent2
print(isinstance(c3, Child3)) # will print True, if c3 instance of Child
c3.getAttr2()
c3.getAttr()