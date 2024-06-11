tuple1 = (0,"ojo",2.5,[])
tuple1[3].extend([1,2,"kent"])
print(tuple1)
tuple1 = tuple1 + (1,6)
names += tuple1
tuple1(names)
names = tuple(names)
print(names.index("afeez"))
print(names)

x = {1,1,2,3,2,2,4,5,1,"esther"}
y = {1,3,7,9,10,2}
x.add(10)
#print(x.difference(y))
help(x.difference)

    def _init_ (self):
        self.stack = []

    def add_to_stack(self,item):


