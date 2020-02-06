class Car:

    def __init__(self):

        self.name = "x1"
        self.__make = "bmw"
        self._price = 20000000

    def print_vars(self):
        print('+name',self.name)
        print('+make',self.__make)
        print('+price',self._price)



def main():
    car = Car()
    # print('+name',car.name)
    # print('+make',car.__make)
    # print('+price',car._price)
    car.print_vars()




if __name__ == '__main__':
    main()
    