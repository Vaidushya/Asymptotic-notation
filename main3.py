def onsquaretime(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            iteration += 1
    print("")
    print(f"When n is {n}, iteration = {iteration}")

onsquaretime(5)
onsquaretime(4)
onsquaretime(3)

print("\nWith every 'n' the time taken equals n²")
print("O(n²)")