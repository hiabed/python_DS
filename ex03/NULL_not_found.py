def NULL_not_found(object: any) -> int:

    if object is None: # means null in other languages.
        # We use 'is' because None is a singleton and is used memory identity comparison.
        # (only one instance exists in memory),
        # checking object is None compares memory identity rather than value equality.
        print (f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and object != object: # because naN is not equal to itself
        print (f"Cheese: {object} {type(object)}")
        # print (f"Is NaN: {object != object}") # should be true
        # print (f"Object: {object}")
        return 0
    elif type(object) is int and object == 0:
        print (f"Zero: {object} {type(object)}")
        # print(f"id of int is {id(int)}")
        # print(f"id of object is {id(type(object))}")
        return 0
    elif object is False: # we use 'is' because 0 means false using '=='
        print (f"Fake: {object} {type(object)}")
        return 0
    elif object == "":
        print (f"Empty: {object} {type(object)}")
        return 0
    else:
        print (f"Type not Found")
        return 1
