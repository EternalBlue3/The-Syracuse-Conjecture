def isEven(n):
    return (n % 2 == 0)

h = int(input("Enter a number to start the syracuse conjecture with: "))
iterations = 0
while h != 4:
    iterations += 1
    print(h)
    if isEven(h):
        h = h // 2
    else:
        h = h * 3 + 1
print("4\n2\n1") 
print("There were "+str(iterations + 2)+" iterations.")
