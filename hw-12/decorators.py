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
            key = list(args[0].keys())[0]
            print(
                "Found 1 error during execution of your function:",
                f"{type(e).__name__} no such key as '{key}'",
            )

    return wrapper


@catch_errors
def some_function_with_risky_operation(data: dict) -> str:
    print(data["key"])


some_function_with_risky_operation({"foo": "bar"})
some_function_with_risky_operation({"key": "bar"})
