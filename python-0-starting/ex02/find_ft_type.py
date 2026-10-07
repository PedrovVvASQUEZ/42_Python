def all_thing_is_obj(object: any) -> int:

    kind = type(object)

    if kind is list:
        print(f"List : {kind}")
    elif kind is tuple:
        print(f"Tuple : {kind}")
    elif kind is set:
        print(f"Set : {kind}")
    elif kind is dict:
        print(f"Dict : {kind}")
    elif kind is str:
        print(f"{object} is in the kitchen : {kind}")
    else:
        print("Type not found")
    return 42
