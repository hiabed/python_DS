def NULL_not_found(object: any) -> int:
    if object is None:
        print (f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and object != object:
        print (f"Cheese: {object} {type(object)}")
        return 0
    elif type(object) is int and object == 0:
        print (f"Zero: {object} {type(object)}")
        return 0
    elif type(object) == bool and object == False:
        print (f"Fake: {object} {type(object)}")
        return 0
    elif object == "":
        print (f"Empty: {object} {type(object)}")
        return 0
    else:
        print (f"Type not Found")
        return 1
