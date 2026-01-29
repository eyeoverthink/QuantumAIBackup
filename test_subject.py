# test_subject.py

def complex_function(a, b, c):
    if a > b:
        if b > c:
            for i in range(a):
                print("Looping...")
            return "Path 1"
        else:
            while c > 0:
                c -= 1
            return "Path 2"
    elif a == b:
        try:
            result = a / (a - c)
            return result
        except ZeroDivisionError:
            return "Error"
    else:
        return "Path 3"

def simple_function(x):
    return x * 2

def helper_one():
    print("Helper one executed")

def helper_two():
    print("Helper two executed")
