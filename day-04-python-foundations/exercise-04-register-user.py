# Question 4 - Custom Exception for User Registration


class InvalidAgeError(Exception):
    pass


def register_user(name, age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Age {age} is not valid for user '{name}'")
    return {"name": name, "age": age}


def try_register(name, age):
    try:
        result = register_user(name, age)
    except InvalidAgeError as e:
        print(f"Registration failed: {e}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        print(f"Registered: {result}")


try_register("Asha", 21)       # succeeds
try_register("Bibek", -5)      # InvalidAgeError
try_register("Chandra", 200)   # InvalidAgeError
