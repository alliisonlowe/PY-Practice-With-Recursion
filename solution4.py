# Write code for algorithm 4 below
def a_to_b(a, b):
    print(f"a: {a}, b: {b}")
    if b<1:
        print("Exponent must be at least 1")
    elif b==1:
        return a
    else:
        return a * a_to_b(a, b-1);

print(f"The power reult is: {a_to_b(2, 4)}")