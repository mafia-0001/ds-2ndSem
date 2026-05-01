def hanoi(n, source, aux, dest):
    if n == 1:
        print(source, "→", dest)
        return
    hanoi(n-1, source, dest, aux)
    print(source, "→", dest)
    hanoi(n-1, aux, source, dest)

hanoi(3, 'A', 'B', 'C')