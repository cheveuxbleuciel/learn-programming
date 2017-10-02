while 1:
    m, n = input().split()# m:height, n:width
    if m == "0" and n == "0":
        breaku
    for i in range(int(m)):
        print("#" * int(n))
    print()
