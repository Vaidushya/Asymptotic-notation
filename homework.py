def myfunction(n):
    # First Loop
    for i in range(0, n+1):
        print("First Loop")

    # Second Loop
    j = 1
    while (j <= n+1):
        print("Second Loop", j)
        j = j * 2

    # Third Loop
    for i in range(0, 100):
        print("Third Loop")


myfunction(10)
print("\n As we can see the first loop is O(n), the second loop is O(log n) and the third loop is O(1).")