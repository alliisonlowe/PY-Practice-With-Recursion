# Write code for algorithm 1 below
def count_down(from_num):
    if from_num <= 0:
        return 
    
    else:
        print(from_num)
        count_down(from_num - 1)

count_down(20)

def count_down_loop(from_num):
    while from_num >= 0:
        print(from_num)
        from_num -= 1

count_down_loop(20)

