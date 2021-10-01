for i in range(1, 334):
    for j in range(i + 1, int((1000 - i) / 2)):
        k = 1000 - i - j
        #steps += 1
        if i**2 + j**2 == k**2:
            print(i, j, k)
