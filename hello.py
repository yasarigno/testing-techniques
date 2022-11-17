def addThis(x, y):
    # import pdb;pdb.set_trace()
    print(f"This is x={x} and this is y={y}")
    print(f"the type of the first variable {type(x)}")
    print(f"the type of the second variable {type(y)}")

    try:
        result = x+y
    except TypeError:
        print("the wrong type passed")
        result = (int(x)+int(y))
    print(f"Here is the result {result}")
    return result

print (addThis("1",2))
print ("---"*15)
print (addThis(3,5))

