def isEven(n):
    return (n % 2 == 0)

h = int(input("Enter a number to start the Syracuse Conjecture with: "))
output = []
four_two_one = ["4","2","1"]
iterations = 0
while h != 4:
    iterations += 1
    output.append(str(h))
    if isEven(h):
        h = h // 2
    else:
        h = h * 3 + 1
output = ','.join(output), ','.join(four_two_one)
print("Output: ",','.join(output))
print("There were "+str(iterations + 2)+" steps.")
