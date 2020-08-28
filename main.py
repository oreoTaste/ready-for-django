def add(*args, **kwargs):

    print(type(args), args)  # tuple <- positional argument
    print(type(kwargs), kwargs)  # dict <- keyword argument
    print("---------------------")

    print(f"hello! {kwargs.get('name')}!")
    result = 0
    for num in args:
        result += num
    print(f"--> result : {result}")


add(1, 2, 3, 4, 5, name="Mike")
