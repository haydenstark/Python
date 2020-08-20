

class Secure:
    def setProtected(self, protected):
        self._protectedVar = protected

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private


x = Secure()
x.setProtected(21)
x.setPrivate(7)


print(x._protectedVar)
x.getPrivate()
