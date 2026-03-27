# tower of hanoi program

def hanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from", a, "to", c)
    else:
        # first move smaller disks
        hanoi(n-1, a, c, b)
        print("Move disk", n, "from", a, "to", c)
        # then move remaining disks
        hanoi(n-1, b, a, c)
# taking number of disks
n = 3
print("Steps are:")
hanoi(n, 'A', 'B', 'C')
