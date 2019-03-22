class Hiding:
  __count = 0

  def count(self):
    self.__count+=1
    print(self.__count)

counter = Hiding()
counter.count()
counter.count()
print(counter._Hiding__count) # will print 2
print(counter.__count) # will error, should call trough methods