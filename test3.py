def average(*args):
    n=0
    sum = 0.0

    for x in args:
        n=n+1
        sum = sum + x
        t=sum/n
    return t

print average(1, 2)
print average(1, 2, 2, 3, 4)