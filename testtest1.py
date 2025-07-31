
print("hello")

n = int(input("Enter num: "))
fact = 1
total = 0


for i in range(1 ,n + 1):
    fact *= i
    total += fact



print(f"The sum of factoreal is {total}")

print("bay")