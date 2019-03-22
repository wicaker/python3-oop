# Destroying Objects (Garbage Collection)
# now times, we are import class from another file
import point

pt1 = point.Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts,all the variable have the same memory
del pt1
del pt2
del pt3     
