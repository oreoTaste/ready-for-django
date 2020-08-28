class Car:
    wheel = 4
    door = 4
    window = 4
    seat = 4

    def check_for_start(self):
        try:
            print(f"{self.color} {self.name} [ON] brrrr...")
        except AttributeError:
            print(f"..!don't forget to input color or name")


hyundai = Car()
hyundai.name = "hyundai"
hyundai.check_for_start()
hyundai.color = "red"
hyundai.check_for_start()


def add(*args, **kwargs):

    print(type(args), args)  # tuple <- positional argument
    print(type(kwargs), kwargs)  # dict <- keyword argument
    print("---------------------")

    print(f"hello! {kwargs.get('name')}!")
    result = 0
    for num in args:
        result += num
    print(f"--> result : {result}")