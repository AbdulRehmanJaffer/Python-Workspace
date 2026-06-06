"""class Base:
    def __init__(self):
        self.a = "GeeksForGeeks"
        self.c = "GeeksForGeeks"

class Derived(Base):
    def __init__(self):

        Base.__init__(self)
        print("Calling private member of Base Class")
        print(self._c)

obj1 = Base()
print(obj1.a)"""

#activity 1
"""class myClass:
    __privateVar = 27

    def __privatemeth(self):
        print("I am in class Myclass")

    def hello(self):
        print("Private variable vallue", self.__privateVar)

    def callPrivate(self):
        self.__privatemeth()

foo = myClass()
foo.hello()
foo.callPrivate()"""

#activity 2
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: ", self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell

c.setMaxPrice(1000)
c.sell