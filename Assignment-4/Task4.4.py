def print_V(n):
    if n < 3:
        print("❌ Number of rows must be at least 3.")
        return
    for i in range(n):
        print(" " * i + "*", end="")
        inner_space = (2 * (n - i - 1) - 1)
        if inner_space > 0:
            print(" " * inner_space + "*")
        else:
            print() 
n = 3 
print_V(n)
