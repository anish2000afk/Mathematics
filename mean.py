def mean(*n):
    count = 0
    sum = 0
    for i in n:
        sum += i
        count += 1
    print(sum / count)


mean(50, 62, 40, 70, 45, 56, 32, 45)
