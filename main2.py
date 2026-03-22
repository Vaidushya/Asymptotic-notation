def ontime(n):
    iteration = 0
    for i in range(n, n+1):
        iteration += 1
    print(f"When n is {n}, iteration = {iteration}")

ontime(10)
ontime(20)
ontime(42)

print("\n With every 'n' the time taken and iteration will increase")
