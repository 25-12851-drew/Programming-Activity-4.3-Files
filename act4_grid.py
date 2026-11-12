
while True:
    n = int(input("Enter size (1-10): "))

    if 1 <= n <= 10:
        break
    else:
        print("Invalid size. Try again.")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
