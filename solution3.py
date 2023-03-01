# Write code for algorithm 3 below
def nth_fibbonacci(num):
    print(num)
    if num <= 0:
        print("Unable to perform a fibbonacci for zero")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return nth_fibbonacci(num-1) + nth_fibbonacci(num-2)
    
print("Fib: 4")
print(nth_fibbonacci(4))

print("\nFib: 10")
print(nth_fibbonacci(10))
    