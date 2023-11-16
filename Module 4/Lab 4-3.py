def skip_integers(*args):
    for value in args:
        if type(value) == int:
            continue
        else:
            print(value)

skip_integers(3, 5.2, "value", 6.0)
