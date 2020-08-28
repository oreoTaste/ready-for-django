class Car:
    def __init__(self, **kwargs):
        self.wheel = 4
        self.door = 4
        self.window = 4
        self.seat = 4
        self.color = kwargs.get("color", "nocolor")
        self.name = kwargs.get("name", "noname")

    def printName(self):
        print(self.name)

    def __str__(self):
        try:
            return (
                f"{self.color} {self.name} car with {self.wheel} wheels, {self.door} door, {self.window} window, {self.seat} seat"
                # + super().__str__()
            )
        except AttributeError:
            return f"car with {self.wheel} wheels + " + super.__str__(self)


class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs.get("type")

    def printName(self):
        print("Convertible...", end=" ")
        super().printName()

    def __str__(self):
        return self.type + "... " + super().__str__()


hyundai = Car(color="green", name="hyundai")
hyundai.printName()
print(hyundai, "\n")

noname = Convertible(color="yellow", name="noname", type="convertible")
noname.printName()
print(noname)


def add(*args, **kwargs):

    print(type(args), args)  # tuple <- positional argument
    print(type(kwargs), kwargs)  # dict <- keyword argument
    print("---------------------")

    print(f"hello! {kwargs.get('name')}!")
    result = 0
    for num in args:
        result += num
    print(f"--> result : {result}")