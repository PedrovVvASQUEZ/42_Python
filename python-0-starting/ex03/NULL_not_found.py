def NULL_not_found(object: any) -> int:

    kind = type(object)

    if object is None :
        print(f"Nothing: {object} {kind}")
    elif kind is float and object != object:
        print(f"Cheese: {object} {kind}")
    elif kind is int and object == 0:
        print(f"Zero: {object} {kind}")
    elif kind is str and object == "":
        print (f"Empty: {kind}")
    elif kind is bool and object is False:
        print(f"Fake: {object} {kind}")
    else:
        print("Type not found")
        return 1
    return 0