def hanoi(n, src, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return
    hanoi(n-1, src, dest, aux)
    print(f"Move disk {n} from {src} to {dest}")
    hanoi(n-1, aux, src, dest)

hanoi(3, 'A', 'B', 'C')