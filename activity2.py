class Computer:
    def __init__(self):
        self.__maxprice=100000
    
    def sell(self):
        print("Selling Price of computer is ",self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice=price

comp1=Computer()
comp1.sell()

comp1.__maxprice=110000
comp1.sell()

comp1.setmaxprice(110000)
comp1.sell()