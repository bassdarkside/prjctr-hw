# |                  --- 1 ---                  |
def is_admin(permission):
    def wrapper(**kwargs):
        key = list(kwargs.keys())[0]
        if kwargs[key] != "admin":
            raise TypeError("Permission denied")
        permission(**kwargs)

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation
    pass


show_customer_receipt(user_type="admin")
show_customer_receipt(user_type="user")


# |                  --- 2 ---                  |
def catch_errors(risky_operation):
    def wrapper(*args, **kwargs):
        try:
            risky_operation(*args, **kwargs)

        except Exception as e:
            print(
                "Found 1 error during execution of your function:",
                f"{type(e).__name__} no such key as 'foo'",
            )

    return wrapper


@catch_errors
def some_function_with_risky_operation(data: dict) -> str:
    print(data["key"])


some_function_with_risky_operation({"foo": "bar"})
some_function_with_risky_operation({"key": "bar"})


# |                  --- 3 ---                  |
def check_types(func):
    def wrapper(*args, **kwargs):
        params_annotations = func.__annotations__
        for i, arg in enumerate(args):
            params_name = list(params_annotations.keys())[i]
            params_type = params_annotations.get(params_name)
            if not isinstance(arg, params_type):
                type_def = str(params_type)[-5:-2]
                type_ = str(type(arg))[-5:-2]
                raise TypeError(
                    f"Argument '{params_name}' must be {type_def}, not {type_}"
                )

        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)
add("1", "2")
