n = 5

# O(n)
count = 0
for i in range(n):
    count += 1
print("O(n) operations:", count)

# O(n^2)
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print("O(n^2) operations:", count)

# O(log n)
count = 0
i = n
while i > 1:
    i //= 2
    count += 1
print("O(log n) operations:", count)