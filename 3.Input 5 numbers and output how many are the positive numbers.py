positive_count = 0
for count in range(5):
    num = int(input("Enter a number: "))
    if num > 0:
        positive_count += 1

print("Total positive numbers are:", positive_count)