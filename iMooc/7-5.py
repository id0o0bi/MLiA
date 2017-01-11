# Tower of Hanoi
def move(n, a, b, c):
    # print n
    if (n == 1):
        print(a + "-->" + c)
    else :
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(4, 'A', 'B', 'C')