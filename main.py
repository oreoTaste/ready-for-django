class Car:  # class : blueprint of instance
    wheel = 4
    door = 4
    window = 4
    seat = 4


porsche = Car()  # instance : the real object of class
porsche.name = "porsche"
hyundai = Car()
hyundai.name = "hyundai"

print(porsche, porsche.door, porsche.name)
print(hyundai, hyundai.door, hyundai.name)


def add(*args, **kwargs):

    print(type(args), args)  # tuple <- positional argument
    print(type(kwargs), kwargs)  # dict <- keyword argument
    print("---------------------")

    print(f"hello! {kwargs.get('name')}!")
    result = 0
    for num in args:
        result += num
    print(f"--> result : {result}")