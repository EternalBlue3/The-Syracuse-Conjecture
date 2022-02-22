def isEven(n):
    return (n % 2 == 0)

full_list = []

h = 10
v = 0
for i in range(int(input("How many iterations of the Syracuse do you want to generate: "))):
    iterations = 0
    i += 1
    v += 1
    h = 10
    while h == 10:
        if i == 1:
            h = 0
        iterations += 1
        if isEven(i):
            i = i // 2
        else:
            i = i * 3 + 1
    a = "Checked ", str(v), " This took "+str(iterations - 1)+" iterations\n"
    a = ''.join(a)
    full_list.append(a)
complete = ''.join(full_list)
fh = open("Syracuse Conjecture file.txt","w")
fh.write(complete)
fh.close()
