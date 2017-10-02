while 1:
    m, n = input().split()# m:heigt, n:width
    if m == "0" and n == "0":
        break
    for i in range(int(m)):
        for j in range(int(n)):
            if i == 0 or j == 0 or i == int(m)-1 or j == int(n)-1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
