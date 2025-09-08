total_heads = 35
total_legs = 94

for chickens in range(total_heads + 1):
    rabbits = total_heads - chickens
    legs = (chickens * 2) + (rabbits * 4)

    if legs == total_legs:
        print(f"Chickens: {chickens}")
        print(f"Rabbits: {rabbits}")
        break
else:
    print("No solution found")
    
