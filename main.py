# main.py

def append_to_list(value, my_list=[]):  # mutable default argument - bug
    my_list.append(value)
    return my_list

def unsafe_eval(user_input):
    # Dangerous usage of eval - security risk
    return eval(user_input)

def unused_variable_example():
    unused_var = 42  # unused variable - code smell
    print("Function runs but unused_var is never used.")

def division_by_zero():
    x = 1 / 0  # runtime error - division by zero

def main():
    print("Mutable default arg example:")
    print(append_to_list(1))
    print(append_to_list(2))  # unexpected behavior!

    print("\nUnsafe eval example:")
    try:
        print(unsafe_eval("2 + 2"))
        print(unsafe_eval("import os; os.system('echo hacked')"))  # risky!
    except Exception as e:
        print("Caught exception:", e)

    print("\nUnused variable example:")
    unused_variable_example()

    print("\nDivision by zero example:")
    try:
        division_by_zero()
    except Exception as e:
        print("Caught exception:", e)

if __name__ == "__main__":
    main()
